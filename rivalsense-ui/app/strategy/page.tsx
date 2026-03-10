"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Copy, CheckCircle2, Target, DollarSign, Megaphone, ListChecks, Lightbulb, Sparkles } from "lucide-react";
import { getStrategy } from "@/lib/storage";
import { motion } from "framer-motion";
import type { StrategyResult } from "@/lib/storage";

const urgencyColors = {
  immediate: "bg-rose-500/10 text-rose-500 border-rose-500/20",
  high: "bg-amber-500/10 text-amber-500 border-amber-500/20",
  moderate: "bg-blue-500/10 text-blue-500 border-blue-500/20",
  low: "bg-emerald-500/10 text-emerald-500 border-emerald-500/20",
};

export default function StrategyPage() {
  const router = useRouter();
  const [strategy, setStrategy] = useState<StrategyResult | null>(null);
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    const data = getStrategy();
    setStrategy(data);
  }, []);

  const copyToClipboard = () => {
    if (strategy?.marketingPost?.text) {
      navigator.clipboard.writeText(strategy.marketingPost.text);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    }
  };

  // Show empty state if no strategy data
  if (!strategy) {
    return (
      <div className="space-y-8 pb-8">
        <div className="space-y-1">
          <h1 className="text-4xl font-bold tracking-tight">Strategic Recommendations</h1>
          <p className="text-muted-foreground text-base">
            AI-generated action plan for your business
          </p>
        </div>
        
        <Card className="border-primary/30 bg-gradient-to-br from-primary/5 via-accent/5 to-primary/10 luxury-card glow-gold">
          <CardContent className="p-12 text-center">
            <div className="flex flex-col items-center gap-4">
              <div className="flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-primary/20 to-accent/20 border-2 border-primary/40">
                <Sparkles className="h-10 w-10 text-primary" />
              </div>
              <div>
                <h3 className="text-xl font-bold mb-2 gold-accent">No Strategy Data Available</h3>
                <p className="text-muted-foreground mb-4">
                  Run the War Room to generate AI-powered strategic recommendations
                </p>
                <Button onClick={() => router.push("/war-room")} className="gap-2 premium-button">
                  <Sparkles className="h-4 w-4" />
                  Run War Room
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>
      </div>
    );
  }

  return (
    <div className="space-y-8 pb-8">
      {/* Header */}
      <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-4">
        <div className="space-y-1">
          <h1 className="text-4xl font-bold tracking-tight">Strategic Recommendations</h1>
          <p className="text-muted-foreground text-base">
            AI-generated action plan for your business
          </p>
        </div>
        <div className={`px-4 py-2.5 rounded-xl text-sm font-bold uppercase tracking-wide border shadow-lg whitespace-nowrap ${
          urgencyColors[strategy.recommendedAction.urgency as keyof typeof urgencyColors] || urgencyColors.moderate
        }`}>
          {strategy.recommendedAction.urgency.toUpperCase()} URGENCY
        </div>
      </div>

      {/* Recommended Action */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <Card className="bg-gradient-to-br from-primary/10 via-accent/15 to-primary/10 border-primary/30 overflow-hidden relative luxury-card glow-gold">
          <div className="absolute inset-0 bg-gradient-to-r from-primary/5 to-accent/5 opacity-0 group-hover:opacity-100 transition-opacity" />
          <CardHeader className="relative">
            <CardTitle className="flex items-center gap-3 text-2xl gold-accent">
              <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-primary/20 border border-primary/30 glow-gold">
                <Target className="h-6 w-6 text-primary" />
              </div>
              Recommended Action
            </CardTitle>
          </CardHeader>
          <CardContent className="relative">
            <p className="text-lg text-foreground leading-relaxed">
              {strategy.recommendedAction.description}
            </p>
          </CardContent>
        </Card>
      </motion.div>

      <div className="grid gap-6 lg:grid-cols-2">
        {/* Price Action */}
        <Card className="luxury-card hover:border-primary/30 transition-all duration-300 group">
          <CardHeader className="pb-4">
            <CardTitle className="flex items-center gap-2 text-xl">
              <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-success/10 border border-success/20 group-hover:scale-110 transition-transform">
                <DollarSign className="h-5 w-5 text-success" />
              </div>
              Pricing Action
            </CardTitle>
            <CardDescription className="text-base mt-2">Recommended pricing strategy</CardDescription>
          </CardHeader>
          <CardContent>
            <p className="text-foreground leading-relaxed">
              {strategy.priceAction.description}
            </p>
          </CardContent>
        </Card>

        {/* Campaign Idea */}
        <Card className="luxury-card hover:border-primary/30 transition-all duration-300 group">
          <CardHeader className="pb-4">
            <CardTitle className="flex items-center gap-2 text-xl">
              <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/10 border border-primary/20 group-hover:scale-110 transition-transform">
                <Megaphone className="h-5 w-5 text-primary" />
              </div>
              Campaign Idea
            </CardTitle>
            <CardDescription className="text-base mt-2">Marketing campaign concept</CardDescription>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-4 p-5 rounded-xl bg-primary/10 border border-primary/20 glow-gold">
              <div className="flex h-14 w-14 items-center justify-center rounded-xl bg-primary/20 shrink-0">
                <Megaphone className="h-7 w-7 text-primary" />
              </div>
              <p className="text-lg font-bold text-foreground flex-1">
                {strategy.campaignIdea.description}
              </p>
            </div>
          </CardContent>
        </Card>
      </div>

      {/* Marketing Post */}
      <Card className="overflow-hidden luxury-card border-primary/20">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
            <div className="space-y-2">
              <CardTitle className="flex items-center gap-2 text-xl">
                <Megaphone className="h-5 w-5 text-primary" />
                Ready-to-Use Marketing Post
              </CardTitle>
              <CardDescription className="text-base">
                Copy and paste directly to your social media platforms
              </CardDescription>
            </div>
            <Button
              onClick={copyToClipboard}
              variant="outline"
              className="gap-2 shadow-md whitespace-nowrap border-primary/30"
            >
              {copied ? (
                <>
                  <CheckCircle2 className="h-4 w-4 text-success" />
                  <span className="text-success">Copied!</span>
                </>
              ) : (
                <>
                  <Copy className="h-4 w-4" />
                  Copy Post
                </>
              )}
            </Button>
          </div>
        </CardHeader>
        <CardContent className="pt-6 space-y-4">
          <div className="rounded-2xl bg-accent/40 p-8 border border-border/50 hover:bg-accent/60 transition-all">
            <p className="text-foreground whitespace-pre-line leading-relaxed text-base">
              {strategy.marketingPost.text}
            </p>
          </div>
          <div className="p-5 rounded-xl bg-primary/10 border border-primary/30">
            <p className="text-sm font-bold text-primary mb-2 uppercase tracking-wide">Strategy Title:</p>
            <p className="text-foreground text-base leading-relaxed">{strategy.recommendedAction.title}</p>
          </div>
        </CardContent>
      </Card>

      {/* Execution Steps */}
      <Card className="overflow-hidden luxury-card border-primary/20">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <CardTitle className="flex items-center gap-2 text-xl">
            <ListChecks className="h-5 w-5 text-success" />
            Execution Steps
          </CardTitle>
          <CardDescription className="text-base mt-2">Follow these steps to implement the strategy</CardDescription>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="space-y-3">
            {strategy.executionSteps.map((step, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1 }}
                className="flex items-start gap-4 p-5 rounded-xl bg-accent/30 hover:bg-accent/60 transition-all duration-200 border border-transparent hover:border-primary/30 cursor-pointer group"
              >
                <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-success/10 text-success border border-success/20 shrink-0 group-hover:bg-success group-hover:text-white transition-all font-bold text-sm">
                  {index + 1}
                </div>
                <p className="text-sm text-foreground leading-relaxed flex-1 pt-1.5">
                  {step}
                </p>
              </motion.div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Strategy Rationale */}
      <Card className="overflow-hidden luxury-card border-primary/20">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <CardTitle className="flex items-center gap-2 text-xl">
            <Lightbulb className="h-5 w-5 text-primary" />
            Why This Strategy?
          </CardTitle>
          <CardDescription className="text-base mt-2">The reasoning behind our recommendation</CardDescription>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="p-5 rounded-xl bg-accent/30 border border-border/30">
            <p className="text-foreground leading-relaxed">
              {strategy.strategyRationale}
            </p>
          </div>
        </CardContent>
      </Card>

      {/* Action Footer */}
      <Card className="bg-gradient-to-br from-success/10 via-success/15 to-primary/10 border-success/30 overflow-hidden relative luxury-card glow-gold">
        <div className="absolute inset-0 bg-gradient-to-r from-success/5 to-primary/5 opacity-0 group-hover:opacity-100 transition-opacity" />
        <CardContent className="p-8 relative">
          <div className="flex flex-col md:flex-row md:items-center justify-between gap-6">
            <div className="space-y-2">
              <h3 className="text-2xl font-bold gold-accent">Ready to execute?</h3>
              <p className="text-muted-foreground text-base">
                All the tools and content you need are ready to deploy
              </p>
            </div>
            <Button size="lg" className="gap-2 whitespace-nowrap premium-button">
              <CheckCircle2 className="h-5 w-5" />
              Mark as Complete
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
