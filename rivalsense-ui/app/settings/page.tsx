"use client";

import { useState, useEffect } from "react";
import { useRouter } from "next/navigation";
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from "@/components/ui/card";
import { Button } from "@/components/ui/button";
import { User, Bell, Shield, CreditCard, Zap, Save, Check, AlertTriangle } from "lucide-react";
import { getBusinessProfile, saveBusinessProfile, clearCompetitors, clearAnalysis, clearStrategy, clearActivities } from "@/lib/storage";
import { saveProfile } from "@/lib/api";

export default function SettingsPage() {
  const router = useRouter();
  const [profile, setProfile] = useState({
    name: "",
    category: "",
    city: "",
    targetAudience: "",
    averagePrice: "",
    currentOffers: "",
    usp: ""
  });
  const [originalProfile, setOriginalProfile] = useState<any>(null);
  const [userName, setUserName] = useState("");
  const [isSaving, setIsSaving] = useState(false);
  const [saveSuccess, setSaveSuccess] = useState(false);
  const [showWarning, setShowWarning] = useState(false);

  useEffect(() => {
    const savedProfile = getBusinessProfile();
    if (savedProfile) {
      setProfile(savedProfile);
      setOriginalProfile(savedProfile);
    }
    
    // Load user name from localStorage
    const savedUserName = localStorage.getItem("userName");
    if (savedUserName) {
      setUserName(savedUserName);
    }
  }, []);

  // Check if key fields changed that would invalidate competitors
  const hasSignificantChanges = () => {
    if (!originalProfile) return false;
    
    return (
      originalProfile.category !== profile.category ||
      originalProfile.city !== profile.city ||
      originalProfile.averagePrice !== profile.averagePrice
    );
  };

  const handleSave = async () => {
    setIsSaving(true);
    setSaveSuccess(false);
    setShowWarning(false);
    
    try {
      // Check if significant changes require clearing competitor data
      const needsClear = hasSignificantChanges();
      
      if (needsClear) {
        // Clear competitors and analysis since business profile changed significantly
        clearCompetitors();
        clearAnalysis();
        clearStrategy();
        clearActivities();
      }
      
      // Save to localStorage
      saveBusinessProfile(profile);
      localStorage.setItem("userName", userName);
      
      // Try to save to backend
      try {
        await saveProfile(profile);
      } catch (err) {
        console.warn("Backend save failed, using localStorage only");
      }
      
      // Update original profile after successful save
      setOriginalProfile(profile);
      
      setSaveSuccess(true);
      
      if (needsClear) {
        setShowWarning(true);
        // Redirect to competitor discovery after a moment
        setTimeout(() => {
          router.push("/discover-competitors");
        }, 2000);
      } else {
        setTimeout(() => setSaveSuccess(false), 3000);
      }
    } catch (err) {
      console.error("Failed to save profile:", err);
    } finally {
      setIsSaving(false);
    }
  };

  return (
    <div className="space-y-8 max-w-5xl pb-8">
      {/* Header */}
      <div className="space-y-1">
        <h1 className="text-4xl font-bold tracking-tight">Settings</h1>
        <p className="text-muted-foreground text-base">
          Manage your account and preferences
        </p>
      </div>

      {/* Warning for significant changes */}
      {hasSignificantChanges() && !showWarning && (
        <Card className="border-amber-500/30 bg-amber-500/5 luxury-card">
          <CardContent className="p-6">
            <div className="flex items-start gap-4">
              <AlertTriangle className="h-6 w-6 text-amber-500 flex-shrink-0 mt-0.5" />
              <div>
                <h4 className="font-bold text-amber-500 mb-1">Important: Profile Changes Detected</h4>
                <p className="text-sm text-muted-foreground">
                  You've changed your business category, location, or pricing. Saving these changes will clear your current competitors and analysis data, as they're no longer relevant. You'll be redirected to discover new competitors that match your updated business profile.
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Success message after clearing data */}
      {showWarning && (
        <Card className="border-primary/30 bg-primary/5 luxury-card">
          <CardContent className="p-6">
            <div className="flex items-start gap-4">
              <Check className="h-6 w-6 text-primary flex-shrink-0 mt-0.5" />
              <div>
                <h4 className="font-bold text-primary mb-1">Profile Updated Successfully!</h4>
                <p className="text-sm text-muted-foreground">
                  Your competitors and analysis data have been cleared. Redirecting you to discover new competitors that match your updated business profile...
                </p>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* User Profile Section */}
      <Card className="luxury-card border-primary/20">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <CardTitle className="flex items-center gap-2 text-xl">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-gradient-to-br from-primary/20 to-accent/20 border border-primary/30">
              <User className="h-5 w-5 text-primary" />
            </div>
            Your Profile
          </CardTitle>
          <CardDescription className="text-base mt-2">Personal information displayed in the app</CardDescription>
        </CardHeader>
        <CardContent className="pt-6 space-y-6">
          <div className="flex items-center gap-6">
            <div className="flex h-20 w-20 items-center justify-center rounded-full bg-gradient-to-br from-primary to-accent text-2xl font-bold text-background shadow-lg glow-gold">
              {userName ? userName.split(' ').map(n => n[0]).join('').toUpperCase().slice(0, 2) : 'TP'}
            </div>
            <div className="flex-1">
              <label className="text-sm font-bold text-foreground uppercase tracking-wide">
                Your Name
              </label>
              <input
                type="text"
                value={userName}
                onChange={(e) => setUserName(e.target.value)}
                placeholder="e.g., Tom Parker"
                className="w-full h-11 rounded-xl border-2 border-border/50 bg-card px-4 text-sm text-foreground focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all mt-2"
              />
              <p className="text-xs text-muted-foreground mt-2">This name will appear in the top bar and throughout the app</p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Business Profile */}
      <Card className="luxury-card border-primary/20">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <CardTitle className="flex items-center gap-2 text-xl">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-gradient-to-br from-primary/20 to-accent/20 border border-primary/30">
              <User className="h-5 w-5 text-primary" />
            </div>
            Business Profile
          </CardTitle>
          <CardDescription className="text-base mt-2">Your business information and settings</CardDescription>
        </CardHeader>
        <CardContent className="pt-6 space-y-6">
          <div className="space-y-2">
            <label className="text-sm font-bold text-foreground uppercase tracking-wide">
              Business Name
            </label>
            <input
              type="text"
              value={profile.name}
              onChange={(e) => setProfile({ ...profile, name: e.target.value })}
              className="w-full h-11 rounded-xl border-2 border-border/50 bg-card px-4 text-sm text-foreground focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all"
            />
          </div>
          <div className="grid gap-6 md:grid-cols-2">
            <div className="space-y-2">
              <label className="text-sm font-bold text-foreground uppercase tracking-wide">
                Category / Business Type
              </label>
              <input
                type="text"
                value={profile.category}
                onChange={(e) => setProfile({ ...profile, category: e.target.value })}
                className="w-full h-11 rounded-xl border-2 border-border/50 bg-card px-4 text-sm text-foreground focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all"
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-bold text-foreground uppercase tracking-wide">
                City / Location
              </label>
              <input
                type="text"
                value={profile.city}
                onChange={(e) => setProfile({ ...profile, city: e.target.value })}
                className="w-full h-11 rounded-xl border-2 border-border/50 bg-card px-4 text-sm text-foreground focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all"
              />
            </div>
          </div>
          <div className="grid gap-6 md:grid-cols-2">
            <div className="space-y-2">
              <label className="text-sm font-bold text-foreground uppercase tracking-wide">
                Target Audience
              </label>
              <input
                type="text"
                value={profile.targetAudience}
                onChange={(e) => setProfile({ ...profile, targetAudience: e.target.value })}
                className="w-full h-11 rounded-xl border-2 border-border/50 bg-card px-4 text-sm text-foreground focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all"
              />
            </div>
            <div className="space-y-2">
              <label className="text-sm font-bold text-foreground uppercase tracking-wide">
                Average Price
              </label>
              <input
                type="text"
                value={profile.averagePrice}
                onChange={(e) => setProfile({ ...profile, averagePrice: e.target.value })}
                placeholder="e.g., low, medium, high, or $15-25"
                className="w-full h-11 rounded-xl border-2 border-border/50 bg-card px-4 text-sm text-foreground focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all"
              />
            </div>
          </div>
          <div className="space-y-2">
            <label className="text-sm font-bold text-foreground uppercase tracking-wide">
              Unique Selling Proposition (USP)
            </label>
            <textarea
              value={profile.usp}
              onChange={(e) => setProfile({ ...profile, usp: e.target.value })}
              rows={3}
              className="w-full rounded-xl border-2 border-border/50 bg-card px-4 py-3 text-sm text-foreground focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all resize-none"
            />
          </div>
          <div className="space-y-2">
            <label className="text-sm font-bold text-foreground uppercase tracking-wide">
              Current Offers
            </label>
            <textarea
              value={profile.currentOffers}
              onChange={(e) => setProfile({ ...profile, currentOffers: e.target.value })}
              rows={2}
              placeholder="e.g., 20% off first purchase, Happy hour 3-5pm"
              className="w-full rounded-xl border-2 border-border/50 bg-card px-4 py-3 text-sm text-foreground focus:outline-none focus:border-primary focus:ring-2 focus:ring-primary/20 transition-all resize-none"
            />
          </div>
          <div className="pt-4 flex items-center gap-4">
            <Button 
              size="lg" 
              className="gap-2 premium-button"
              onClick={handleSave}
              disabled={isSaving}
            >
              {isSaving ? (
                <>Saving...</>
              ) : saveSuccess ? (
                <>
                  <Check className="h-4 w-4" />
                  Saved!
                </>
              ) : (
                <>
                  <Save className="h-4 w-4" />
                  Save Changes
                </>
              )}
            </Button>
            {saveSuccess && (
              <span className="text-sm text-success font-medium">Profile updated successfully!</span>
            )}
          </div>
        </CardContent>
      </Card>

      {/* Notifications */}
      <Card className="overflow-hidden hover:shadow-lg transition-all duration-300">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <CardTitle className="flex items-center gap-2 text-xl">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-amber-500/10 border border-amber-500/20">
              <Bell className="h-5 w-5 text-amber-500" />
            </div>
            Notifications
          </CardTitle>
          <CardDescription className="text-base mt-2">Manage how you receive alerts</CardDescription>
        </CardHeader>
        <CardContent className="pt-6 space-y-3">
          <div className="flex items-center justify-between p-5 rounded-xl bg-accent/30 border border-border/30 hover:bg-accent/50 hover:border-border/50 transition-all group cursor-pointer">
            <div className="flex-1">
              <p className="font-bold text-sm mb-1">Competitor Activity Alerts</p>
              <p className="text-xs text-muted-foreground leading-relaxed">Get notified when competitors change pricing or launch promotions</p>
            </div>
            <button className="flex h-7 w-12 items-center rounded-full bg-primary transition-all relative group-hover:shadow-lg group-hover:shadow-primary/20">
              <div className="h-6 w-6 rounded-full bg-white translate-x-5 transition-transform shadow-md" />
            </button>
          </div>
          <div className="flex items-center justify-between p-5 rounded-xl bg-accent/30 border border-border/30 hover:bg-accent/50 hover:border-border/50 transition-all group cursor-pointer">
            <div className="flex-1">
              <p className="font-bold text-sm mb-1">Weekly Reports</p>
              <p className="text-xs text-muted-foreground leading-relaxed">Receive weekly market intelligence summaries</p>
            </div>
            <button className="flex h-7 w-12 items-center rounded-full bg-primary transition-all relative group-hover:shadow-lg group-hover:shadow-primary/20">
              <div className="h-6 w-6 rounded-full bg-white translate-x-5 transition-transform shadow-md" />
            </button>
          </div>
          <div className="flex items-center justify-between p-5 rounded-xl bg-accent/30 border border-border/30 hover:bg-accent/50 hover:border-border/50 transition-all group cursor-pointer">
            <div className="flex-1">
              <p className="font-bold text-sm mb-1">High Threat Alerts</p>
              <p className="text-xs text-muted-foreground leading-relaxed">Immediate notifications for high-threat situations</p>
            </div>
            <button className="flex h-7 w-12 items-center rounded-full bg-primary transition-all relative group-hover:shadow-lg group-hover:shadow-primary/20">
              <div className="h-6 w-6 rounded-full bg-white translate-x-5 transition-transform shadow-md" />
            </button>
          </div>
        </CardContent>
      </Card>

      {/* Subscription */}
      <Card className="overflow-hidden hover:shadow-lg transition-all duration-300">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <CardTitle className="flex items-center gap-2 text-xl">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-emerald-500/10 border border-emerald-500/20">
              <CreditCard className="h-5 w-5 text-emerald-500" />
            </div>
            Subscription
          </CardTitle>
          <CardDescription className="text-base mt-2">Manage your plan and billing</CardDescription>
        </CardHeader>
        <CardContent className="pt-6">
          <div className="rounded-2xl border-2 border-primary/30 bg-gradient-to-br from-indigo-500/10 via-purple-500/10 to-pink-500/10 p-8 shadow-xl">
            <div className="flex flex-col sm:flex-row sm:items-start justify-between gap-6 mb-6">
              <div className="flex-1">
                <div className="flex items-center gap-2 mb-3">
                  <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-primary/20 border border-primary/30">
                    <Zap className="h-5 w-5 text-primary" />
                  </div>
                  <h3 className="text-2xl font-bold">Pro Plan</h3>
                </div>
                <p className="text-sm text-muted-foreground leading-relaxed">
                  Unlimited competitor tracking and AI-powered insights
                </p>
              </div>
              <div className="text-right">
                <p className="text-4xl font-bold tracking-tight">$49</p>
                <p className="text-sm text-muted-foreground font-medium">/month</p>
              </div>
            </div>
            <div className="flex flex-wrap items-center gap-3 pt-6 border-t border-border/30">
              <Button variant="outline" size="lg" className="shadow-md">
                Change Plan
              </Button>
              <Button variant="ghost" size="lg">
                Cancel Subscription
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Security */}
      <Card className="overflow-hidden hover:shadow-lg transition-all duration-300">
        <CardHeader className="border-b border-border/40 bg-card/50">
          <CardTitle className="flex items-center gap-2 text-xl">
            <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-rose-500/10 border border-rose-500/20">
              <Shield className="h-5 w-5 text-rose-500" />
            </div>
            Security
          </CardTitle>
          <CardDescription className="text-base mt-2">Manage your security settings</CardDescription>
        </CardHeader>
        <CardContent className="pt-6 space-y-3">
          <div className="flex items-center justify-between p-5 rounded-xl bg-accent/30 border border-border/30 hover:bg-accent/50 hover:border-border/50 transition-all group cursor-pointer">
            <div className="flex-1">
              <p className="font-bold text-sm mb-1">Change Password</p>
              <p className="text-xs text-muted-foreground leading-relaxed">Update your account password</p>
            </div>
            <Button variant="ghost" size="sm" className="group-hover:bg-accent">
              Change
            </Button>
          </div>
          <div className="flex items-center justify-between p-5 rounded-xl bg-accent/30 border border-border/30 hover:bg-accent/50 hover:border-border/50 transition-all group cursor-pointer">
            <div className="flex-1">
              <p className="font-bold text-sm mb-1">Two-Factor Authentication</p>
              <p className="text-xs text-muted-foreground leading-relaxed">Add an extra layer of security</p>
            </div>
            <Button variant="ghost" size="sm" className="group-hover:bg-accent">
              Enable
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
