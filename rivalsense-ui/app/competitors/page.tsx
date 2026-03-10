"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { TrendingUp, Activity, MapPin, Tag, Eye, Sparkles, ExternalLink } from "lucide-react";
import { getCompetitors, type Competitor } from "@/lib/storage";
import { getThreatBadgeColor, formatCurrency } from "@/lib/utils";
import { motion } from "framer-motion";

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.05,
    },
  },
};

const item = {
  hidden: { opacity: 0, y: 10 },
  show: { opacity: 1, y: 0 },
};

export default function CompetitorsPage() {
  const router = useRouter();
  const [competitors, setCompetitors] = useState<Competitor[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    setCompetitors(getCompetitors());
    setLoading(false);
  }, []);

  // Empty state when no competitors
  if (!loading && competitors.length === 0) {
    return (
      <div className="space-y-8 pb-8">
        <div className="space-y-1">
          <h1 className="text-4xl font-bold tracking-tight gold-accent">Competitors</h1>
          <p className="text-muted-foreground text-base">
            Monitor your competitive landscape
          </p>
        </div>

        <Card className="border-2 border-dashed border-border/50">
          <CardContent className="flex flex-col items-center justify-center py-24 px-6">
            <div className="flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-primary/20 to-accent/20 border-2 border-primary/30 mb-6 glow-gold">
              <Eye className="h-10 w-10 text-primary" />
            </div>
            <h3 className="text-2xl font-bold mb-3">No Competitors Yet</h3>
            <p className="text-muted-foreground text-center max-w-md mb-6">
              Discover competitors in your market using our AI-powered discovery system.
            </p>
            <Button 
              size="lg" 
              onClick={() => router.push("/discover-competitors")}
              className="gap-2 premium-button"
            >
              <Sparkles className="h-5 w-5" />
              Discover Competitors
            </Button>
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
          <h1 className="text-4xl font-bold tracking-tight gold-accent">Competitors</h1>
          <p className="text-muted-foreground text-base">
            Monitor <span className="font-semibold text-foreground">{competitors.length}</span> competitors in real-time
          </p>
        </div>
        <Button onClick={() => router.push("/discover-competitors")} className="gap-2 premium-button shadow-lg">
          <TrendingUp className="h-4 w-4" />
          Discover More
        </Button>
      </div>

      {/* Competitor Cards */}
      <motion.div
        variants={container}
        initial="hidden"
        animate="show"
        className="grid gap-6 md:grid-cols-2 lg:grid-cols-3"
      >
        {competitors.map((competitor, idx) => (
          <motion.div key={competitor.id || idx} variants={item}>
            <Card className="hover:border-primary/50 transition-all duration-300 hover:shadow-xl hover:shadow-primary/5 h-full group cursor-pointer luxury-card">
              <CardHeader className="pb-4">
                <div className="flex items-start justify-between gap-4">
                  <div className="space-y-2 flex-1">
                    <CardTitle className="text-xl group-hover:text-primary transition-colors gold-accent">{competitor.name}</CardTitle>
                    <div className="flex items-center gap-2 text-sm text-muted-foreground">
                      <Tag className="h-3.5 w-3.5" />
                      <span>{competitor.category}</span>
                    </div>
                    {competitor.location && (
                      <div className="flex items-center gap-2 text-sm text-muted-foreground">
                        <MapPin className="h-3.5 w-3.5" />
                        <span>{competitor.location}</span>
                      </div>
                    )}
                  </div>
                  {competitor.threatLevel && (
                    <div className={`px-3 py-1.5 rounded-lg text-xs font-bold uppercase tracking-wide ${getThreatBadgeColor(competitor.threatScore || 5)} border shadow-sm whitespace-nowrap`}>
                      {competitor.threatLevel}
                    </div>
                  )}
                </div>
              </CardHeader>

              <CardContent className="space-y-4">
                {/* Pricing */}
                {competitor.pricing !== undefined && (
                  <div className="flex items-baseline justify-between">
                    <div>
                      <p className="text-xs text-muted-foreground mb-1">Average Price</p>
                      <p className="text-3xl font-bold tracking-tight gold-accent">{formatCurrency(competitor.pricing)}</p>
                    </div>
                    {competitor.threatScore !== undefined && (
                      <div className="text-right">
                        <p className="text-xs text-muted-foreground mb-1">Threat Score</p>
                        <p className="text-xl font-bold">{competitor.threatScore}<span className="text-sm text-muted-foreground">/10</span></p>
                      </div>
                    )}
                  </div>
                )}

                {/* Promotion */}
                {competitor.promotion ? (
                  <div className="rounded-xl bg-warning/10 p-4 border border-warning/30">
                    <div className="flex items-start gap-2">
                      <Activity className="h-4 w-4 text-warning flex-shrink-0 mt-0.5" />
                      <div className="flex-1 min-w-0">
                        <p className="text-xs text-warning font-bold mb-1">ACTIVE PROMOTION</p>
                        <p className="text-sm text-foreground break-words">
                          {competitor.promotion}
                        </p>
                      </div>
                    </div>
                  </div>
                ) : (
                  <div className="text-center py-3 text-sm text-muted-foreground">
                    No active promotions
                  </div>
                )}

                {/* Links */}
                <div className="flex gap-2 pt-2 border-t border-border/50">
                  {competitor.websiteUrl && (
                    <Button 
                      variant="outline" 
                      size="sm"  
                      className="flex-1 group/btn"
                      asChild
                    >
                      <a href={competitor.websiteUrl} target="_blank" rel="noopener noreferrer">
                        <ExternalLink className="h-3.5 w-3.5 mr-2" />
                        Website
                      </a>
                    </Button>
                  )}
                  {competitor.socialUrl && (
                    <Button 
                      variant="outline" 
                      size="sm" 
                      className="flex-1 group/btn"
                      asChild
                    >
                      <a href={competitor.socialUrl} target="_blank" rel="noopener noreferrer">
                        <ExternalLink className="h-3.5 w-3.5 mr-2" />
                        Social
                      </a>
                    </Button>
                  )}
                </div>

                {competitor.confidenceScore && (
                  <div className="pt-2 border-t border-border/50">
                    <div className="flex justify-between items-center text-xs">
                      <span className="text-muted-foreground">Match Confidence</span>
                      <span className="font-semibold text-primary">{Math.round(competitor.confidenceScore * 100)}%</span>
                    </div>
                    <div className="mt-2 h-1.5 bg-muted rounded-full overflow-hidden">
                      <div 
                        className="h-full bg-gradient-to-r from-primary to-accent rounded-full glow-gold transition-all"
                        style={{ width: `${(competitor.confidenceScore || 0) * 100}%` }}
                      />
                    </div>
                  </div>
                )}
              </CardContent>
            </Card>
          </motion.div>
        ))}
      </motion.div>
    </div>
  );
}
