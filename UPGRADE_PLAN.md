# 🚀 RivalSense AI - Multi-Business Platform Upgrade Plan

## 🎯 Goal
Transform from fixed pizza/coffee demo → Dynamic platform for ANY business type

---

## 📋 Implementation Phases

### Phase 1: Core Infrastructure (Priority: HIGH)
**Status:** Ready to implement

1. **Dynamic Business Profile System**
   - Create onboarding flow (multi-step form)
   - Capture: name, category, city, audience, price, USP
   - Store in backend or localStorage initially

2. **Flexible Backend Models**
   - Update Scout to accept dynamic URLs
   - Make Analyst category-agnostic
   - Make Strategist adapt to any business type

3. **Database Schema** (Optional for hackathon)
   - Use JSON files initially for speed
   - Can upgrade to SQLite/Postgres later

### Phase 2: UI/UX Polish (Priority: HIGH)
**Status:** Can improve existing pages

1. **Onboarding Page** - New
2. **Business Profile Card** - New component
3. **Competitor Management** - New UI
4. **Dynamic Dashboard** - Update existing
5. **Premium Polish** - Enhance spacing/typography

### Phase 3: Agent Intelligence (Priority: MEDIUM)
**Status:** Refactor existing agents

1. **Scout Agent** - Parse live URLs
2. **Analyst Agent** - Remove food-specific assumptions
3. **Strategist Agent** - Adapt to business category

---

## 🎬 Quick Win Strategy (2-3 Hours)

### Immediate Changes:
1. ✅ Create onboarding form (capture business profile)
2. ✅ Store profile in localStorage/backend
3. ✅ Pass profile dynamically to War Room
4. ✅ Update agent prompts to be category-aware
5. ✅ Polish UI for investor demo

### Technical Approach:
- **Frontend:** Add /onboarding route
- **Backend:** Add POST /profile endpoint
- **Agents:** Use f-strings with {category} variables
- **Storage:** JSON files for now (fast for hackathon)

---

## 📂 Files to Create/Modify

### New Files:
```
rivalsense-ui/
├── app/onboarding/page.tsx          (multi-step form)
├── components/onboarding-form.tsx   (form component)
├── components/business-profile.tsx  (profile card)
├── components/competitor-card.tsx   (competitor mgmt)
└── lib/storage.ts                   (profile storage)

backend/
├── api_server.py                    (add profile endpoints)
├── models.py                        (business profile schema)
└── storage/
    ├── profiles.json                (user data)
    └── competitors.json             (competitor data)
```

### Files to Update:
```
- agent_b_analyst.py                 (make category-aware)
- agent_c_strategist.py              (dynamic recommendations)
- app/war-room/page.tsx              (use dynamic profile)
- app/dashboard/page.tsx             (show user's business)
```

---

## 🎨 UI/UX Improvements

### Onboarding Flow:
```
Step 1: Business Details
  - Name, Category, City, Audience, Price

Step 2: Add Competitors
  - Name, Website URL, Social URL

Step 3: Review & Launch
  - Summary, "Run War Room" CTA
```

### Dashboard Updates:
- Show YOUR business profile (not hardcoded example)
- Show YOUR competitors (dynamic)
- Run War Room with YOUR data

---

## 🔧 Technical Implementation

### 1. Onboarding Form (Frontend)
```typescript
interface BusinessProfile {
  name: string;
  category: string;
  city: string;
  targetAudience: string;
  averagePrice: number;
  currentOffers: string;
  usp: string;
}

interface Competitor {
  name: string;
  websiteUrl: string;
  socialUrl?: string;
  category: string;
}
```

### 2. Backend Profile Endpoint
```python
@app.post("/profile")
async def create_profile(profile: BusinessProfile):
    # Save to JSON file
    # Return profile ID
    pass
```

### 3. Dynamic Agent Prompts
```python
# Before: "Your pizza shop..."
# After: f"Your {business_profile.category} business..."
```

---

## ⚡ Quick Wins for Demo

1. **Onboarding → Dashboard Flow**
   - User enters business → sees personalized dashboard

2. **Dynamic War Room**
   - Uses user's actual business data
   - Compares against user's competitors

3. **Category-Aware Results**
   - Strategy adapts to business type
   - Marketing post fits the niche

---

## 🎯 Success Metrics

- ✅ Works for 5+ different business types
- ✅ No hardcoded assumptions
- ✅ User can input real data
- ✅ Results feel personalized
- ✅ UI looks premium

---

## 🚦 Implementation Order (Recommended)

**Day 1 (3-4 hours):**
1. Create onboarding form UI
2. Add profile storage (localStorage)
3. Update War Room to use stored profile
4. Test with 2-3 different business types

**Day 2 (2-3 hours):**
5. Make agents category-agnostic
6. Polish UI (spacing, typography, animations)
7. Add competitor management UI

**Day 3 (2-3 hours):**
8. Add backend profile endpoints
9. Connect frontend to backend
10. Final polish and testing

---

## 💡 MVP Features (Hackathon-Ready)

**Must Have:**
- ✅ Onboarding form
- ✅ Profile storage
- ✅ Dynamic War Room
- ✅ Category-aware agents

**Nice to Have:**
- Competitor URL parsing
- Historical analysis
- Multi-profile support
- Export reports

**Future:**
- Real-time scraping
- Email alerts
- Team collaboration
- API integrations

---

**Ready to implement? Let's start with the onboarding form!** 🚀
