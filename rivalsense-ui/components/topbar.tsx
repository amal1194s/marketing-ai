"use client";

import { useState, useEffect } from "react";
import { Play, Bell, Search } from "lucide-react";
import { Button } from "@/components/ui/button";
import Link from "next/link";

export function Topbar() {
  const [userName, setUserName] = useState("Tom Parker");

  useEffect(() => {
    // Load user name from localStorage
    const savedUserName = localStorage.getItem("userName");
    if (savedUserName && savedUserName.trim()) {
      setUserName(savedUserName);
    }
  }, []);

  const initials = userName
    .split(' ')
    .map(n => n[0])
    .join('')
    .toUpperCase()
    .slice(0, 2);

  return (
    <div className="sticky top-0 z-40 flex h-16 shrink-0 items-center gap-x-4 border-b border-border/50 bg-background/95 backdrop-blur-xl supports-[backdrop-filter]:bg-background/80 px-4 sm:px-6 lg:px-8 shadow-sm">
      <div className="flex flex-1 gap-x-4 self-stretch lg:gap-x-6 items-center">
        <form className="relative flex flex-1 max-w-2xl" action="#" method="GET">
          <Search className="pointer-events-none absolute left-3.5 top-1/2 -translate-y-1/2 h-4 w-4 text-muted-foreground" />
          <input
            id="search-field"
            className="block h-10 w-full rounded-xl border border-border/50 bg-card/50 pl-10 pr-4 text-sm text-foreground placeholder:text-muted-foreground focus:border-primary/50 focus:ring-2 focus:ring-primary/20 focus:bg-card outline-none transition-all duration-200"
            placeholder="Search competitors, insights, strategies..."
            type="search"
            name="search"
          />
        </form>
        
        <div className="flex items-center gap-x-3 lg:gap-x-4">
          <button
            type="button"
            className="relative -m-2 p-2.5 text-muted-foreground hover:text-foreground transition-colors rounded-lg hover:bg-accent"
            aria-label="View notifications"
          >
            <Bell className="h-5 w-5" aria-hidden="true" />
            <span className="absolute top-1.5 right-1.5 h-2 w-2 rounded-full bg-rose-500 ring-2 ring-background animate-pulse" />
          </button>

          <div className="hidden lg:block lg:h-6 lg:w-px lg:bg-border/50" aria-hidden="true" />

          <Link href="/war-room">
            <Button size="default" className="gap-2">
              <Play className="h-4 w-4 fill-current" />
              Run War Room
            </Button>
          </Link>

          <div className="hidden lg:block lg:h-6 lg:w-px lg:bg-border/50" aria-hidden="true" />

          <button className="relative flex items-center gap-x-3 rounded-xl hover:bg-accent p-2 transition-all duration-200 group">
            <div className="flex h-9 w-9 items-center justify-center rounded-full bg-gradient-to-br from-primary to-accent text-sm font-bold text-background shadow-lg ring-2 ring-background group-hover:shadow-xl group-hover:scale-105 transition-all duration-200">
              {initials}
            </div>
            <div className="hidden lg:block text-left">
              <p className="text-sm font-semibold text-foreground">{userName}</p>
              <p className="text-xs text-muted-foreground">Pro Plan</p>
            </div>
          </button>
        </div>
      </div>
    </div>
  );
}
