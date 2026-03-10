"use client";

import Link from "next/link";
import { usePathname } from "next/navigation";
import { 
  LayoutDashboard, 
  Users, 
  TrendingUp, 
  Target, 
  Settings,
  Zap,
  Sparkles
} from "lucide-react";
import { cn } from "@/lib/utils";

const navigation = [
  { name: "Dashboard", href: "/dashboard", icon: LayoutDashboard },
  { name: "Competitors", href: "/competitors", icon: Users },
  { name: "Analysis", href: "/analysis", icon: TrendingUp },
  { name: "Strategy", href: "/strategy", icon: Target },
  { name: "War Room", href: "/war-room", icon: Sparkles },
  { name: "Settings", href: "/settings", icon: Settings },
];

export function Sidebar() {
  const pathname = usePathname();

  return (
    <div className="hidden lg:fixed lg:inset-y-0 lg:z-50 lg:flex lg:w-72 lg:flex-col">
      <div className="flex grow flex-col gap-y-5 overflow-y-auto border-r border-border/50 bg-card/50 backdrop-blur-xl px-6 pb-6">
        <div className="flex h-16 shrink-0 items-center gap-3 pt-6">
          <div className="flex h-11 w-11 items-center justify-center rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 shadow-lg shadow-indigo-500/25 ring-2 ring-background">
            <Zap className="h-6 w-6 text-white" />
          </div>
          <div className="flex flex-col">
            <span className="text-xl font-bold bg-gradient-to-r from-indigo-400 to-purple-400 bg-clip-text text-transparent">
              RivalSense
            </span>
            <span className="text-xs text-muted-foreground font-medium">Market Intelligence</span>
          </div>
        </div>
        <nav className="flex flex-1 flex-col">
          <ul role="list" className="flex flex-1 flex-col gap-y-7">
            <li>
              <ul role="list" className="-mx-2 space-y-2">
                {navigation.map((item) => {
                  const isActive = pathname === item.href;
                  return (
                    <li key={item.name}>
                      <Link
                        href={item.href}
                        className={cn(
                          "group flex gap-x-3 rounded-xl p-3 text-sm font-semibold leading-6 transition-all duration-200",
                          isActive
                            ? "bg-primary text-primary-foreground shadow-lg shadow-primary/25 scale-[1.02]"
                            : "text-muted-foreground hover:text-foreground hover:bg-accent hover:scale-[1.01]"
                        )}
                      >
                        <item.icon
                          className={cn(
                            "h-5 w-5 shrink-0 transition-transform duration-200",
                            isActive ? "scale-110" : "group-hover:scale-105"
                          )}
                          aria-hidden="true"
                        />
                        {item.name}
                      </Link>
                    </li>
                  );
                })}
              </ul>
            </li>
            <li className="mt-auto">
              <div className="rounded-2xl border-2 border-border/50 bg-gradient-to-br from-indigo-500/10 via-purple-500/10 to-pink-500/10 p-5 hover:border-primary/30 transition-all duration-300 group cursor-pointer">
                <div className="flex items-center gap-3">
                  <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-gradient-to-br from-indigo-500 to-purple-600 shadow-lg group-hover:scale-105 transition-transform">
                    <Zap className="h-6 w-6 text-white" />
                  </div>
                  <div className="flex-1">
                    <p className="text-sm font-bold">Pro Plan</p>
                    <p className="text-xs text-muted-foreground">Unlimited scans</p>
                  </div>
                </div>
              </div>
            </li>
          </ul>
        </nav>
      </div>
    </div>
  );
}
