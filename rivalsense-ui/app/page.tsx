"use client";

import Link from "next/link";
import { ArrowRight, Zap, TrendingUp, Target, Shield, ChevronRight, Play } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { motion } from "framer-motion";

const features = [
  {
    name: "Real-time Monitoring",
    description: "Track competitor pricing, promotions, and market moves as they happen.",
    icon: TrendingUp,
  },
  {
    name: "AI-Powered Analysis",
    description: "Get instant threat assessments and market intelligence reports.",
    icon: Zap,
  },
  {
    name: "Strategic Recommendations",
    description: "Receive actionable strategies with ready-to-use marketing content.",
    icon: Target,
  },
  {
    name: "Enterprise-Grade Security",
    description: "Your competitive intelligence is protected with bank-level encryption.",
    icon: Shield,
  },
];

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

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-background via-background to-indigo-950/20">
      {/* Navigation */}
      <nav className="fixed top-0 w-full z-50 bg-background/80 backdrop-blur-xl border-b border-border/50">
        <div className="max-w-7xl mx-auto px-6 sm:px-8 lg:px-12">
          <div className="flex h-16 items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 shadow-lg shadow-indigo-500/25">
                <Zap className="h-6 w-6 text-white" />
              </div>
              <span className="text-xl font-bold bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent">
                RivalSense AI
              </span>
            </div>
            <div className="flex items-center gap-4">
              <Link href="/dashboard">
                <Button variant="ghost" className="hidden sm:flex">
                  Sign In
                </Button>
              </Link>
              <Link href="/dashboard">
                <Button className="gap-2">
                  Get Started
                  <ArrowRight className="h-4 w-4" />
                </Button>
              </Link>
            </div>
          </div>
        </div>
      </nav>

      {/* Hero Section */}
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="relative isolate px-6 pt-14 lg:px-8"
      >
        <div
          className="absolute inset-x-0 -top-40 -z-10 transform-gpu overflow-hidden blur-3xl sm:-top-80"
          aria-hidden="true"
        >
          <div
            className="relative left-[calc(50%-11rem)] aspect-[1155/678] w-[36.125rem] -translate-x-1/2 rotate-[30deg] bg-gradient-to-tr from-indigo-500 to-purple-600 opacity-20 sm:left-[calc(50%-30rem)] sm:w-[72.1875rem]"
            style={{
              clipPath:
                "polygon(74.1% 44.1%, 100% 61.6%, 97.5% 26.9%, 85.5% 0.1%, 80.7% 2%, 72.5% 32.5%, 60.2% 62.4%, 52.4% 68.1%, 47.5% 58.3%, 45.2% 34.5%, 27.5% 76.7%, 0.1% 64.9%, 17.9% 100%, 27.6% 76.8%, 76.1% 97.7%, 74.1% 44.1%)",
            }}
          />
        </div>
        <div className="mx-auto max-w-3xl py-32 sm:py-48 lg:py-56">
          <div className="text-center">
            <motion.div
              initial={{ opacity: 0, scale: 0.95 }}
              animate={{ opacity: 1, scale: 1 }}
              transition={{ duration: 0.5 }}
              className="inline-flex items-center gap-2 rounded-full bg-primary/10 px-5 py-2 text-sm font-semibold text-primary ring-1 ring-inset ring-primary/20 mb-8 hover:bg-primary/15 transition-all cursor-pointer"
            >
              <Zap className="h-4 w-4" />
              AI-Powered Market Intelligence
            </motion.div>
            <h1 className="text-5xl font-bold tracking-tight text-foreground sm:text-7xl mb-6 leading-tight">
              Stay Ahead of Your{" "}
              <span className="bg-gradient-to-r from-indigo-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
                Competition
              </span>
            </h1>
            <p className="text-lg leading-relaxed text-muted-foreground max-w-2xl mx-auto mb-10">
              RivalSense AI monitors your competitors 24/7, analyzes market threats, and delivers 
              actionable strategies—so you can focus on growing your business.
            </p>
            <div className="flex flex-col sm:flex-row items-center justify-center gap-4">
              <Link href="/dashboard">
                <Button size="lg" className="gap-2 text-base px-8 h-14 shadow-2xl shadow-primary/25 hover:shadow-primary/40 transition-all w-full sm:w-auto">
                  <Play className="h-5 w-5 fill-current" />
                  Start Free Trial
                </Button>
              </Link>
              <Link href="/dashboard">
                <Button size="lg" variant="outline" className="gap-2 text-base h-14 w-full sm:w-auto">
                  Watch Demo
                  <ChevronRight className="h-4 w-4" />
                </Button>
              </Link>
            </div>
            <p className="mt-6 text-sm text-muted-foreground font-medium">
              No credit card required • 14-day free trial • Cancel anytime
            </p>
          </div>
        </div>
      </motion.div>

      {/* Features Section */}
      <motion.div
        variants={container}
        initial="hidden"
        whileInView="show"
        viewport={{ once: true }}
        className="mx-auto max-w-7xl px-6 lg:px-8 py-24 sm:py-32"
      >
        <div className="mx-auto max-w-2xl text-center mb-20">
          <h2 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl mb-4">
            Everything you need to outsmart the competition
          </h2>
          <p className="mt-4 text-lg text-muted-foreground leading-relaxed">
            Powerful features designed for modern businesses
          </p>
        </div>
        <div className="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-none">
          <dl className="grid max-w-xl grid-cols-1 gap-8 lg:max-w-none lg:grid-cols-2">
            {features.map((feature, index) => (
              <motion.div key={feature.name} variants={item}>
                <Card className="relative overflow-hidden hover:border-primary/50 transition-all duration-300 group hover:shadow-xl hover:shadow-primary/5 h-full">
                  <div className="absolute inset-0 bg-gradient-to-br from-primary/5 to-transparent opacity-0 group-hover:opacity-100 transition-opacity" />
                  <CardContent className="p-8 relative">
                    <div className="flex items-start gap-4">
                      <div className="flex h-14 w-14 items-center justify-center rounded-xl bg-gradient-to-br from-indigo-500/20 to-purple-600/20 ring-2 ring-primary/20 group-hover:ring-primary/40 transition-all group-hover:scale-110 shrink-0">
                        <feature.icon className="h-7 w-7 text-primary" />
                      </div>
                      <div className="flex-1">
                        <dt className="text-xl font-bold leading-7 text-foreground mb-3">
                          {feature.name}
                        </dt>
                        <dd className="text-sm leading-7 text-muted-foreground">
                          {feature.description}
                        </dd>
                      </div>
                    </div>
                  </CardContent>
                </Card>
              </motion.div>
            ))}
          </dl>
        </div>
      </motion.div>

      {/* CTA Section */}
      <motion.div
        initial={{ opacity: 0 }}
        whileInView={{ opacity: 1 }}
        viewport={{ once: true }}
        className="mx-auto max-w-7xl px-6 lg:px-8 py-24 sm:py-32"
      >
        <Card className="relative overflow-hidden bg-gradient-to-br from-indigo-500/10 via-purple-600/10 to-pink-500/10 border-primary/30 group hover:shadow-2xl hover:shadow-primary/10 transition-all duration-500">
          <div className="absolute inset-0 bg-gradient-to-r from-indigo-500/5 to-purple-600/5 opacity-0 group-hover:opacity-100 transition-opacity" />
          <CardContent className="p-12 sm:p-16 lg:p-20 relative">
            <div className="mx-auto max-w-2xl text-center">
              <h2 className="text-4xl font-bold tracking-tight text-foreground sm:text-5xl mb-6">
                Ready to gain the competitive edge?
              </h2>
              <p className="text-lg text-muted-foreground mb-10 leading-relaxed">
                Join hundreds of businesses using AI to stay ahead of the market.
              </p>
              <Link href="/dashboard">
                <Button size="lg" className="gap-2 text-base px-10 h-14 shadow-2xl shadow-primary/30 hover:shadow-primary/50 transition-all">
                  Get Started Now
                  <ArrowRight className="h-5 w-5" />
                </Button>
              </Link>
            </div>
          </CardContent>
        </Card>
      </motion.div>

      {/* Footer */}
      <footer className="border-t border-border/50 mt-32 bg-card/30">
        <div className="mx-auto max-w-7xl px-6 py-16 md:flex md:items-center md:justify-between lg:px-8">
          <div className="flex justify-center md:order-2">
            <p className="text-sm text-muted-foreground font-medium">
              Built with Next.js, TypeScript, and AI
            </p>
          </div>
          <div className="mt-8 md:order-1 md:mt-0">
            <div className="flex items-center justify-center md:justify-start gap-3 mb-4">
              <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 shadow-lg">
                <Zap className="h-5 w-5 text-white" />
              </div>
              <span className="text-xl font-bold bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent">
                RivalSense AI
              </span>
            </div>
            <p className="text-center md:text-left text-sm text-muted-foreground">
              &copy; 2026 RivalSense AI. All rights reserved.
            </p>
          </div>
        </div>
      </footer>
    </div>
  );
}
