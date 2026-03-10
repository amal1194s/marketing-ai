"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion, AnimatePresence } from "framer-motion";
import {
  Sparkles,
  Check,
  X,
  Plus,
  Loader2,
  TrendingUp,
  Building2,
  AlertCircle
} from "lucide-react";
import { getBusinessProfile, saveCompetitors } from "@/lib/storage";

interface DiscoveredCompetitor {
  name: string;
  category: string;
  website_url: string | null;
  social_url: string | null;
  reason: string;
  confidence_score: number;
  selected: boolean;
}

export default function DiscoverCompetitorsPage() {
  const router = useRouter();
  const [profile, setProfile] = useState<any>(null);
  const [competitors, setCompetitors] = useState<DiscoveredCompetitor[]>([]);
  const [isDiscovering, setIsDiscovering] = useState(false);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [manualCompetitor, setManualCompetitor] = useState({
    name: "",
    website: "",
    category: ""
  });
  const [showManualAdd, setShowManualAdd] = useState(false);

  useEffect(() => {
    // Load profile from localStorage
    const savedProfile = getBusinessProfile();
    if (!savedProfile) {
      router.push("/onboarding");
      return;
    }
    setProfile(savedProfile);
    
    // Auto-discover competitors
    discoverCompetitors(savedProfile);
  }, []);

  const discoverCompetitors = async (businessProfile: any) => {
    setIsDiscovering(true);
    setError(null);

    try {
      console.log("Sending discovery request for:", businessProfile);
      const response = await fetch("http://localhost:8000/discover-competitors", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          business_name: businessProfile.name,
          business_category: businessProfile.category,
          city: businessProfile.city,
          target_audience: businessProfile.targetAudience || "",
          average_price: businessProfile.averagePrice || "medium",
          max_results: 10
        })
      });

      console.log("Response status:", response.status);

      if (!response.ok) {
        const errorText = await response.text();
        console.error("API error:", errorText);
        throw new Error(`Failed to discover competitors: ${response.status} ${errorText}`);
      }

      const data = await response.json();
      console.log("Discovery response:", data);
      
      const discovered = data.competitors.map((comp: any) => ({
        ...comp,
        selected: comp.confidence_score >= 0.7 // Auto-select high confidence
      }));

      setCompetitors(discovered);
    } catch (err) {
      const errorMessage = err instanceof Error ? err.message : "Discovery failed - please check console";
      setError(errorMessage);
      console.error("Discovery error:", err);
    } finally {
      setIsDiscovering(false);
    }
  };

  const toggleCompetitor = (index: number) => {
    setCompetitors(competitors.map((comp, i) => 
      i === index ? { ...comp, selected: !comp.selected } : comp
    ));
  };

  const removeCompetitor = (index: number) => {
    setCompetitors(competitors.filter((_, i) => i !== index));
  };

  const addManualCompetitor = () => {
    if (!manualCompetitor.name || !manualCompetitor.website) {
      return;
    }

    const newCompetitor: DiscoveredCompetitor = {
      name: manualCompetitor.name,
      category: manualCompetitor.category || "Competitor",
      website_url: manualCompetitor.website,
      social_url: null,
      reason: "Manually added by user",
      confidence_score: 1.0,
      selected: true
    };

    setCompetitors([...competitors, newCompetitor]);
    setManualCompetitor({ name: "", website: "", category: "" });
    setShowManualAdd(false);
  };

  const handleContinue = async () => {
    const selected = competitors.filter(c => c.selected);
    
    if (selected.length === 0) {
      setError("Please select at least one competitor");
      return;
    }

    setIsSubmitting(true);
    setError(null);

    try {
      // Format for storage
      const competitorData = selected.map(c => ({
        name: c.name,
        websiteUrl: c.website_url || "",
        socialUrl: c.social_url || "",
        category: c.category
      }));

      // Save to localStorage
      await saveCompetitors(competitorData);
      
      // Redirect to dashboard
      router.push("/dashboard");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to save competitors");
      setIsSubmitting(false);
    }
  };

  const selectedCount = competitors.filter(c => c.selected).length;

  if (!profile) {
    return null;
  }

  return (
    <div className="min-h-screen bg-background py-12 px-6">
      <div className="max-w-6xl mx-auto">
        {/* Header */}
        <div className="text-center mb-12">
          <div className="inline-flex h-20 w-20 items-center justify-center rounded-2xl bg-gradient-to-br from-primary via-accent to-primary shadow-lg glow-gold-strong mb-6">
            <TrendingUp className="h-10 w-10 text-background" />
          </div>
          <h1 className="text-5xl font-bold mb-4 bg-gradient-to-r from-primary via-accent to-primary bg-clip-text text-transparent">
            Discover Your Competitors
          </h1>
          <p className="text-muted-foreground text-lg max-w-2xl mx-auto">
            AI-powered competitor discovery based on your business profile
          </p>
        </div>

        {/* Business Summary Card */}
        <Card className="luxury-card mb-8 border-primary/20">
          <CardHeader>
            <div className="flex items-start gap-4">
              <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-primary/20 to-accent/20 border border-primary/30">
                <Building2 className="h-6 w-6 text-primary" />
              </div>
              <div className="flex-1">
                <CardTitle className="text-2xl mb-1">{profile.name}</CardTitle>
                <CardDescription className="text-base flex gap-2 flex-wrap">
                  <span className="gold-accent">{profile.category}</span>
                  <span>•</span>
                  <span>{profile.city}</span>
                  <span>•</span>
                  <span>{profile.averagePrice}</span>
                </CardDescription>
              </div>
            </div>
          </CardHeader>
        </Card>

        {/* Discovery Status */}
        {isDiscovering && (
          <Card className="luxury-card border-accent/30 mb-8">
            <CardContent className="py-12 text-center">
              <Loader2 className="h-12 w-12 text-primary animate-spin mx-auto mb-4" />
              <h3 className="text-xl font-semibold mb-2">Discovering Competitors...</h3>
              <p className="text-muted-foreground">
                Analyzing market data for {profile.category} in {profile.city}
              </p>
            </CardContent>
          </Card>
        )}

        {/* Error Display */}
        {error && (
          <Card className="border-destructive/30 bg-destructive/5 mb-8">
            <CardContent className="p-6 flex items-start gap-4">
              <AlertCircle className="h-6 w-6 text-destructive flex-shrink-0 mt-0.5" />
              <div>
                <h4 className="font-bold text-destructive mb-1">Error</h4>
                <p className="text-sm text-muted-foreground">{error}</p>
              </div>
            </CardContent>
          </Card>
        )}

        {/* Competitor Selection */}
        {!isDiscovering && competitors.length > 0 && (
          <>
            <div className="flex items-center justify-between mb-6">
              <div>
                <h2 className="text-2xl font-bold">Discovered {competitors.length} Competitors</h2>
                <p className="text-muted-foreground">
                  {selectedCount} selected • Click to select/deselect
                </p>
              </div>
              <Button
                variant="outline"
                onClick={() => setShowManualAdd(!showManualAdd)}
                className="gap-2 border-primary/30 hover:bg-primary/10"
              >
                <Plus className="h-4 w-4" />
                Add Manually
              </Button>
            </div>

            {/* Manual Add Form */}
            {showManualAdd && (
              <Card className="luxury-card border-primary/30 mb-6">
                <CardContent className="p-6 space-y-4">
                  <h3 className="font-semibold text-lg">Add Competitor Manually</h3>
                  <div className="grid gap-4 sm:grid-cols-3">
                    <input
                      type="text"
                      placeholder="Competitor name"
                      value={manualCompetitor.name}
                      onChange={(e) => setManualCompetitor({ ...manualCompetitor, name: e.target.value })}
                      className="px-4 py-2 bg-input border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                    />
                    <input
                      type="url"
                      placeholder="Website URL"
                      value={manualCompetitor.website}
                      onChange={(e) => setManualCompetitor({ ...manualCompetitor, website: e.target.value })}
                      className="px-4 py-2 bg-input border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                    />
                    <input
                      type="text"
                      placeholder="Category (optional)"
                      value={manualCompetitor.category}
                      onChange={(e) => setManualCompetitor({ ...manualCompetitor, category: e.target.value })}
                      className="px-4 py-2 bg-input border border-border rounded-lg focus:outline-none focus:ring-2 focus:ring-primary"
                    />
                  </div>
                  <div className="flex gap-3">
                    <Button onClick={addManualCompetitor} className="gap-2">
                      <Plus className="h-4 w-4" />
                      Add Competitor
                    </Button>
                    <Button variant="outline" onClick={() => setShowManualAdd(false)}>
                      Cancel
                    </Button>
                  </div>
                </CardContent>
              </Card>
            )}

            {/* Competitor Cards Grid */}
            <div className="grid gap-4 sm:grid-cols-2 mb-8">
              <AnimatePresence>
                {competitors.map((comp, index) => (
                  <motion.div
                    key={index}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, scale: 0.9 }}
                    transition={{ duration: 0.3, delay: index * 0.05 }}
                  >
                    <Card
                      className={`luxury-card cursor-pointer transition-all duration-300 ${
                        comp.selected
                          ? "border-primary/50 bg-primary/5 glow-gold"
                          : "border-border/30 hover:border-primary/30"
                      }`}
                      onClick={() => toggleCompetitor(index)}
                    >
                      <CardContent className="p-6">
                        <div className="flex items-start justify-between mb-4">
                          <div className="flex-1">
                            <div className="flex items-center gap-3 mb-2">
                              <h3 className="font-bold text-lg">{comp.name}</h3>
                              {comp.selected && (
                                <Check className="h-5 w-5 text-primary" />
                              )}
                            </div>
                            <p className="text-sm text-muted-foreground mb-1">{comp.category}</p>
                            <div className="flex items-center gap-2 mb-3">
                              <div className="h-2 w-20 bg-muted rounded-full overflow-hidden">
                                <div
                                  className="h-full bg-gradient-to-r from-primary to-accent"
                                  style={{ width: `${comp.confidence_score * 100}%` }}
                                />
                              </div>
                              <span className="text-xs font-medium gold-accent">
                                {Math.round(comp.confidence_score * 100)}% match
                              </span>
                            </div>
                          </div>
                          <Button
                            variant="ghost"
                            size="sm"
                            onClick={(e) => {
                              e.stopPropagation();
                              removeCompetitor(index);
                            }}
                            className="text-muted-foreground hover:text-destructive hover:bg-destructive/10"
                          >
                            <X className="h-4 w-4" />
                          </Button>
                        </div>
                        
                        <div className="space-y-2 text-sm">
                          {comp.website_url && (
                            <a
                              href={comp.website_url}
                              target="_blank"
                              rel="noopener noreferrer"
                              onClick={(e) => e.stopPropagation()}
                              className="block text-primary hover:underline truncate"
                            >
                              {comp.website_url}
                            </a>
                          )}
                          <p className="text-muted-foreground text-xs leading-relaxed">
                            {comp.reason}
                          </p>
                        </div>
                      </CardContent>
                    </Card>
                  </motion.div>
                ))}
              </AnimatePresence>
            </div>

            {/* Action Buttons */}
            <div className="flex items-center justify-between">
              <Button
                variant="outline"
                onClick={() => router.push("/onboarding")}
                disabled={isSubmitting}
                className="border-border/50"
              >
                Back
              </Button>
              <Button
                onClick={handleContinue}
                disabled={selectedCount === 0 || isSubmitting}
                className="gap-2 premium-button"
              >
                {isSubmitting ? (
                  <>
                    <Loader2 className="h-4 w-4 animate-spin" />
                    Saving...
                  </>
                ) : (
                  <>
                    <Sparkles className="h-4 w-4" />
                    Continue with {selectedCount} {selectedCount === 1 ? "Competitor" : "Competitors"}
                  </>
                )}
              </Button>
            </div>
          </>
        )}

        {/* No Competitors Found */}
        {!isDiscovering && competitors.length === 0 && (
          <Card className="luxury-card border-dashed border-border/50">
            <CardContent className="py-24 text-center">
              <TrendingUp className="h-16 w-16 text-muted-foreground mx-auto mb-6 opacity-50" />
              <h3 className="text-2xl font-bold mb-3">No Competitors Found</h3>
              <p className="text-muted-foreground mb-6 max-w-md mx-auto">
                We couldn't find competitors in our database. You can add them manually.
              </p>
              <Button
                onClick={() => setShowManualAdd(true)}
                className="gap-2 premium-button"
              >
                <Plus className="h-4 w-4" />
                Add Competitors Manually
              </Button>
            </CardContent>
          </Card>
        )}
      </div>
    </div>
  );
}
