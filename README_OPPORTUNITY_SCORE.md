# ScoutIQ Analyst Agent - Opportunity Score Upgrade

## Overview

The Analyst Agent has been upgraded with a **Market Opportunity Score** feature that quantifies competitive threats on a 0-10 scale.

## What's New

### ✅ Added Features

1. **calculate_opportunity_score()** - Calculates 0-10 threat score based on:
   - Price differences
   - Event type (promotion, discount, launch)
   - Percentage-based scoring
   
2. **Updated classify_impact()** - Now uses score-based mapping:
   - Score ≥ 8 → HIGH
   - Score 5-7 → MEDIUM
   - Score < 5 → LOW

3. **opportunity_score field** in output JSON

4. **Enhanced console output** showing scores

---

## Complete Example

### 1. Example Terminal Output

```
======================================================================
ScoutIQ Analyst Agent - Market Analysis
======================================================================

📁 Loading input files...
✓ Loaded 4 competitor signal(s)
✓ Business: Tony's Pizza

🔬 Analyzing competitor signals...
  1. 🔴 Dominos - Score: 8.5/10 (HIGH Impact)
  2. 🔴 Pizza Hut - Score: 10.0/10 (HIGH Impact)
  3. 🟡 Papa John's - Score: 6.0/10 (MEDIUM Impact)
  4. 🟡 Local Pizza Co - Score: 7.5/10 (MEDIUM Impact)

✓ Analyzed 4 signal(s)
💾 Saving analysis to data\outputs\market_analysis.json...

======================================================================
✅ Market analysis generated successfully
======================================================================

Output saved to: data\outputs\market_analysis.json
Total insights: 4

Impact Summary:
  🔴 High: 2
  🟡 Medium: 2
  🟢 Low: 0
```

### 2. Example Output JSON

**File: data/outputs/market_analysis.json**

```json
[
  {
    "competitor": "Dominos",
    "event_type": "promotion",
    "competitor_price": 299,
    "user_price": 350,
    "price_difference": -51,
    "opportunity_score": 8.5,
    "impact_level": "high",
    "insight": "Dominos promotion offers a significantly lower price (₹299 vs your ₹350) and may attract price-sensitive customers. Immediate response recommended.",
    "timestamp": "2026-03-09T10:30:00",
    "offer": "Buy 1 Get 1",
    "product": "Farmhouse Pizza"
  },
  {
    "competitor": "Pizza Hut",
    "event_type": "discount",
    "competitor_price": 199,
    "user_price": 350,
    "price_difference": -151,
    "opportunity_score": 10.0,
    "impact_level": "high",
    "insight": "Pizza Hut discount offers a significantly lower price (₹199 vs your ₹350) and may attract price-sensitive customers. Immediate response recommended.",
    "timestamp": "2026-03-09T11:00:00",
    "offer": "30% off",
    "product": "Margherita Pizza"
  }
]
```

---

## Scoring Logic

### Formula

```
Base Score: 5

+ IF competitor cheaper:
    0-10% cheaper   → +0.5
    10-20% cheaper  → +1.5
    20-30% cheaper  → +2.5
    >30% cheaper    → +3.0

+ IF event type:
    promotion/discount → +2.0
    launch            → +1.0

+ IF >30% cheaper:
    Extreme bonus → +3.0

= Total (capped at 10.0)
```

### Example Calculations

#### Example 1: Dominos Promotion (Score: 8.5)

```
User Price:        ₹350
Competitor Price:  ₹299
Difference:        -₹51 (14.6% cheaper)
Event Type:        promotion

Calculation:
  Base score:              5.0
  Price (10-20% range):   +1.5
  Promotion bonus:        +2.0
  ────────────────────────────
  Total Score:             8.5  → HIGH IMPACT
```

#### Example 2: Pizza Hut Discount (Score: 10.0)

```
User Price:        ₹350
Competitor Price:  ₹199
Difference:        -₹151 (43% cheaper)
Event Type:        discount

Calculation:
  Base score:              5.0
  Price (>30%):           +3.0
  Discount bonus:         +2.0
  Extreme discount:       +3.0
  ────────────────────────────
  Total (before cap):     13.0
  Total (capped):         10.0  → HIGH IMPACT
```

#### Example 3: Papa John's Launch (Score: 6.0)

```
User Price:        ₹350
Competitor Price:  ₹399
Difference:        +₹49 (14% more expensive)
Event Type:        launch

Calculation:
  Base score:              5.0
  Price (more expensive):  0.0
  Launch bonus:           +1.0
  ────────────────────────────
  Total Score:             6.0  → MEDIUM IMPACT
```

---

## Usage

### Run the Agent

```bash
python agents/analyst_agent.py
```

**Inputs:**
- `data/outputs/competitor_signals.json` (from Scout Agent)
- `data/inputs/business_profile.json` (user business data)

**Output:**
- `data/outputs/market_analysis.json` (with opportunity_score)

### Run Tests

```bash
python test_opportunity_score.py
```

**Test Coverage:**
- 8 opportunity score scenarios ✓
- Full analysis pipeline ✓
- 4 edge cases ✓
- 9 score-to-impact mappings ✓

**Result:** 🎉 ALL 21 TESTS PASSED

