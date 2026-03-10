"use client";

import { motion, AnimatePresence } from "framer-motion";
import { Search, TrendingUp, Target, CheckCircle2, Loader2 } from "lucide-react";
import { cn } from "@/lib/utils";

export type StepStatus = "pending" | "active" | "completed";

interface Step {
  id: string;
  name: string;
  description: string;
  icon: typeof Search;
  status: StepStatus;
}

interface WarRoomProgressProps {
  currentStep?: number; // 0, 1, or 2
  className?: string;
}

const defaultSteps: Step[] = [
  {
    id: "scout",
    name: "Scout Agent",
    description: "Scanning competitors and promotions",
    icon: Search,
    status: "pending",
  },
  {
    id: "analyst",
    name: "Analyst Agent",
    description: "Evaluating market pressure and threats",
    icon: TrendingUp,
    status: "pending",
  },
  {
    id: "strategist",
    name: "Strategist Agent",
    description: "Generating action plan and recommendations",
    icon: Target,
    status: "pending",
  },
];

export function WarRoomProgress({ currentStep = 0, className }: WarRoomProgressProps) {
  const steps = defaultSteps.map((step, index) => ({
    ...step,
    status:
      index < currentStep
        ? "completed"
        : index === currentStep
        ? "active"
        : "pending",
  })) as Step[];

  return (
    <div className={cn("w-full", className)}>
      <div className="relative">
        {/* Progress Bar Background */}
        <div className="absolute top-12 left-0 right-0 h-1 bg-border/30 rounded-full" />

        {/* Animated Progress Bar */}
        <motion.div
          className="absolute top-12 left-0 h-1 bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 rounded-full shadow-lg shadow-primary/30"
          initial={{ width: "0%" }}
          animate={{
            width: currentStep === 0 ? "0%" : currentStep === 1 ? "50%" : "100%",
          }}
          transition={{ duration: 0.8, ease: "easeInOut" }}
        />

        {/* Steps */}
        <div className="relative grid grid-cols-3 gap-8">
          {steps.map((step, index) => (
            <motion.div
              key={step.id}
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ delay: index * 0.1, duration: 0.5 }}
              className="flex flex-col items-center"
            >
              {/* Icon Container */}
              <motion.div
                className={cn(
                  "relative flex h-24 w-24 items-center justify-center rounded-2xl border-2 transition-all duration-500 mb-4",
                  step.status === "completed" &&
                    "bg-emerald-500/10 border-emerald-500/50 shadow-lg shadow-emerald-500/20",
                  step.status === "active" &&
                    "bg-primary/10 border-primary shadow-2xl shadow-primary/40 scale-110",
                  step.status === "pending" &&
                    "bg-accent/30 border-border/50"
                )}
                animate={{
                  scale: step.status === "active" ? [1, 1.05, 1] : 1,
                }}
                transition={{
                  duration: 2,
                  repeat: step.status === "active" ? Infinity : 0,
                  ease: "easeInOut",
                }}
              >
                {/* Glow Effect for Active Step */}
                {step.status === "active" && (
                  <motion.div
                    className="absolute inset-0 rounded-2xl bg-primary/20 blur-xl"
                    animate={{
                      opacity: [0.3, 0.6, 0.3],
                      scale: [1, 1.2, 1],
                    }}
                    transition={{
                      duration: 2,
                      repeat: Infinity,
                      ease: "easeInOut",
                    }}
                  />
                )}

                {/* Icon or Status */}
                <AnimatePresence mode="wait">
                  {step.status === "completed" ? (
                    <motion.div
                      key="completed"
                      initial={{ scale: 0, rotate: -180 }}
                      animate={{ scale: 1, rotate: 0 }}
                      exit={{ scale: 0, rotate: 180 }}
                      transition={{ duration: 0.5, type: "spring" }}
                    >
                      <CheckCircle2 className="h-12 w-12 text-emerald-500" />
                    </motion.div>
                  ) : step.status === "active" ? (
                    <motion.div
                      key="active"
                      initial={{ scale: 0 }}
                      animate={{ scale: 1, rotate: 360 }}
                      exit={{ scale: 0 }}
                      transition={{ duration: 0.5 }}
                    >
                      <Loader2 className="h-12 w-12 text-primary animate-spin" />
                    </motion.div>
                  ) : (
                    <motion.div
                      key="pending"
                      initial={{ scale: 0 }}
                      animate={{ scale: 1 }}
                      exit={{ scale: 0 }}
                    >
                      <step.icon className="h-12 w-12 text-muted-foreground" />
                    </motion.div>
                  )}
                </AnimatePresence>

                {/* Pulse Ring for Active */}
                {step.status === "active" && (
                  <motion.div
                    className="absolute inset-0 rounded-2xl border-2 border-primary"
                    initial={{ scale: 1, opacity: 0.8 }}
                    animate={{ scale: 1.3, opacity: 0 }}
                    transition={{
                      duration: 1.5,
                      repeat: Infinity,
                      ease: "easeOut",
                    }}
                  />
                )}
              </motion.div>

              {/* Step Info */}
              <div className="text-center space-y-1">
                <motion.h3
                  className={cn(
                    "text-lg font-bold transition-colors duration-300",
                    step.status === "completed" && "text-emerald-500",
                    step.status === "active" && "text-primary",
                    step.status === "pending" && "text-muted-foreground"
                  )}
                  animate={{
                    scale: step.status === "active" ? [1, 1.05, 1] : 1,
                  }}
                  transition={{
                    duration: 2,
                    repeat: step.status === "active" ? Infinity : 0,
                  }}
                >
                  {step.name}
                </motion.h3>
                <p
                  className={cn(
                    "text-sm transition-colors duration-300",
                    step.status === "active"
                      ? "text-foreground font-medium"
                      : "text-muted-foreground"
                  )}
                >
                  {step.description}
                </p>

                {/* Status Badge */}
                <AnimatePresence mode="wait">
                  {step.status === "completed" && (
                    <motion.div
                      initial={{ opacity: 0, y: -10 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: 10 }}
                      className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-emerald-500/10 border border-emerald-500/30 text-xs font-semibold text-emerald-500 mt-2"
                    >
                      <CheckCircle2 className="h-3 w-3" />
                      Completed
                    </motion.div>
                  )}
                  {step.status === "active" && (
                    <motion.div
                      initial={{ opacity: 0, y: -10 }}
                      animate={{ opacity: 1, y: 0 }}
                      exit={{ opacity: 0, y: 10 }}
                      className="inline-flex items-center gap-1.5 px-3 py-1 rounded-full bg-primary/10 border border-primary/30 text-xs font-semibold text-primary mt-2"
                    >
                      <motion.div
                        animate={{ rotate: 360 }}
                        transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                      >
                        <Loader2 className="h-3 w-3" />
                      </motion.div>
                      In Progress
                    </motion.div>
                  )}
                </AnimatePresence>
              </div>
            </motion.div>
          ))}
        </div>
      </div>
    </div>
  );
}
