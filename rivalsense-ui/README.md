# RivalSense AI - Market Intelligence Dashboard

A premium, production-ready AI SaaS dashboard for competitive market intelligence. Built with Next.js 14, TypeScript, Tailwind CSS, shadcn/ui, and Framer Motion.

## 🚀 Features

- **Modern Dark Theme** - Elegant, high-end SaaS design
- **Real-time Competitor Monitoring** - Track pricing, promotions, and market moves
- **AI-Powered Analysis** - Instant threat assessments and intelligence reports
- **Strategic Recommendations** - Actionable strategies with ready-to-use marketing content
- **Beautiful Animations** - Smooth transitions with Framer Motion
- **Fully Responsive** - Optimized for desktop and tablet

## 📁 Project Structure

```
rivalsense-ui/
├── app/
│   ├── page.tsx                 # Landing page
│   ├── layout.tsx               # Root layout
│   ├── globals.css              # Global styles
│   ├── dashboard/
│   │   ├── layout.tsx           # Dashboard layout with sidebar/topbar
│   │   └── page.tsx             # Dashboard overview
│   ├── competitors/
│   │   └── page.tsx             # Competitors monitoring page
│   ├── analysis/
│   │   └── page.tsx             # Market analysis page
│   ├── strategy/
│   │   └── page.tsx             # Strategic recommendations page
│   └── settings/
│       └── page.tsx             # Settings page
├── components/
│   ├── ui/
│   │   ├── button.tsx           # Button component
│   │   └── card.tsx             # Card component
│   ├── sidebar.tsx              # Navigation sidebar
│   └── topbar.tsx               # Top navigation bar
├── lib/
│   ├── utils.ts                 # Utility functions
│   ├── types.ts                 # TypeScript types
│   └── mock-data.ts             # Mock data for demo
├── tailwind.config.ts           # Tailwind configuration
├── tsconfig.json                # TypeScript configuration
└── package.json                 # Dependencies
```

## 🛠️ Tech Stack

- **Framework:** Next.js 14 (App Router)
- **Language:** TypeScript
- **Styling:** Tailwind CSS
- **Components:** shadcn/ui
- **Animations:** Framer Motion
- **Icons:** Lucide React

## 📦 Installation

1. **Install dependencies:**
   ```bash
   npm install
   ```

2. **Run the development server:**
   ```bash
   npm run dev
   ```

3. **Open your browser:**
   Navigate to [http://localhost:3000](http://localhost:3000)

## 🎨 Design System

### Colors
- **Background:** Dark slate (`#0f172a`)
- **Primary:** Indigo (`#6366f1`)
- **Success:** Emerald (`#10b981`)
- **Warning:** Amber (`#f59e0b`)
- **Danger:** Rose (`#f43f5e`)

### Typography
- **Font:** Inter
- **Headings:** Bold, modern style
- **Body:** Readable, clean

### Components
- **Cards:** `rounded-2xl` with soft shadows
- **Buttons:** `rounded-xl` with hover effects
- **Borders:** Subtle, semi-transparent

## 🧩 Page Overview

### Landing Page (`/`)
- Hero section with gradient background
- Feature showcase
- Call-to-action sections
- Modern, startup-style design

### Dashboard (`/dashboard`)
- Stats overview (Threat Score, High Threats, Active Promotions, Monitoring)
- Recent competitive activity
- Key insights panel
- Quick actions

### Competitors (`/competitors`)
- Competitor cards with real-time data
- Pricing, promotions, threat levels
- Trend indicators
- Location information

### Analysis (`/analysis`)
- Overall threat assessment
- Pricing gap analysis
- Market risk breakdown
- Key insights with AI-generated intelligence
- Competitor comparison table

### Strategy (`/strategy`)
- Recommended action
- Pricing strategy
- Campaign ideas
- Ready-to-use marketing posts with copy button
- Execution steps
- Strategy rationale

### Settings (`/settings`)
- Business profile management
- Notification preferences
- Subscription details
- Security settings

## 🎯 Key Components

### Sidebar Navigation
- Fixed left sidebar on desktop
- Active page highlighting
- Brand identity with logo
- Plan indicator

### Topbar
- Search functionality
- Notifications bell
- "Run War Room" CTA button
- User profile avatar

### Stat Cards
- Animated on load
- Color-coded threat levels
- Hover effects
- Icon indicators

### Competitor Cards
- Threat level badges
- Pricing displays
- Promotion alerts
- Trend arrows

## 🚀 Integration Points

This UI is designed to integrate with the RivalSense AI backend:

1. **Scout Agent** - Fetches competitor data
2. **Analyst Agent** - Analyzes market threats
3. **Strategist Agent** - Generates recommendations

Current implementation uses `lib/mock-data.ts` for demo purposes.

## 🎭 Mock Data

The dashboard uses realistic mock data including:
- 3 competitor profiles
- Pricing information
- Active promotions
- Threat assessments
- Strategic recommendations
- Marketing content

To connect real data, replace imports from `lib/mock-data.ts` with API calls.

## 📱 Responsive Design

- **Desktop:** Full sidebar navigation
- **Tablet:** Optimized layouts
- **Mobile:** (Can be enhanced further)

## ⚡ Performance

- Next.js App Router for optimal performance
- Server and Client Components
- Framer Motion animations optimized
- Lazy loading where applicable

## 🎨 Customization

### Colors
Edit `app/globals.css` to change the color scheme:
```css
--primary: 239 84% 67%;  /* Indigo */
--background: 222.2 84% 4.9%;  /* Dark slate */
```

### Typography
Change font in `tailwind.config.ts`:
```typescript
fontFamily: {
  sans: ["Inter", "system-ui", "sans-serif"],
}
```

## 🐛 Troubleshooting

### Animations not working
Install Framer Motion:
```bash
npm install framer-motion
```

### Styles not applying
Ensure Tailwind is properly configured:
```bash
npm install -D tailwindcss postcss autoprefixer
```

### TypeScript errors
Check `tsconfig.json` paths are correct

## 📄 License

Built for RivalSense AI - Market Intelligence Platform

## 🙏 Credits

- UI Design: Premium SaaS dashboard patterns
- Icons: Lucide React
- Components: shadcn/ui
- Animations: Framer Motion

---

**Built with Next.js 14, TypeScript, and modern web technologies** 🚀
