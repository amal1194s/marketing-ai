"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { Download, AlertTriangle, TrendingUp, DollarSign, Target, Sparkles } from "lucide-react";
import { getAnalysis, getCompetitors } from "@/lib/storage";
import { getThreatColor, getThreatBadgeColor, formatPercent } from "@/lib/utils";
import { motion } from "framer-motion";
import type { AnalysisResult, Competitor } from "@/lib/storage";

export default function AnalysisPage() {
  const router = useRouter();
  const [analysis, setAnalysis] = useState<AnalysisResult | null>(null);
  const [competitors, setCompetitors] = useState<Competitor[]>([]);

  useEffect(() => {
    const data = getAnalysis();
    const comps = getCompetitors();
    setAnalysis(data);
    setCompetitors(comps);
  }, []);

  // Show empty state if no analysis data
  if (!analysis) {
    return (
      <div className="space-y-8 pb-8">
        <div className="space-y-1">
          <h1 className="text-4xl font-bold tracking-tight">Market Analysis</h1>
          <p className="text-muted-foreground text-base">
            AI-powered competitive intelligence report
          </p>
        </div>
        
        <Card className="border-primary/30 bg-gradient-to-br from-primary/5 via-accent/5 to-primary/10 luxury-card glow-gold">
          <CardContent className="p-12 text-center">
            <div className="flex flex-col items-center gap-4">
              <div className="flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-primary/20 to-accent/20 border-2 border-primary/40">
                <Sparkles className="h-10 w-10 text-primary" />
              </div>
              <div>
                <h3 className="text-xl font-bold mb-2 gold-accent">No Analysis Data Available</h3>
                <p className="text-muted-foreground mb-4">
                  Run the War Room to generate AI-powered market analysis
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
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4">
        <div className="space-y-1">
          <h1 className="text-4xl font-bold tracking-tight">Market Analysis</h1>
          <p className="text-muted-foreground text-base">
            AI-powered competitive intelligence report
          </p>
        </div>
        <Button variant="outline" className="gap-2 shadow-md">
          <Download className="h-4 w-4" />
          Export Report
        </Button>
      </div>

      {/* Threat Overview */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
        className="grid gap-6 md:grid-cols-3"
      >
        <Card className="md:col-span-2 hover:shadow-lg transition-all duration-300">
          <CardHeader className="pb-5">
            <div className="flex items-start justify-between gap-4">
              <div className="space-y-2">
                <CardTitle className="text-2xl">Overall Threat Assessment</CardTitle>
                <CardDescription className="text-base">Current competitive landscape</CardDescription>
              </div>
              <div className={`flex h-20 w-20 items-center justify-center rounded-2xl ${getThreatBadgeColor(analysis.threatScore)} border-2 shadow-lg`}>
                <span className="text-3xl font-bold">{analysis.threatScore}</span>
              </div>
            </div>
          </CardHeader>
          <CardContent className="space-y-4">
            <p className="text-foreground leading-relaxed text-base">
              {analysis.summary}
            </p>
            <div className="flex items-center gap-3">
              <div className={`px-4 py-2 rounded-lg text-sm font-bold uppercase tracking-wide ${getThreatBadgeColor(analysis.threatScore)} border shadow-sm`}>
                {analysis.impactLevel} IMPACT
              </div>
            </div>
          </CardContent>
        </Card>

        <Card className="hover:shadow-lg transition-all duration-300">
          <CardHeader className="pb-4">
            <CardTitle className="flex items-center gap-2 text-xl">
              <DollarSign className="h-5 w-5 text-amber-500" />
              Pricing Gap
            </CardTitle>
          </CardHeader>
          <CardContent className="space-y-3">
            <div className="text-4xl font-bold tracking-tight">
              {formatPercent(analysis.priceDifferencePercent || 0)}
            </div>
            <p className="text-sm text-muted-foreground leading-relaxed">
              {analysis.pricingGap}
            </p>
          </CardContent>
        </Card>
      </motion.div>

      {/* Market Risk */}
      <Card className="overflow-hidden hover:shadow-lg transition-all duration-300">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <CardTitle className="flex items-center gap-2 text-xl">
            <AlertTriangle className="h-5 w-5 text-amber-500" />
            Market Risk Analysis
          </CardTitle>
          <p className="text-sm text-muted-foreground mt-2">Competitive threat breakdown</p>
        </CardHeader>
        <CardContent className="pt-6">
          <p className="text-foreground mb-6 leading-relaxed">{analysis.marketRisk}</p>
          <div className="grid gap-4 md:grid-cols-3">
            {analysis.competitorBreakdown.map((comp, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.1 }}
                className="p-5 rounded-xl bg-accent/30 hover:bg-accent/60 transition-all duration-200 border border-border/30 hover:border-border/60 cursor-pointer group"
              >
                <div className="flex items-center justify-between mb-3">
                  <p className="font-bold text-base">{comp.name}</p>
                  <div className={`px-2.5 py-1 rounded-lg text-xs font-bold uppercase tracking-wide shadow-sm ${
                    comp.threat?.toLowerCase() === "high" ? "bg-rose-500/10 text-rose-500 border border-rose-500/30" :
                    comp.threat?.toLowerCase() === "medium" ? "bg-amber-500/10 text-amber-500 border border-amber-500/30" :
                    "bg-emerald-500/10 text-emerald-500 border border-emerald-500/30"
                  }`}>
                    {comp.threat || "Unknown"}
                  </div>
                </div>
                <p className="text-sm text-muted-foreground leading-relaxed">{comp.reason}</p>
              </motion.div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Key Insights */}
      <Card className="overflow-hidden hover:shadow-lg transition-all duration-300">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <CardTitle className="flex items-center gap-2 text-xl">
            <Target className="h-5 w-5 text-indigo-500" />
            Key Insights
          </CardTitle>
          <CardDescription className="text-base mt-2">
            AI-generated competitive intelligence
          </CardDescription>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="space-y-3">
            {analysis.keyInsights.map((insight, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, x: -20 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ delay: index * 0.1 }}
                className="flex items-start gap-4 p-5 rounded-xl bg-accent/30 hover:bg-accent/60 transition-all duration-200 border border-transparent hover:border-border/50 cursor-pointer group"
              >
                <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-500/10 text-indigo-500 border border-indigo-500/20 shrink-0 font-bold text-sm group-hover:scale-105 group-hover:bg-indigo-500/20 transition-all">
                  {index + 1}
                </div>
                <p className="text-sm text-foreground leading-relaxed flex-1 pt-1.5">
                  {insight}
                </p>
              </motion.div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Competitor Comparison Table */}
      <Card className="overflow-hidden hover:shadow-lg transition-all duration-300">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <CardTitle className="text-xl">Competitor Comparison</CardTitle>
          <CardDescription className="text-base mt-2">Head-to-head analysis</CardDescription>
        </CardHeader>
        <CardContent className="p-0">
          <div className="overflow-x-auto">
            <table className="w-full">
              <thead>
                <tr className="border-b border-border/50 bg-accent/30">
                  <th className="text-left py-4 px-6 text-xs font-bold text-muted-foreground uppercase tracking-wider">
                    Competitor
                  </th>
                  <th className="text-left py-4 px-6 text-xs font-bold text-muted-foreground uppercase tracking-wider">
                    Pricing
                  </th>
                  <th className="text-left py-4 px-6 text-xs font-bold text-muted-foreground uppercase tracking-wider">
                    Promotion
                  </th>
                  <th className="text-left py-4 px-6 text-xs font-bold text-muted-foreground uppercase tracking-wider">
                    Threat Level
                  </th>
                  <th className="text-right py-4 px-6 text-xs font-bold text-muted-foreground uppercase tracking-wider">
                    Score
                  </th>
                </tr>
              </thead>
              <tbody>
                {competitors.map((comp) => (
                  <tr key={comp.id} className="border-b border-border/30 hover:bg-accent/40 transition-all group">
                    <td className="py-5 px-6">
                      <p className="font-bold text-sm">{comp.name}</p>
                      <p className="text-xs text-muted-foreground mt-0.5">{comp.location}</p>
                    </td>
                    <td className="py-5 px-6">
                      <p className="font-bold text-sm">${comp.pricing}</p>
                    </td>
                    <td className="py-5 px-6">
                      {comp.promotion ? (
                        <div className="px-2 py-1 rounded-lg bg-amber-500/10 text-amber-500 text-xs font-semibold inline-block">
                          Active
                        </div>
                      ) : (
                        <span className="text-muted-foreground text-sm">None</span>
                      )}
                    </td>
                    <td className="py-4 px-4">
                      <div className={`px-2 py-1 rounded-lg text-xs font-semibold inline-block ${getThreatBadgeColor(comp.threatScore || 0)}`}>
                        {(comp.threatLevel || 'unknown').toUpperCase()}
                      </div>
                    </td>
                    <td className="py-4 px-4 text-right">
                      <p className={`text-lg font-bold ${getThreatColor(comp.threatScore || 0)}`}>
                        {comp.threatScore || 0}
                      </p>
                    </td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
