"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { motion, AnimatePresence } from "framer-motion";
import { 
  Building2, 
  Users, 
  DollarSign, 
  Target, 
  Sparkles,
  ArrowRight,
  ArrowLeft,
  Check,
  Loader2
} from "lucide-react";
import { saveProfile } from "@/lib/api";

interface BusinessProfile {
  name: string;
  category: string;
  city: string;
  targetAudience: string;
  averagePrice: string;
  currentOffers: string;
  usp: string;
}

export default function OnboardingPage() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [profile, setProfile] = useState<BusinessProfile>({
    name: "",
    category: "",
    city: "",
    targetAudience: "",
    averagePrice: "",
    currentOffers: "",
    usp: "",
  });

  const totalSteps = 2;

  const handleNext = () => {
    if (step < totalSteps) setStep(step + 1);
  };

  const handleBack = () => {
    if (step > 1) setStep(step - 1);
  };

  const handleProfileChange = (field: keyof BusinessProfile, value: string) => {
    setProfile({ ...profile, [field]: value });
  };

  const handleFinish = async () => {
    if (isSubmitting) return;
    
    setIsSubmitting(true);
    setError(null);

    try {
      // Save to localStorage first (offline-first approach)
      localStorage.setItem("businessProfile", JSON.stringify(profile));
      
      // Try to save to backend (don't block on failure)
      try {
        await saveProfile(profile);
        console.log("✓ Profile saved to backend");
      } catch (apiError) {
        console.warn("Backend save failed (using localStorage only):", apiError);
        // Continue anyway - localStorage is sufficient
      }
      
      // Redirect to competitor discovery
      router.push("/discover-competitors");
    } catch (err) {
      setError(err instanceof Error ? err.message : "Failed to save profile");
      setIsSubmitting(false);
    }
  };

  const isStep1Valid = profile.name && profile.category && profile.city;

  return (
    <div className="min-h-screen bg-background flex items-center justify-center p-6">
      <div className="w-full max-w-4xl">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="inline-flex h-16 w-16 items-center justify-center rounded-2xl bg-gradient-to-br from-indigo-500 to-purple-600 shadow-lg shadow-indigo-500/25 mb-4">
            <Sparkles className="h-8 w-8 text-white" />
          </div>
          <h1 className="text-4xl font-bold mb-2">Welcome to RivalSense AI</h1>
          <p className="text-muted-foreground text-lg">
            Let's set up your market intelligence profile
          </p>
        </div>

        {/* Progress Steps */}
        <div className="flex items-center justify-center mb-8">
          {[1, 2].map((s) => (
            <div key={s} className="flex items-center">
              <div
                className={`flex h-10 w-10 items-center justify-center rounded-full border-2 transition-all duration-300 ${
                  s <= step
                    ? "border-primary bg-primary text-primary-foreground"
                    : "border-border bg-background text-muted-foreground"
                }`}
              >
                {s < step ? <Check className="h-5 w-5" /> : s}
              </div>
              {s < 2 && (
                <div
                  className={`h-0.5 w-16 mx-2 transition-all duration-300 ${
                    s < step ? "bg-primary" : "bg-border"
                  }`}
                />
              )}
            </div>
          ))}
        </div>

        {/* Form Content */}
        <AnimatePresence mode="wait">
          <motion.div
            key={step}
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            exit={{ opacity: 0, x: -20 }}
            transition={{ duration: 0.3 }}
          >
            <Card className="overflow-hidden border-primary/20">
              <CardHeader className="border-b border-border/40 bg-card/50">
                <CardTitle className="text-2xl">
                  {step === 1 && "Business Details"}
                  {step === 2 && "Review & Discover Competitors"}
                </CardTitle>
                <CardDescription className="text-base">
                  {step === 1 && "Tell us about your business"}
                  {step === 2 && "Review your information and discover competitors"}
                </CardDescription>
              </CardHeader>

              <CardContent className="p-8">
                {/* Step 1: Business Details */}
                {step === 1 && (
                  <div className="space-y-6">
                    <div>
                      <label className="text-sm font-medium mb-2 block">Business Name *</label>
                      <input
                        type="text"
                        value={profile.name}
                        onChange={(e) => handleProfileChange("name", e.target.value)}
                        placeholder="e.g., Acme Coffee Shop"
                        className="w-full h-11 px-4 rounded-lg border-2 border-border bg-background focus:border-primary focus:outline-none transition-colors"
                      />
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div>
                        <label className="text-sm font-medium mb-2 block">Category / Niche *</label>
                        <input
                          type="text"
                          value={profile.category}
                          onChange={(e) => handleProfileChange("category", e.target.value)}
                          placeholder="e.g., Coffee Shop, Bakery, Gym"
                          className="w-full h-11 px-4 rounded-lg border-2 border-border bg-background focus:border-primary focus:outline-none transition-colors"
                        />
                      </div>

                      <div>
                        <label className="text-sm font-medium mb-2 block">City / Location *</label>
                        <input
                          type="text"
                          value={profile.city}
                          onChange={(e) => handleProfileChange("city", e.target.value)}
                          placeholder="e.g., San Francisco, CA"
                          className="w-full h-11 px-4 rounded-lg border-2 border-border bg-background focus:border-primary focus:outline-none transition-colors"
                        />
                      </div>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                      <div>
                        <label className="text-sm font-medium mb-2 block">Target Audience</label>
                        <input
                          type="text"
                          value={profile.targetAudience}
                          onChange={(e) => handleProfileChange("targetAudience", e.target.value)}
                          placeholder="e.g., Young professionals, Families"
                          className="w-full h-11 px-4 rounded-lg border-2 border-border bg-background focus:border-primary focus:outline-none transition-colors"
                        />
                      </div>

                      <div>
                        <label className="text-sm font-medium mb-2 block">Average Price</label>
                        <input
                          type="text"
                          value={profile.averagePrice}
                          onChange={(e) => handleProfileChange("averagePrice", e.target.value)}
                          placeholder="e.g., $15-25"
                          className="w-full h-11 px-4 rounded-lg border-2 border-border bg-background focus:border-primary focus:outline-none transition-colors"
                        />
                      </div>
                    </div>

                    <div>
                      <label className="text-sm font-medium mb-2 block">Current Offers</label>
                      <textarea
                        value={profile.currentOffers}
                        onChange={(e) => handleProfileChange("currentOffers", e.target.value)}
                        placeholder="e.g., 20% off first purchase, Happy hour 3-5pm"
                        rows={3}
                        className="w-full px-4 py-3 rounded-lg border-2 border-border bg-background focus:border-primary focus:outline-none transition-colors resize-none"
                      />
                    </div>

                    <div>
                      <label className="text-sm font-medium mb-2 block">Unique Selling Proposition (USP)</label>
                      <textarea
                        value={profile.usp}
                        onChange={(e) => handleProfileChange("usp", e.target.value)}
                        placeholder="What makes your business special?"
                        rows={3}
                        className="w-full px-4 py-3 rounded-lg border-2 border-border bg-background focus:border-primary focus:outline-none transition-colors resize-none"
                      />
                    </div>
                  </div>
                )}

                {/* Step 2: Review */}
                {step === 2 && (
                  <div className="space-y-6">
                    <Card className="p-6 bg-gradient-to-br from-indigo-500/10 to-purple-500/10 border-primary/20">
                      <h3 className="font-bold text-xl mb-4">Your Business</h3>
                      <div className="grid grid-cols-2 gap-4 text-sm">
                        <div>
                          <span className="text-muted-foreground">Name:</span>
                          <p className="font-medium">{profile.name || "Not provided"}</p>
                        </div>
                        <div>
                          <span className="text-muted-foreground">Category:</span>
                          <p className="font-medium">{profile.category || "Not provided"}</p>
                        </div>
                        <div>
                          <span className="text-muted-foreground">City:</span>
                          <p className="font-medium">{profile.city || "Not provided"}</p>
                        </div>
                        <div>
                          <span className="text-muted-foreground">Target Audience:</span>
                          <p className="font-medium">{profile.targetAudience || "Not provided"}</p>
                        </div>
                        <div>
                          <span className="text-muted-foreground">Average Price:</span>
                          <p className="font-medium">{profile.averagePrice || "Not provided"}</p>
                        </div>
                        <div>
                          <span className="text-muted-foreground">Current Offers:</span>
                          <p className="font-medium">{profile.currentOffers || "None"}</p>
                        </div>
                      </div>
                      {profile.usp && (
                        <div className="mt-4 pt-4 border-t border-border/40">
                          <span className="text-muted-foreground text-sm">USP:</span>
                          <p className="font-medium mt-1">{profile.usp}</p>
                        </div>
                      )}
                    </Card>

                    <div className="bg-emerald-500/10 border border-emerald-500/20 rounded-xl p-6 text-center">
                      <Sparkles className="h-12 w-12 text-emerald-500 mx-auto mb-3" />
                      <h3 className="font-bold text-xl mb-2">Ready to Discover Competitors!</h3>
                      <p className="text-muted-foreground">
                        Click continue to use AI-powered competitor discovery
                      </p>
                    </div>

                    {/* Error Display */}
                    {error && (
                      <div className="bg-rose-500/10 border border-rose-500/20 rounded-xl p-4">
                        <p className="text-sm text-rose-500 font-medium">{error}</p>
                      </div>
                    )}
                  </div>
                )}
              </CardContent>
            </Card>
          </motion.div>
        </AnimatePresence>

        {/* Navigation Buttons */}
        <div className="flex items-center justify-between mt-8">
          {step > 1 ? (
            <Button 
              variant="outline" 
              onClick={handleBack} 
              className="gap-2"
              disabled={isSubmitting}
            >
              <ArrowLeft className="h-4 w-4" />
              Back
            </Button>
          ) : (
            <div />
          )}

          {step < totalSteps ? (
            <Button
              onClick={handleNext}
              className="gap-2"
              disabled={step === 1 ? !isStep1Valid : false}
            >
              Next
              <ArrowRight className="h-4 w-4" />
            </Button>
          ) : (
            <Button 
              onClick={handleFinish} 
              className="gap-2 bg-emerald-600 hover:bg-emerald-700"
              disabled={isSubmitting}
            >
              {isSubmitting ? (
                <>
                  <Loader2 className="h-4 w-4 animate-spin" />
                  Saving...
                </>
              ) : (
                <>
                  <Sparkles className="h-4 w-4" />
                  Discover Competitors
                </>
              )}
            </Button>
          )}
        </div>
      </div>
    </div>
  );
}