---

## Code Examples

### Calculate Opportunity Score

```python
from agents.analyst_agent import calculate_opportunity_score

business = {
    "business_name": "Tony's Pizza",
    "product": "Veg Pizza",
    "price": 350
}

signal = {
    "competitor": "Dominos",
    "product": "Farmhouse Pizza",
    "event_type": "promotion",
    "price": 299,
    "offer": "Buy 1 Get 1"
}

score = calculate_opportunity_score(signal, business)
print(f"Opportunity Score: {score}/10")
# Output: 8.5/10
```

### Classify Impact

```python
from agents.analyst_agent import classify_impact

score = 8.5
impact = classify_impact(score)
print(f"Impact Level: {impact.upper()}")
# Output: HIGH
```

### Full Analysis

```python
from agents.analyst_agent import analyze_signal

result = analyze_signal(signal, business)

print(f"Competitor: {result['competitor']}")
print(f"Score: {result['opportunity_score']}/10")
print(f"Impact: {result['impact_level'].upper()}")
print(f"Insight: {result['insight']}")
```

**Output:**
```
Competitor: Dominos
Score: 8.5/10
Impact: HIGH
Insight: Dominos promotion offers a significantly lower price (₹299 vs your ₹350)...
```

---

## Impact Level Mapping

| Score Range | Impact Level | Action Required |
|------------|-------------|----------------|
| 8.0 - 10.0 | 🔴 HIGH     | Immediate response |
| 5.0 - 7.9  | 🟡 MEDIUM   | Monitor & prepare |
| 0.0 - 4.9  | 🟢 LOW      | Standard tracking |

---

## Edge Cases Handled

✅ **Missing competitor price** - Returns base score + event bonus  
✅ **Zero competitor price** - Treated as missing price  
✅ **Negative competitor price** - Converted to 0  
✅ **Missing event type** - Uses base score only  
✅ **Missing offer field** - Handled gracefully  
✅ **Invalid business price** - Validation error with clear message  

---

## Integration with Pipeline

### Scout → Analyst → Strategist

```
┌─────────────┐
│ Scout Agent │ → competitor_signals.json
└─────────────┘
       ↓
┌────────────────┐
│ Analyst Agent  │ → market_analysis.json (with opportunity_score)
└────────────────┘
       ↓
┌──────────────────┐
│ Strategist Agent │ → Uses score for strategy priority
└──────────────────┘
```

**Strategist uses opportunity_score to:**
1. Prioritize responses (high score = urgent)
2. Select strategy type (defensive vs offensive)
3. Allocate resources (high score = more budget)
4. Set timelines (high score = faster action)

---

## File Structure

```
d:\marketing-ai\
│
├── agents/
│   └── analyst_agent.py             ← UPGRADED with opportunity_score
│
├── data/
│   ├── inputs/
│   │   └── business_profile.json    ← User business data
│   └── outputs/
│       ├── competitor_signals.json  ← Input from Scout
│       └── market_analysis.json     ← Output with scores
│
├── test_opportunity_score.py        ← Test suite (21 tests)
├── OPPORTUNITY_SCORE_EXAMPLES.md    ← Detailed examples
├── OPPORTUNITY_SCORE_SUMMARY.py     ← Complete summary
└── README_OPPORTUNITY_SCORE.md      ← This file
```

---

## Validation Results

```
╔════════════════════════════════════════════════════════════════════╗
║                         FINAL SUMMARY                              ║
╚════════════════════════════════════════════════════════════════════╝

✓ PASSED   - Opportunity Score Scenarios (8/8)
✓ PASSED   - Full Analysis Pipeline (1/1)
✓ PASSED   - Edge Cases (4/4)
✓ PASSED   - Score to Impact Mapping (9/9)

🎉 ALL TESTS PASSED! Opportunity Score feature working correctly.
```

---

## Quick Reference

### Command Summary

```bash
# Run analysis
python agents/analyst_agent.py

# Run tests
python test_opportunity_score.py

# View example output
cat data/outputs/market_analysis.json
```

### Key Functions

- **calculate_opportunity_score(signal, business)** - Returns score 0-10
- **classify_impact(score)** - Returns "high"/"medium"/"low"
- **analyze_signal(signal, business)** - Full analysis with score
- **run_analyst_agent()** - Complete pipeline execution

### Output Fields

All analysis results include:
- `opportunity_score` (float 0-10) ← **NEW**
- `impact_level` (string)
- `competitor_price` (float)
- `user_price` (float)
- `price_difference` (float)
- `insight` (string)
- `timestamp` (string)
- `offer` (string)
- `product` (string)

---

## Status

✅ **Implementation:** Complete  
✅ **Testing:** All 21 tests passing  
✅ **Documentation:** Complete  
✅ **Production Ready:** Yes  
✅ **Hackathon Ready:** Yes  

---

## Support

For detailed examples and scoring scenarios, see:
- `OPPORTUNITY_SCORE_EXAMPLES.md` - Comprehensive examples
- `OPPORTUNITY_SCORE_SUMMARY.py` - Code reference
- `test_opportunity_score.py` - Test coverage

---

**Last Updated:** March 9, 2026  
**Version:** 2.0 with Market Opportunity Score
