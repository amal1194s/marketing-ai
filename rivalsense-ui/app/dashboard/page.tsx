"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { TrendingUp, AlertTriangle, Eye, Activity, Sparkles, Building2, Clock, ArrowRight } from "lucide-react";
import { getThreatColor, getThreatBadgeColor } from "@/lib/utils";
import { motion } from "framer-motion";
import Link from "next/link";
import { getDashboardSummary, isProfileSetup } from "@/lib/storage";

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1,
    },
  },
};

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 },
};

export default function DashboardPage() {
  const router = useRouter();
  const [dashboardData, setDashboardData] = useState<any>(null);
  const [profileSetup, setProfileSetup] = useState(false);

  useEffect(() => {
    const setup = isProfileSetup();
    setProfileSetup(setup);
    
    if (setup) {
      const data = getDashboardSummary();
      setDashboardData(data);
    }
  }, []);

  // Empty state when profile is not setup
  if (!profileSetup) {
    return (
      <div className="space-y-8 pb-8">
        <div className="space-y-1">
          <h1 className="text-4xl font-bold tracking-tight">Dashboard</h1>
          <p className="text-muted-foreground text-base">
            Your market intelligence command center
          </p>
        </div>

        <Card className="border-2 border-dashed border-border/50">
          <CardContent className="flex flex-col items-center justify-center py-24 px-6">
            <div className="flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-primary/20 to-accent/20 border-2 border-primary/30 mb-6 glow-gold">
              <Sparkles className="h-10 w-10 text-primary" />
            </div>
            <h3 className="text-2xl font-bold mb-3">Welcome to RivalSense AI</h3>
            <p className="text-muted-foreground text-center max-w-md mb-6">
              Get started by completing your business profile. Our AI agents will then monitor your competitors 
              and provide real-time market intelligence tailored to your business.
            </p>
            <Button 
              size="lg" 
              onClick={() => router.push("/onboarding")}
              className="gap-2 premium-button"
            >
              <Sparkles className="h-5 w-5" />
              Complete Onboarding
            </Button>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="space-y-8 pb-8">
      {/* Header */}
      <div className="flex items-center justify-between">
        <div className="space-y-1">
          <h1 className="text-4xl font-bold tracking-tight gold-accent">Dashboard</h1>
          <p className="text-muted-foreground text-base">
            Welcome back! Here's what's happening with your {dashboardData?.profile?.category || 'business'}.
          </p>
        </div>
        <div className="flex items-center gap-3">
          <div className="flex items-center gap-2 px-3 py-2 rounded-lg bg-success/10 border border-success/20">
            <div className="h-2 w-2 rounded-full bg-success animate-pulse" />
            <span className="text-sm font-medium text-success">Live monitoring</span>
          </div>
        </div>
      </div>

      {/* Business Profile Card */}
      {dashboardData?.profile && (
        <Card className="border-primary/20 bg-gradient-to-br from-primary/5 via-accent/5 to-primary/10 luxury-card glow-gold">
          <CardContent className="p-6">
            <div className="flex items-start gap-4">
              <div className="flex h-14 w-14 items-center justify-center rounded-xl bg-gradient-to-br from-primary/20 to-accent/20 border-2 border-primary/30 flex-shrink-0 glow-gold">
                <Building2 className="h-7 w-7 text-primary" />
              </div>
              <div className="flex-1 min-w-0">
                <h3 className="text-xl font-bold mb-1 gold-accent">{dashboardData.profile.name}</h3>
                <div className="flex flex-wrap gap-3 text-sm text-muted-foreground mb-3">
                  <span className="flex items-center gap-1.5">
                    <span className="font-medium text-foreground">{dashboardData.profile.category}</span>
                  </span>
                  <span>•</span>
                  <span>{dashboardData.profile.city}</span>
                  <span>•</span>
                  <span>{dashboardData.competitorCount} competitors tracked</span>
                </div>
                <p className="text-sm text-muted-foreground line-clamp-2">{dashboardData.profile.usp}</p>
              </div>
              <Button 
                variant="outline" 
                size="sm"
                onClick={() => router.push("/settings")}
              >
                Edit Profile
              </Button>
            </div>
          </CardContent>
        </Card>
      )}

      {/* No Competitors Empty State */}
      {dashboardData && dashboardData.competitorCount === 0 && (
        <Card className="border-2 border-dashed border-border/50">
          <CardContent className="flex flex-col items-center justify-center py-16 px-6">
            <div className="flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-primary/20 to-accent/20 border-2 border-primary/30 mb-4 glow-gold">
              <Eye className="h-8 w-8 text-primary" />
            </div>
            <h3 className="text-xl font-bold mb-2">No Competitors Yet</h3>
            <p className="text-muted-foreground text-center max-w-md mb-4">
              Discover competitors in your market to start tracking their activities and get AI-powered insights.
            </p>
            <Button 
              onClick={() => router.push("/discover-competitors")}
              className="gap-2 premium-button"
            >
              <Sparkles className="h-4 w-4" />
              Discover Competitors
            </Button>
          </CardContent>
        </Card>
      )}

      {/* Stats Grid */}
      {dashboardData && dashboardData.competitorCount > 0 && (
        <>
          <motion.div
            variants={container}
            initial="hidden"
            animate="show"
            className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4"
          >
            <motion.div variants={item}>
              <Card className="hover:border-primary/50 transition-all duration-300 hover:shadow-xl hover:shadow-primary/5 cursor-pointer group luxury-card">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-3">
                  <CardTitle className="text-sm font-semibold text-muted-foreground">
                    Threat Score
                  </CardTitle>
                  <AlertTriangle className={`h-5 w-5 ${dashboardData.analysis ? getThreatColor(dashboardData.analysis.threatScore) : 'text-muted-foreground'} transition-transform group-hover:scale-110`} />
                </CardHeader>
                <CardContent className="space-y-2">
                  <div className="text-4xl font-bold tracking-tight gold-accent">
                    {dashboardData.analysis?.threatScore || '--'}
                    <span className="text-muted-foreground text-xl font-normal">/10</span>
                  </div>
                  <p className="text-xs font-medium">
                    {dashboardData.analysis ? (
                      <span className={getThreatColor(dashboardData.analysis.threatScore)}>
                        {dashboardData.analysis.impactLevel.charAt(0).toUpperCase() + dashboardData.analysis.impactLevel.slice(1)} impact
                      </span>
                    ) : (
                      <span className="text-muted-foreground">Run War Room for insights</span>
                    )}
                  </p>
                </CardContent>
              </Card>
            </motion.div>

            <motion.div variants={item}>
              <Card className="hover:border-warning/50 transition-all duration-300 hover:shadow-xl hover:shadow-warning/5 cursor-pointer group luxury-card">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-3">
                  <CardTitle className="text-sm font-semibold text-muted-foreground">
                    High Threats
                  </CardTitle>
                  <TrendingUp className="h-5 w-5 text-warning transition-transform group-hover:scale-110" />
                </CardHeader>
                <CardContent className="space-y-2">
                  <div className="text-4xl font-bold tracking-tight gold-accent">{dashboardData.highThreatCount}</div>
                  <p className="text-xs font-medium text-muted-foreground">
                    Competitors need attention
                  </p>
                </CardContent>
              </Card>
            </motion.div>

            <motion.div variants={item}>
              <Card className="hover:border-rose-500/50 transition-all duration-300 hover:shadow-xl hover:shadow-rose-500/5 cursor-pointer group luxury-card">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-3">
                  <CardTitle className="text-sm font-semibold text-muted-foreground">
                    Active Promotions
                  </CardTitle>
                  <Activity className="h-5 w-5 text-rose-500 transition-transform group-hover:scale-110" />
                </CardHeader>
                <CardContent className="space-y-2">
                  <div className="text-4xl font-bold tracking-tight gold-accent">{dashboardData.activePromotions}</div>
                  <p className="text-xs font-medium text-muted-foreground">
                    Running campaigns
                  </p>
                </CardContent>
              </Card>
            </motion.div>

            <motion.div variants={item}>
              <Card className="hover:border-success/50 transition-all duration-300 hover:shadow-xl hover:shadow-success/5 cursor-pointer group luxury-card">
                <CardHeader className="flex flex-row items-center justify-between space-y-0 pb-3">
                  <CardTitle className="text-sm font-semibold text-muted-foreground">
                    Monitoring
                  </CardTitle>
                  <Eye className="h-5 w-5 text-success transition-transform group-hover:scale-110" />
                </CardHeader>
                <CardContent className="space-y-2">
                  <div className="text-4xl font-bold tracking-tight gold-accent">{dashboardData.competitorCount}</div>
                  <p className="text-xs font-medium text-muted-foreground">
                    Competitors tracked
                  </p>
                </CardContent>
              </Card>
            </motion.div>
          </motion.div>

          {/* Recent Activity Section */}
          <div className="grid gap-6 lg:grid-cols-2">
            <Card className="overflow-hidden luxury-card">
              <CardHeader className="border-b border-border/40 bg-card/50">
                <CardTitle className="text-xl gold-accent">Recent Competitive Activity</CardTitle>
                <p className="text-sm text-muted-foreground mt-1">Latest updates from your competitors</p>
              </CardHeader>
              <CardContent className="pt-6">
                {dashboardData.recentActivities && dashboardData.recentActivities.length > 0 ? (
                  <div className="space-y-3">
                    {dashboardData.recentActivities.map((activity: any, idx: number) => (
                      <motion.div
                        key={activity.id}
                        initial={{ opacity: 0, x: -10 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: idx * 0.05 }}
                        className="flex items-start gap-4 p-4 rounded-xl bg-accent/30 hover:bg-accent/60 transition-all duration-200 border border-transparent hover:border-border/50 cursor-pointer group"
                      >
                        <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-primary/10 border border-primary/20 shadow-sm group-hover:scale-105 transition-transform">
                          <Activity className="h-5 w-5 text-primary" />
                        </div>
                        <div className="flex-1 min-w-0">
                          <p className="font-bold text-sm mb-0.5">{activity.competitorName}</p>
                          <p className="text-sm text-foreground mb-1">{activity.title}</p>
                          <p className="text-xs text-muted-foreground flex items-center gap-2">
                            <Clock className="h-3 w-3" />
                            {new Date(activity.timestamp).toLocaleDateString()}
                          </p>
                        </div>
                        {activity.threatScore && (
                          <div className={`px-2 py-1 rounded-lg text-xs font-semibold ${getThreatBadgeColor(activity.threatScore)}`}>
                            {activity.threatScore}
                          </div>
                        )}
                      </motion.div>
                    ))}
                  </div>
                ) : (
                  <div className="text-center py-8">
                    <p className="text-muted-foreground text-sm mb-4">No activity yet</p>
                    <Button onClick={() => router.push("/war-room")} variant="outline" size="sm" className="gap-2">
                      <Sparkles className="h-4 w-4" />
                      Run War Room
                    </Button>
                  </div>
                )}
              </CardContent>
            </Card>

            {/* Key Insights */}
            <Card className="overflow-hidden luxury-card">
              <CardHeader className="border-b border-border/40 bg-card/50">
                <CardTitle className="text-xl gold-accent">Key Insights</CardTitle>
                <p className="text-sm text-muted-foreground mt-1">AI-powered competitive intelligence</p>
              </CardHeader>
              <CardContent className="pt-6">
                {dashboardData.analysis?.keyInsights && dashboardData.analysis.keyInsights.length > 0 ? (
                  <div className="space-y-3">
                    {dashboardData.analysis.keyInsights.map((insight: string, index: number) => (
                      <motion.div
                        key={index}
                        initial={{ opacity: 0, x: -10 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: index * 0.05 }}
                        className="flex items-start gap-3 p-4 rounded-xl bg-accent/30 border border-border/30"
                      >
                        <div className="flex h-6 w-6 items-center justify-center rounded-full bg-primary/20 text-primary font-bold text-xs flex-shrink-0 mt-0.5">
                          {index + 1}
                        </div>
                        <p className="text-sm text-foreground leading-relaxed">{insight}</p>
                      </motion.div>
                    ))}
                  </div>
                ) : (
                  <div className="text-center py-8">
                    <p className="text-muted-foreground text-sm mb-4">No insights yet</p>
                    <Button onClick={() => router.push("/war-room")} variant="outline" size="sm" className="gap-2">
                      <Sparkles className="h-4 w-4" />
                      Run Analysis
                    </Button>
                  </div>
                )}
              </CardContent>
            </Card>
          </div>

          {/* Strategy Recommendations */}
          {dashboardData.strategy && (
            <Card className="luxury-card glow-gold border-primary/20">
              <CardHeader>
                <CardTitle className="text-xl gold-accent">Recommended Strategy</CardTitle>
                <p className="text-sm text-muted-foreground mt-1">AI-generated action plan</p>
              </CardHeader>
              <CardContent className="space-y-4">
                <div className="p-4 rounded-xl bg-gradient-to-r from-primary/10 via-accent/10 to-primary/10 border border-primary/20">
                  <h4 className="font-bold mb-2 gold-accent">{dashboardData.strategy.recommendedAction.title}</h4>
                  <p className="text-sm text-foreground mb-3">{dashboardData.strategy.recommendedAction.description}</p>
                  <Link href="/strategy">
                    <Button size="sm" className="gap-2 premium-button">
                      View Full Strategy
                      <ArrowRight className="h-4 w-4" />
                    </Button>
                  </Link>
                </div>
              </CardContent>
            </Card>
          )}
        </>
      )}
    </div>
  );
}
