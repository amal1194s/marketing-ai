# 🚀 MULTI-BUSINESS PLATFORM - QUICK TEST GUIDE

**Purpose:** Test the upgraded RivalSense AI system with multiple business types

---

## ✅ WHAT'S NEW

**Before:** Fixed demo for pizza/coffee shops only  
**After:** Dynamic platform supporting ANY business type

**New Features:**
- ✨ Multi-step onboarding form
- 💾 Profile and competitor management
- 🎯 Category-agnostic AI agents
- 📊 Dynamic dashboard with profile display
- ⚡ Backend API for profile storage

---

## 🧪 TEST SCENARIOS

### Scenario 1: Gym/Fitness Center

#### 1. Complete Onboarding
```
Navigate to: http://localhost:3000/onboarding

Step 1 - Business Details:
  Name: FitZone Gym
  Category: Fitness Center
  City: Austin
  Target Audience: Young professionals aged 25-40
  Average Price: $50/month
  Current Offers: First month free for new members
  USP: 24/7 access with certified personal trainers and premium equipment

Step 2 - Add Competitors:
  Competitor 1:
    Name: Planet Fitness
    Website: https://www.planetfitness.com
    Social: https://facebook.com/planetfitness
    Category: Budget Gym
    
  Competitor 2:
    Name: LA Fitness
    Website: https://www.lafitness.com
    Social: https://instagram.com/lafitness
    Category: Full-Service Gym

Step 3 - Review & Launch:
  ✓ Verify all data is correct
  ✓ Click "Launch Dashboard"
```

#### 2. Expected Results

**Dashboard:**
- Should show "FitZone Gym" in profile card
- Category displayed as "Fitness Center"
- Shows "2 competitors tracked"
- USP visible: "24/7 access with certified personal trainers..."

**War Room:**
- Profile setup check passes
- Can run War Room analysis
- Agent output should say "facility" not "restaurant"
- Example: "Your facility's pricing is competitive..."

**Category-Adapted Language:**
- ❌ Avoid: "pizza", "restaurant", "menu", "delivery"
- ✅ Expect: "memberships", "facility", "training", "packages"

---

### Scenario 2: Hair Salon

#### 1. Complete Onboarding
```
Navigate to: http://localhost:3000/onboarding

Step 1 - Business Details:
  Name: Luxe Hair Studio
  Category: Hair Salon
  City: Miami
  Target Audience: Women 30-50 seeking premium hair care
  Average Price: $120 per visit
  Current Offers: 20% off first visit, referral discounts
  USP: Master stylists with 15+ years experience, organic products only

Step 2 - Add Competitors:
  Competitor 1:
    Name: Supercuts
    Website: https://www.supercuts.com
    Social: https://instagram.com/supercuts
    Category: Budget Hair Salon
    
  Competitor 2:
    Name: Salon Republic
    Website: https://www.salonrepublic.com
    Social: https://facebook.com/salonrepublic
    Category: Premium Salon

Step 3 - Review & Launch
```

#### 2. Expected Results

**Dashboard:**
- Profile card shows "Luxe Hair Studio"
- Category: "Hair Salon"
- Competitors: 2

**War Room Analysis:**
- ❌ Avoid: "pizza", "restaurant", "food"
- ✅ Expect: "salon", "services", "treatments", "specials"

---

### Scenario 3: Consulting Firm

#### 1. Complete Onboarding
```
Step 1 - Business Details:
  Name: Apex Strategy Consulting
  Category: Business Consulting
  City: New York
  Target Audience: Mid-size companies ($10M-$100M revenue)
  Average Price: $15,000 per project
  Current Offers: Free initial consultation, package discounts
  USP: Former Fortune 500 executives with proven ROI track record

Step 2 - Add Competitors:
  Competitor 1:
    Name: McKinsey & Company
    Website: https://www.mckinsey.com
    Social: https://linkedin.com/company/mckinsey
    Category: Top-Tier Consulting
    
  Competitor 2:
    Name: Deloitte Consulting
    Website: https://www.deloitte.com/consulting
    Social: https://linkedin.com/company/deloitte
    Category: Big Four Consulting

Step 3 - Review & Launch
```

