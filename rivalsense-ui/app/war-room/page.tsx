"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { WarRoomProgress } from "@/components/war-room-progress";
import { Play, RotateCcw, Sparkles, AlertCircle, Settings } from "lucide-react";
import { motion } from "framer-motion";
import { runWarRoom, checkHealth, type WarRoomResponse } from "@/lib/api";
import { getBusinessProfile, getCompetitors, isProfileSetup, saveAnalysis, saveStrategy, addActivity } from "@/lib/storage";

export default function WarRoomPage() {
  const router = useRouter();
  const [currentStep, setCurrentStep] = useState<number>(-1);
  const [isRunning, setIsRunning] = useState(false);
  const [results, setResults] = useState<WarRoomResponse | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [apiHealthy, setApiHealthy] = useState<boolean | null>(null);
  const [profileSetup, setProfileSetup] = useState(false);

  // Check API health and profile on mount
  useEffect(() => {
    checkApiHealth();
    setProfileSetup(isProfileSetup());
  }, []);

  const checkApiHealth = async () => {
    try {
      await checkHealth();
      setApiHealthy(true);
    } catch (err) {
      setApiHealthy(false);
      console.error("API health check failed:", err);
    }
  };

  const handleStart = async () => {
    // Check if profile is setup before running
    if (!profileSetup) {
      setError("Please complete onboarding first");
      router.push("/onboarding");
      return;
    }

    setError(null);
    setResults(null);
    setCurrentStep(0);
    setIsRunning(true);

    try {
      const profile = getBusinessProfile();
      const competitors = getCompetitors();

      if (!profile || competitors.length === 0) {
        throw new Error("Missing profile or competitor data");
      }

      // Simulate step progression while API call is running
      const progressInterval = setInterval(() => {
        setCurrentStep((prev) => {
          if (prev < 2) return prev + 1;
          return prev;
        });
      }, 2000);

      // Call the actual API with user's data
      const response = await runWarRoom();
      
      clearInterval(progressInterval);
      setCurrentStep(2);
      setResults(response);
      
      // Save analysis results to localStorage
      if (response.analyst) {
        saveAnalysis({
          threatScore: response.analyst.threat_score || 0,
          impactLevel: response.analyst.impact_level || "medium",
          summary: response.analyst.summary || "",
          priceDifferencePercent: response.analyst.price_difference_percent || 0,
          pricingGap: response.analyst.pricing_gap || "",
          marketRisk: response.analyst.market_risk || "",
          recommendedUrgency: response.analyst.recommended_urgency || "moderate",
          keyInsights: response.analyst.key_insights || [],
          competitorBreakdown: response.analyst.competitor_breakdown || [],
          timestamp: new Date().toISOString(),
        });
      }
      
      // Save strategy results to localStorage
      if (response.strategist) {
        saveStrategy({
          recommendedAction: {
            title: response.strategist.strategy_title || "Strategic Response",
            description: response.strategist.recommended_strategy || "",
            urgency: response.analyst?.recommended_urgency || "moderate",
          },
          priceAction: {
            type: response.strategist.pricing_recommendation || "maintain",
            description: response.strategist.pricing_recommendation || "",
          },
          campaignIdea: {
            title: response.strategist.campaign_ideas?.[0] || "Marketing Campaign",
            description: response.strategist.campaign_ideas?.join(" • ") || "",
          },
          marketingPost: {
            text: response.strategist.marketing_post?.content || "",
          },
          executionSteps: response.strategist.action_steps || [],
          strategyRationale: response.strategist.recommended_strategy || "",
          timestamp: new Date().toISOString(),
        });
      }
      
      // Add activity entry for this War Room run
      const competitorsFound = response.scout?.competitors_found || competitors.length;
      const threatScore = response.analyst?.threat_score || 0;
      addActivity({
        id: crypto.randomUUID(),
        competitorName: "All Competitors",
        activityType: "war_room_run",
        title: "War Room Analysis Complete",
        description: `Analyzed ${competitorsFound} competitors with ${threatScore}/10 threat score`,
        threatScore: threatScore,
        timestamp: new Date().toISOString(),
      });
      
      // Wait a moment before marking complete
      setTimeout(() => {
        setIsRunning(false);
      }, 1000);

    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to run War Room");
      setIsRunning(false);
      setCurrentStep(-1);
      console.error("War Room execution failed:", err);
    }
  };

  const handleReset = () => {
    setCurrentStep(-1);
    setIsRunning(false);
    setResults(null);
    setError(null);
  };

  const isComplete = currentStep === 2 && !isRunning && results !== null;

  return (
    <div className="space-y-8 pb-8">
      {/* Header */}
      <div className="space-y-1">
        <h1 className="text-4xl font-bold tracking-tight">War Room</h1>
        <p className="text-muted-foreground text-base">
          Run your AI agents to analyze the market and generate strategies
        </p>
      </div>

      {/* API Health Warning */}
      {apiHealthy === false && (
        <Card className="border-warning/30 bg-warning/5 luxury-card">
          <CardContent className="p-6">
            <div className="flex items-start gap-4">
              <AlertCircle className="h-6 w-6 text-warning flex-shrink-0 mt-0.5" />
              <div>
                <h4 className="font-bold text-warning mb-1">Backend API Not Available</h4>
                <p className="text-sm text-muted-foreground">
                  The FastAPI backend is not running. Start it with:{" "}
                  <code className="px-2 py-1 bg-background rounded text-xs gold-accent">
                    python api_server.py
                  </code>
                </p>
                <Button 
                  size="sm" 
                  variant="outline" 
                  onClick={checkApiHealth} 
                  className="mt-3 border-primary/30"
                >
                  Retry Connection
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Profile Setup Warning */}
      {!profileSetup && (
        <Card className="border-primary/30 bg-primary/5 luxury-card">
          <CardContent className="p-6">
            <div className="flex items-start gap-4">
              <Settings className="h-6 w-6 text-primary flex-shrink-0 mt-0.5" />
              <div className="flex-1">
                <h4 className="font-bold text-primary mb-1">Complete Your Profile First</h4>
                <p className="text-sm text-muted-foreground mb-3">
                  The War Room needs your business profile and competitor information to run analysis. 
                  Complete the quick onboarding to get started.
                </p>
                <Button 
                  size="sm" 
                  onClick={() => router.push("/onboarding")}
                  className="gap-2 premium-button"
                >
                  <Sparkles className="h-4 w-4" />
                  Complete Onboarding
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Error Display */}
      {error && (
        <Card className="border-rose-500/30 bg-rose-500/5">
          <CardContent className="p-6">
            <div className="flex items-start gap-4">
              <AlertCircle className="h-6 w-6 text-rose-500 flex-shrink-0 mt-0.5" />
              <div>
                <h4 className="font-bold text-rose-500 mb-1">Error</h4>
                <p className="text-sm text-muted-foreground">{error}</p>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Controls */}
      <Card className="overflow-hidden border-primary/30 bg-gradient-to-br from-primary/5 via-accent/5 to-primary/10 luxury-card glow-gold">
        <CardContent className="p-8">
          <div className="flex flex-col sm:flex-row items-center justify-between gap-6">
            <div className="flex items-center gap-4">
              <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-primary/20 to-accent/20 border-2 border-primary/40 glow-gold">
                <Sparkles className="h-8 w-8 text-primary" />
              </div>
              <div>
                <h3 className="text-xl font-bold mb-1 gold-accent">AI Market Intelligence</h3>
                <p className="text-sm text-muted-foreground">
                  {isRunning
                    ? "Analysis in progress..."
                    : isComplete
                    ? "Analysis complete! Check your results below."
                    : "Ready to analyze your competitive landscape"}
                </p>
              </div>
            </div>
            <div className="flex gap-3">
              {!isRunning && !isComplete && (
                <Button 
                  size="lg" 
                  onClick={handleStart} 
                  className="gap-2 premium-button"
                  disabled={apiHealthy === false}
                >
                  <Play className="h-5 w-5 fill-current" />
                  Start Analysis
                </Button>
              )}
              {(isComplete || currentStep >= 0) && (
                <Button size="lg" variant="outline" onClick={handleReset} className="gap-2 border-primary/30">
                  <RotateCcw className="h-5 w-5" />
                  Reset
                </Button>
              )}
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Progress Component */}
      {currentStep >= 0 && (
        <motion.div
          initial={{ opacity: 0, y: 20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.5 }}
        >
          <Card className="overflow-hidden luxury-card border-primary/20">
            <CardHeader className="border-b border-border/40 bg-card/50">
              <CardTitle className="text-2xl gold-accent">Agent Pipeline</CardTitle>
              <CardDescription className="text-base">
                Your AI agents are working together to deliver insights
              </CardDescription>
            </CardHeader>
            <CardContent className="p-12">
              <WarRoomProgress currentStep={currentStep} />
            </CardContent>
          </Card>
        </motion.div>
      )}

      {/* Completion Card */}
      {isComplete && results && (
        <motion.div
          initial={{ opacity: 0, scale: 0.9 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.5, delay: 0.3 }}
          className="space-y-6"
        >
          {/* Success Banner */}
          <Card className="overflow-hidden bg-gradient-to-br from-success/10 via-success/15 to-primary/10 border-success/30 luxury-card glow-gold">
            <CardContent className="p-12 text-center">
              <div className="flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-success/20 to-primary/20 border-2 border-success/50 mx-auto mb-6 glow-gold">
                <Sparkles className="h-10 w-10 text-success" />
              </div>
              <h3 className="text-3xl font-bold mb-4">Analysis Complete! 🎉</h3>
              <p className="text-lg text-muted-foreground mb-8 max-w-2xl mx-auto">
                Your AI agents have successfully analyzed the market. Review the insights below.
              </p>
            </CardContent>
          </Card>

          {/* Results Grid */}
          <div className="grid gap-6 md:grid-cols-2">
            {/* Analyst Results */}
            <Card>
              <CardHeader className="border-b border-border/40 bg-card/50">
                <CardTitle className="text-xl">Market Analysis</CardTitle>
                <CardDescription>Agent B: Analyst Results</CardDescription>
              </CardHeader>
              <CardContent className="p-6 space-y-4">
                <div>
                  <span className="text-sm font-medium text-muted-foreground uppercase tracking-wide">
                    Impact Level
                  </span>
                  <p className="text-2xl font-bold mt-1 capitalize">
                    {results.analyst.impact_level}
                  </p>
                </div>

                {results.analyst.threat_score && (
                  <div>
                    <span className="text-sm font-medium text-muted-foreground uppercase tracking-wide">
                      Threat Score
                    </span>
                    <p className="text-2xl font-bold mt-1">
                      {results.analyst.threat_score.toFixed(1)} / 10
                    </p>
                  </div>
                )}

                <div>
                  <span className="text-sm font-medium text-muted-foreground uppercase tracking-wide">
                    Summary
                  </span>
                  <p className="text-sm mt-2 leading-relaxed">
                    {results.analyst.summary}
                  </p>
                </div>

                {results.analyst.key_insights && results.analyst.key_insights.length > 0 && (
                  <div>
                    <span className="text-sm font-medium text-muted-foreground uppercase tracking-wide">
                      Key Insights
                    </span>
                    <ul className="mt-2 space-y-2">
                      {results.analyst.key_insights.slice(0, 3).map((insight, idx) => (
                        <li key={idx} className="text-sm flex items-start gap-2">
                          <span className="text-primary mt-1">•</span>
                          <span className="leading-relaxed">{insight}</span>
                        </li>
                      ))}
                    </ul>
                  </div>
                )}
              </CardContent>
            </Card>

            {/* Strategist Results */}
            <Card>
              <CardHeader className="border-b border-border/40 bg-card/50">
                <CardTitle className="text-xl">Strategy</CardTitle>
                <CardDescription>Agent C: Strategist Recommendations</CardDescription>
              </CardHeader>
              <CardContent className="p-6 space-y-4">
                <div>
                  <span className="text-sm font-medium text-muted-foreground uppercase tracking-wide">
                    Recommended Strategy
                  </span>
                  <p className="text-2xl font-bold mt-1">
                    {results.strategist.strategy_title || results.strategist.recommended_strategy}
                  </p>
                </div>

                {results.strategist.action_steps && results.strategist.action_steps.length > 0 && (
                  <div>
                    <span className="text-sm font-medium text-muted-foreground uppercase tracking-wide">
                      Action Steps
                    </span>
                    <ol className="mt-2 space-y-2">
                      {results.strategist.action_steps.slice(0, 3).map((step, idx) => (
                        <li key={idx} className="text-sm flex items-start gap-2">
                          <span className="text-primary font-bold mt-0.5">{idx + 1}.</span>
                          <span className="leading-relaxed">{step}</span>
                        </li>
                      ))}
                    </ol>
                  </div>
                )}

                {results.strategist.pricing_recommendation && (
                  <div>
                    <span className="text-sm font-medium text-muted-foreground uppercase tracking-wide">
                      Pricing Recommendation
                    </span>
                    <p className="text-sm mt-2 leading-relaxed">
                      {results.strategist.pricing_recommendation}
                    </p>
                  </div>
                )}
              </CardContent>
            </Card>
          </div>

          {/* Marketing Post */}
          {results.strategist.marketing_post && (
            <Card className="bg-gradient-to-br from-purple-500/5 to-pink-500/5 border-purple-500/20">
              <CardHeader className="border-b border-border/40 bg-card/50">
                <CardTitle className="text-xl">Ready-to-Use Marketing Content</CardTitle>
                <CardDescription>
                  Platform: {results.strategist.marketing_post.platform}
                </CardDescription>
              </CardHeader>
              <CardContent className="p-8 space-y-4">
                <div className="bg-background/50 rounded-xl p-6 border border-border/40">
                  <p className="text-base leading-relaxed whitespace-pre-line">
                    {results.strategist.marketing_post.content}
                  </p>
                </div>

                <div>
                  <span className="text-sm font-medium text-muted-foreground uppercase tracking-wide">
                    Caption
                  </span>
                  <p className="text-sm mt-2 leading-relaxed">
                    {results.strategist.marketing_post.caption}
                  </p>
                </div>

                {results.strategist.marketing_post.cta && (
                  <div>
                    <span className="text-sm font-medium text-muted-foreground uppercase tracking-wide">
                      Call to Action
                    </span>
                    <p className="text-sm mt-2 leading-relaxed font-bold">
                      {results.strategist.marketing_post.cta}
                    </p>
                  </div>
                )}
              </CardContent>
            </Card>
          )}

          {/* Action Buttons */}
          <div className="flex items-center justify-center gap-4">
            <Button size="lg" onClick={() => window.location.href = '/dashboard'}>
              View Dashboard
            </Button>
            <Button size="lg" variant="outline" onClick={() => window.location.href = '/strategy'}>
              View Full Strategy
            </Button>
          </div>
        </motion.div>
      )}

      {/* Info Cards */}
      {currentStep < 0 && (
        <div className="grid gap-6 md:grid-cols-3">
          <Card className="hover:shadow-lg transition-all duration-300">
            <CardContent className="pt-6 space-y-4">
              <div className="flex h-14 w-14 items-center justify-center rounded-xl bg-indigo-500/10 border border-indigo-500/20">
                <Sparkles className="h-7 w-7 text-indigo-500" />
              </div>
              <div>
                <h4 className="font-bold text-lg mb-2">Scout Agent</h4>
                <p className="text-sm text-muted-foreground leading-relaxed">
                  Continuously monitors competitor pricing, promotions, and market movements
                  in real-time.
                </p>
              </div>
            </CardContent>
          </Card>

          <Card className="hover:shadow-lg transition-all duration-300">
            <CardContent className="pt-6 space-y-4">
              <div className="flex h-14 w-14 items-center justify-center rounded-xl bg-purple-500/10 border border-purple-500/20">
                <Sparkles className="h-7 w-7 text-purple-500" />
              </div>
              <div>
                <h4 className="font-bold text-lg mb-2">Analyst Agent</h4>
                <p className="text-sm text-muted-foreground leading-relaxed">
                  Evaluates competitive threats, calculates market pressure, and identifies
                  opportunities.
                </p>
              </div>
            </CardContent>
          </Card>

          <Card className="hover:shadow-lg transition-all duration-300">
            <CardContent className="pt-6 space-y-4">
              <div className="flex h-14 w-14 items-center justify-center rounded-xl bg-pink-500/10 border border-pink-500/20">
                <Sparkles className="h-7 w-7 text-pink-500" />
              </div>
              <div>
                <h4 className="font-bold text-lg mb-2">Strategist Agent</h4>
                <p className="text-sm text-muted-foreground leading-relaxed">
                  Generates actionable strategies with ready-to-use marketing content and
                  execution plans.
                </p>
              </div>
            </CardContent>
          </Card>
        </div>
      )}
    </div>
  );
}
