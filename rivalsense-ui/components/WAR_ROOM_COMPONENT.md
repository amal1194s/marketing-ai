# War Room Progress Component

A premium animated progress component for visualizing the RivalSense AI agent pipeline.

## Features

✨ **Visual Progress Tracking**
- Real-time step visualization for Scout → Analyst → Strategist pipeline
- Animated progress bar with gradient styling
- Three distinct states: pending, active, completed

🎨 **Premium Design**
- Modern dark UI matching RivalSense design system
- Glowing pulse effects on active steps
- Smooth Framer Motion animations
- Success states with emerald accents

⚡ **Interactive States**
- **Pending**: Muted icons with subtle styling
- **Active**: Pulsing glow, rotating loader, primary colors
- **Completed**: Success checkmark with emerald theme

## Component API

### `<WarRoomProgress />`

```tsx
interface WarRoomProgressProps {
  currentStep?: number; // 0 = Scout, 1 = Analyst, 2 = Strategist
  className?: string;   // Optional Tailwind classes
}
```

### Usage Examples

#### Basic Usage
```tsx
import { WarRoomProgress } from "@/components/war-room-progress";

export default function MyPage() {
  return <WarRoomProgress currentStep={1} />;
}
```

#### With State Management
```tsx
"use client";

import { useState } from "react";
import { WarRoomProgress } from "@/components/war-room-progress";
import { Button } from "@/components/ui/button";

export default function WarRoom() {
  const [step, setStep] = useState(0);
  
  return (
    <div>
      <WarRoomProgress currentStep={step} />
      <Button onClick={() => setStep(step + 1)}>Next Step</Button>
    </div>
  );
}
```

#### Automated Progress
```tsx
"use client";

import { useState, useEffect } from "react";
import { WarRoomProgress } from "@/components/war-room-progress";

export default function AutoProgress() {
  const [step, setStep] = useState(0);
  
  useEffect(() => {
    if (step < 3) {
      const timer = setTimeout(() => setStep(step + 1), 3000);
      return () => clearTimeout(timer);
    }
  }, [step]);
  
  return <WarRoomProgress currentStep={step} />;
}
```

## Step Details

### Step 0: Scout Agent
- **Icon**: Search (Lucide)
- **Name**: "Scout Agent"
- **Description**: "Scanning competitors and promotions"
- **Function**: Monitors competitor activity in real-time

### Step 1: Analyst Agent
- **Icon**: TrendingUp (Lucide)
- **Name**: "Analyst Agent"
- **Description**: "Evaluating market pressure and threats"
- **Function**: Analyzes competitive threats and opportunities

### Step 2: Strategist Agent
- **Icon**: Target (Lucide)
- **Name**: "Strategist Agent"
- **Description**: "Generating action plan and recommendations"
- **Function**: Creates actionable strategies with marketing content

## Animation Details

### Active Step Animations
- **Icon Container**: Continuous pulse scale (1 → 1.05 → 1)
- **Glow Effect**: Fading blur with scale variation
- **Pulse Ring**: Expanding ring from center
- **Loader**: 360° rotation with spin animation
- **Duration**: 2 seconds per cycle

### Transition Animations
- **State Changes**: 0.5s spring animations
- **Icon Swaps**: Scale and rotate transitions
- **Progress Bar**: 0.8s ease-in-out fill
- **Badge Appearance**: Fade + slide animations

### Completion State
- **Icon**: CheckCircle2 with spring animation
- **Colors**: Emerald-500 theme
- **Badge**: "Completed" with checkmark
- **Shadow**: Success glow effect

## Styling

### Color Palette
- **Primary (Active)**: Indigo → Purple gradient
- **Success (Completed)**: Emerald-500
- **Pending**: Muted-foreground
- **Background**: Accent/Border from design system

### Spacing
- Icon container: 24×24 (h-24 w-24)
- Grid gap: 8 (gap-8)
- Icon size: 12×12 (h-12 w-12)
- Badge padding: px-3 py-1

### Shadows
- Active: `shadow-2xl shadow-primary/40`
- Completed: `shadow-lg shadow-emerald-500/20`
- Glow: `blur-xl` with opacity animation

## Dependencies

Required packages (already in RivalSense):
- `framer-motion` - Animation library
- `lucide-react` - Icon components
- `tailwindcss` - Styling
- `clsx` / `tailwind-merge` - Class utilities

## Customization

### Change Step Content
Modify the `defaultSteps` array in the component:

```tsx
const customSteps = [
  {
    id: "step1",
    name: "Custom Step",
    description: "Your description",
    icon: YourIcon,
    status: "pending",
  },
  // ... more steps
];
```

### Adjust Timing
Change animation durations:

```tsx
// Progress bar speed
transition={{ duration: 0.8 }} // ← Adjust this

// Pulse speed
transition={{ duration: 2 }} // ← Adjust this
```

### Custom Colors
Override with className prop:

```tsx
<WarRoomProgress 
  currentStep={1}
  className="[&_.text-primary]:text-blue-500"
/>
```

## Accessibility

- ✅ Semantic HTML structure
- ✅ Proper aria labels on icons
- ✅ Color + icon state indicators
- ✅ Reduced motion support (Framer Motion)
- ✅ Keyboard navigation friendly

## Performance

- **Optimized**: AnimatePresence for efficient DOM updates
- **Lazy Loading**: Icons only render when needed
- **GPU Accelerated**: Transform animations use hardware acceleration
- **Cleanup**: Timers cleared on unmount

## Integration Tips

### With Real API Calls
```tsx
const runWarRoom = async () => {
  setStep(0);
  await scoutAPI.scan();
  
  setStep(1);
  await analystAPI.analyze();
  
  setStep(2);
  await strategistAPI.generate();
};
```

### Error Handling
```tsx
const [error, setError] = useState(null);

// Add error state to component
{error && <ErrorMessage>{error}</ErrorMessage>}
```

### Loading States
```tsx
const [isRunning, setIsRunning] = useState(false);

// Disable controls while running
<Button disabled={isRunning}>Start</Button>
```

## File Locations

- **Component**: `components/war-room-progress.tsx`
- **Page Example**: `app/war-room/page.tsx`
- **Types**: Inline TypeScript interfaces

## Live Demo

Visit `/war-room` in the RivalSense dashboard to see the component in action with automated progression and interactive controls.

## Support

For questions or customization help, refer to:
- [Framer Motion Docs](https://www.framer.com/motion/)
- [Lucide Icons](https://lucide.dev/)
- RivalSense Design System (`POLISH_SUMMARY.md`)