#### 2. Expected Results

**Category-Adapted Language:**
- ❌ Avoid: "pizza", "restaurant", "delivery", "menu"
- ✅ Expect: "firm", "services", "consulting", "packages"

---

### Scenario 4: Coffee Shop (Original Domain)

#### 1. Complete Onboarding
```
Step 1 - Business Details:
  Name: Bean & Brew Cafe
  Category: Coffee Shop
  City: Seattle
  Target Audience: Remote workers and students
  Average Price: $5 per drink
  Current Offers: Buy 10 get 1 free loyalty card
  USP: Locally roasted beans, cozy workspace with free WiFi

Step 2 - Add Competitors:
  Competitor 1:
    Name: Starbucks
    Website: https://www.starbucks.com
    Social: https://instagram.com/starbucks
    Category: Coffee Chain
    
  Competitor 2:
    Name: Local Grounds
    Website: https://localgrounds.com
    Social: https://facebook.com/localgrounds
    Category: Indie Coffee Shop
```

#### 2. Expected Results

**Category-Adapted Language:**
- ✅ Should say "cafe" or "coffee shop" (appropriate for category)
- ✅ Can use "drinks", "cafe experience"
- ❌ Should NOT say "pizza" or "restaurant"

---

### Scenario 5: Bakery

#### 1. Complete Onboarding
```
Step 1 - Business Details:
  Name: Sunrise Artisan Bakery
  Category: Bakery
  City: Portland
  Target Audience: Families and breakfast lovers
  Average Price: $8 per item
  Current Offers: Daily special: buy 6 get 1 free
  USP: Fresh-baked daily using organic local ingredients

Step 2 - Add Competitors:
  Competitor 1:
    Name: Panera Bread
    Website: https://www.panerabread.com
    Social: https://instagram.com/panerabread
    Category: Bakery Chain
    
  Competitor 2:
    Name: Corner Bakery
    Website: https://www.cornerbakery.com
    Social: https://facebook.com/cornerbakery
    Category: Fast Casual Bakery
```

#### 2. Expected Results

**Category-Adapted Language:**
- ✅ Should say "bakery", "baked goods", "daily specials"
- ❌ Should NOT say "pizza" or generic "food items"

---

## 🔍 VALIDATION CHECKLIST

For each test scenario, verify:

### Onboarding Flow
- [ ] Form accepts all business types
- [ ] Category field allows custom input
- [ ] Can add/remove multiple competitors
- [ ] Progress indicator works (1 → 2 → 3)
- [ ] Validation requires name/category/city
- [ ] Validation requires at least 1 competitor
- [ ] localStorage saves profile correctly
- [ ] localStorage saves competitors correctly
- [ ] Redirects to dashboard after completion

### Dashboard Display
- [ ] Shows empty state if no profile
- [ ] Profile card displays business name
- [ ] Category shown correctly (not "pizza" for gym)
- [ ] Competitor count is accurate
- [ ] USP displayed (truncated if long)
- [ ] "Edit Profile" button present
- [ ] Welcome message adapts to category

### War Room Functionality
- [ ] Shows "Complete Onboarding" warning if no profile
- [ ] Loads profile from localStorage on mount
- [ ] Validates profile exists before running
- [ ] Backend API call succeeds
- [ ] Category adapter transforms output
- [ ] No food-specific terms for non-food businesses

### Category Adapter Output
- [ ] Replaces "pizza shop" with appropriate term (facility, salon, firm)
- [ ] Replaces "restaurant" with category-appropriate location
- [ ] Preserves possessive forms ("shop's" → "facility's")
- [ ] No leftover food terms in non-food categories
- [ ] Text is grammatically correct after transformation

