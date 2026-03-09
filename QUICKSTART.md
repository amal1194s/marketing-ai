# 🚀 ScoutIQ - Quick Start Guide

Get started with the ScoutIQ multi-agent system in 5 minutes!

---

## System Overview

ScoutIQ = **Scout Agent** (collects data) + **Analyst Agent** (analyzes threats)

```
Scout → competitor_signals.json → Analyst → market_analysis.json
```

---

## Part 1: Scout Agent - Data Collection

### Step 1: Installation

```bash
cd marketing-ai
pip install -r requirements.txt
```

### Step 2: Run Scout Demo

```bash
python main.py
```

**Expected Output:**
- ✅ 4 competitor signals extracted
- ✅ Events detected: promotions, discounts, new products
- ✅ Signals saved to `data/outputs/competitor_signals.json`

### Step 3: Scout Code Example

```python
from agents.scout_agent import ScoutAgent

agent = ScoutAgent()

# Process text
text = "Dominos launched Buy 1 Get 1 offer on Pizza at ₹299"
signals = agent.process_text(text, "Dominos", "website")

# Export
agent.export_signals("data/outputs/competitor_signals.json")
```

---

## Part 2: Analyst Agent - Threat Analysis

### Step 1: Setup Business Profile

Create `data/inputs/business_profile.json`:

```json
{
  "business_name": "Tony's Pizza",
  "product": "Veg Pizza",
  "price": 350,
  "location": "Coimbatore"
}
```

### Step 2: Run Analyst Agent

```bash
python agents/analyst_agent.py
```

**Expected Output:**
```
🔬 Analyzing competitor signals...
  1. 🔴 Dominos - Score: 8.5/10 (HIGH Impact)
  2. 🔴 Pizza Hut - Score: 10.0/10 (HIGH Impact)
  3. 🟡 Papa John's - Score: 6.0/10 (MEDIUM Impact)

Impact Summary:
  🔴 High: 2
  🟡 Medium: 1
```

### Step 3: Analyst Code Example

```python
from agents.analyst_agent import run_analyst_agent, calculate_opportunity_score

# Run full analysis
results = run_analyst_agent()

# Review high-priority threats
high_threats = [r for r in results if r['opportunity_score'] >= 8]
for threat in high_threats:
    print(f"{threat['competitor']}: {threat['opportunity_score']}/10")
    print(f"→ {threat['insight']}")
```

---

## Complete Pipeline Example

```python
# Step 1: Scout collects data
from agents.scout_agent import ScoutAgent

scout = ScoutAgent()
scout.process_text("Dominos BOGO at ₹299", "Dominos", "website")
scout.export_signals("data/outputs/competitor_signals.json")

# Step 2: Analyst analyzes
from agents.analyst_agent import run_analyst_agent

results = run_analyst_agent()

# Step 3: Review results
for r in results:
    if r['opportunity_score'] >= 8:
        print(f"⚠️ HIGH THREAT: {r['competitor']} - {r['insight']}")
```

---

## Understanding Opportunity Scores

### Scoring System (0-10)

| Score | Meaning | Action |
|-------|---------|--------|
| 8-10  | 🔴 HIGH | Immediate action needed |
| 5-7   | 🟡 MEDIUM | Monitor & prepare |
| 0-4   | 🟢 LOW | Standard tracking |

### Score Calculation

```
Base: 5
+ Price advantage (if cheaper): up to +3
+ Event bonus (promo/discount): +2
+ Extreme discount (>30%): +3
= Total (max 10)
```

### Example Scenarios

**Scenario 1: Aggressive Promo (Score 8.5)**
- Competitor: ₹299 | You: ₹350 (15% cheaper)
- Event: promotion
- Score: 5 + 1.5 (price) + 2 (promo) = 8.5 → HIGH

**Scenario 2: Deep Discount (Score 10)**
- Competitor: ₹199 | You: ₹350 (43% cheaper)
- Event: discount
- Score: 5 + 3 + 2 + 3 (extreme) = 13 → 10 (capped) → HIGH

**Scenario 3: Premium Launch (Score 6)**
- Competitor: ₹399 | You: ₹350 (more expensive)
- Event: launch
- Score: 5 + 0 (no advantage) + 1 (launch) = 6 → MEDIUM

---

## Running Tests

### Scout Agent Tests
```bash
python -m pytest tests/ -v
```

### Analyst Agent Tests
```bash
python test_opportunity_score.py
```

**Result:** ✅ All tests passing (21/21 for Analyst)

---

## File Locations

### Input Files
- `data/inputs/business_profile.json` - Your business data (for Analyst)
- `data/inputs/sample_competitor_data.json` - Sample data (for Scout)

### Output Files
- `data/outputs/competitor_signals.json` - Scout output → Analyst input
- `data/outputs/market_analysis.json` - Analyst output with scores

---

## Common Use Cases

### Use Case 1: Daily Monitoring
```bash
# Morning: Scout collects overnight data
python main.py

# Review: Analyst generates threat report
python agents/analyst_agent.py

# Action: Focus on HIGH impact signals (score ≥ 8)
```

### Use Case 2: Competitive Intelligence
```python
# Filter by competitor
from agents.scout_agent import ScoutAgent
agent = ScoutAgent()
dominos_signals = agent.get_signals_by_competitor("Dominos")

# Analyze specific competitor
from agents.analyst_agent import analyze_signal
business = {"price": 350}
for signal in dominos_signals:
    result = analyze_signal(signal, business)
    print(f"Score: {result['opportunity_score']}/10")
```

### Use Case 3: Alert System
```python
# Monitor high threats
results = run_analyst_agent()
high_threats = [r for r in results if r['opportunity_score'] >= 8]

if high_threats:
    print(f"⚠️ ALERT: {len(high_threats)} high-priority threats detected!")
    for threat in high_threats:
        print(f"  • {threat['competitor']}: {threat['insight']}")
```

---

## Tips for Best Results

### For Scout Agent
✅ Provide clear, structured text  
✅ Specify accurate competitor names  
✅ Include pricing information when available  
✅ Process data in batches for efficiency  

### For Analyst Agent
✅ Keep business profile updated  
✅ Review HIGH impact signals first  
✅ Consider score + insight together  
✅ Run analysis after new signals collected  

---

## Troubleshooting

**Issue: No signals detected**
- Check input file format
- Verify text contains competitor info
- Ensure pricing is extractable

**Issue: All scores are MEDIUM**
- Check if business price is set correctly
- Verify competitor prices are different
- Review event types in signals

**Issue: Import errors**
- Run `pip install -r requirements.txt`
- Check Python version (3.8+)
- Verify file paths are correct

---

## Next Steps

1. ✅ **Customize Business Profile** - Update price, location, products
2. ✅ **Add More Competitors** - Monitor 3-5 direct competitors
3. ✅ **Set Up Automation** - Schedule daily monitoring
4. ✅ **Integrate with Tools** - Connect to dashboards, alerts
5. ⏳ **Wait for Strategist** - Coming soon for action recommendations

---

## Need Help?

- 📖 **Full Documentation**: README.md
- 📊 **Scoring Guide**: README_OPPORTUNITY_SCORE.md
- 💡 **Examples**: OPPORTUNITY_SCORE_EXAMPLES.md
- 🧪 **Tests**: `test_opportunity_score.py`

---

**Ready to go?**

```bash
# Quick test
python agents/analyst_agent.py

# Full pipeline
python main.py && python agents/analyst_agent.py
```

---

**System Status:** 🟢 Production Ready  
**Last Updated:** March 9, 2026  
**Version:** Scout v1.0 | Analyst v2.0