### Backend API
- [ ] POST /profile saves successfully
- [ ] GET /profile retrieves saved profile
- [ ] POST /competitors saves list
- [ ] GET /competitors returns list
- [ ] POST /run-war-room uses category adapter
- [ ] Files saved to data/profiles/ directory

---

## 🐛 KNOWN ISSUES & EDGE CASES

### Issue 1: Category Adapter Limitations
**Problem:** Some complex sentences may not adapt perfectly  
**Example:** "Your pizza's unique toppings attract customers"  
**Status:** Minor - most common phrases handled correctly  
**Workaround:** Agent output will improve over time with more testing

### Issue 2: Mock Data Still Showing
**Problem:** Dashboard stats use mockCompetitors, not real data  
**Status:** Expected - stats not connected to real analysis yet  
**Workaround:** Future update will connect dashboard to actual War Room results

### Issue 3: Competitor Data Not Used
**Problem:** War Room still uses example JSON files, not saved competitors  
**Status:** Partial - profile loads from localStorage, competitors pending full integration  
**Workaround:** Next update will pass competitors to backend

---

## 📊 TEST RESULTS TEMPLATE

Use this template to document test results:

```
Test Date: ___________
Tester: ___________

Scenario: [Gym / Salon / Consulting / Coffee / Bakery]

✅ PASSED:
- Onboarding form works
- Profile saved to localStorage
- Dashboard shows profile card
- War Room loads profile
- Category adapter transforms text

❌ FAILED:
- [List any failures]

🐛 BUGS FOUND:
- [Describe any bugs]

💡 SUGGESTIONS:
- [List improvements]
```

---

## 🎯 SUCCESS CRITERIA

**System PASSES if:**
1. ✅ Onboarding works for 5+ different business types
2. ✅ Dashboard adapts to each category (no hardcoded "pizza")
3. ✅ War Room checks for profile before running
4. ✅ Category adapter transforms agent output correctly
5. ✅ localStorage persists profile/competitors
6. ✅ Backend endpoints save/retrieve data
7. ✅ No food-specific language for non-food businesses

**System FAILS if:**
1. ❌ Onboarding crashes for certain categories
2. ❌ Dashboard still says "pizza" for gym business
3. ❌ War Room runs without profile (should redirect)
4. ❌ Category adapter leaves food terms in output
5. ❌ localStorage doesn't persist data
6. ❌ Backend endpoints return errors
7. ❌ Text transformations are grammatically incorrect

---

## 🚀 RUNNING THE TESTS

### Prerequisites
```bash
# Terminal 1: Start Backend
cd d:\marketing-ai
python api_server.py

# Terminal 2: Start Frontend
cd d:\marketing-ai\rivalsense-ui
npm run dev

# Open browser
http://localhost:3000/onboarding
```

### Test Sequence
1. Start with **Scenario 1 (Gym)** - most different from food
2. Test **Scenario 2 (Salon)** - verify variety
3. Test **Scenario 3 (Consulting)** - B2B use case
4. Test **Scenario 4 (Coffee)** - original domain
5. Test **Scenario 5 (Bakery)** - validate food category still works

---

## 📞 NEED HELP?

**Documentation:**
- `MULTI_BUSINESS_STATUS.md` - Implementation details
- `UPGRADE_PLAN.md` - Original plan
- `README.md` - Project overview

**Code References:**
- Onboarding: `rivalsense-ui/app/onboarding/page.tsx`
- Storage: `rivalsense-ui/lib/storage.ts`
- Category Adapter: `utils/category_adapter.py`
- Backend API: `api_server.py`

**Test Category Adapter:**
```bash
cd d:\marketing-ai
python utils/category_adapter.py
```

**Check API Endpoints:**
```bash
# Test profile endpoint
curl http://localhost:8000/health

# Test save profile
curl -X POST http://localhost:8000/profile \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Gym","category":"Fitness","city":"Austin","targetAudience":"Athletes","averagePrice":"$50","currentOffers":"Free trial","usp":"Best equipment"}'
```

---

**Last Updated:** December 2024  
**Version:** 1.0  
**Status:** Ready for Testing
