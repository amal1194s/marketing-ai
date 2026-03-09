# Market Opportunity Score - Examples & Logic

## Scoring Formula

```
Base Score: 5

+ Price Advantage (if competitor cheaper):
  - 0-10% cheaper:   +0.5
  - 10-20% cheaper:  +1.5
  - 20-30% cheaper:  +2.5
  - >30% cheaper:    +3.0

+ Event Type Bonus:
  - promotion/discount: +2.0
  - launch:            +1.0

+ Extreme Discount Bonus:
  - If >30% cheaper:   +3.0 (additional)

Maximum Score: 10
Minimum Score: 0
```

## Impact Level Mapping

| Score Range | Impact Level |
|-------------|--------------|
| 8 - 10      | HIGH         |
| 5 - 7       | MEDIUM       |
| 0 - 4       | LOW          |

---

## Example Scenarios

### 1. High Impact - Aggressive Promotion (Score: 8.5/10)

**Scenario:**
- **Competitor:** Dominos
- **User Price:** ₹350
- **Competitor Price:** ₹299
- **Event Type:** promotion
- **Offer:** Buy 1 Get 1

**Calculation:**
```
Base Score:              5.0
Price difference:        -51 (14.6% cheaper)
  → 10-20% range:       +1.5
Event type (promotion):  +2.0
─────────────────────────────
Total Score:             8.5 → HIGH IMPACT
```

**Insight:**
> "Dominos promotion offers a significantly lower price (₹299 vs your ₹350) and may attract price-sensitive customers. Immediate response recommended."

---

### 2. Extreme High Impact - Deep Discount (Score: 10/10)

**Scenario:**
- **Competitor:** Pizza Hut
- **User Price:** ₹350
- **Competitor Price:** ₹199
- **Event Type:** discount
- **Offer:** 30% off

**Calculation:**
```
Base Score:              5.0
Price difference:        -151 (43% cheaper)
  → >30% cheaper:       +3.0
Event type (discount):   +2.0
Extreme discount bonus:  +3.0 (>30%)
─────────────────────────────
Total (capped):          10.0 → HIGH IMPACT
```

**Insight:**
> "Pizza Hut discount offers a significantly lower price (₹199 vs your ₹350) and may attract price-sensitive customers. Immediate response recommended."

---

### 3. Medium Impact - Premium Launch (Score: 6/10)

**Scenario:**
- **Competitor:** Papa John's
- **User Price:** ₹350
- **Competitor Price:** ₹399
- **Event Type:** launch
- **Offer:** New product launch

**Calculation:**
```
Base Score:              5.0
Price difference:        +49 (more expensive)
  → No price bonus:      0.0
Event type (launch):     +1.0
─────────────────────────────
Total Score:             6.0 → MEDIUM IMPACT
```

**Insight:**
> "Papa John's launch creates market movement. Evaluate if product refresh or promotional response is needed."

---

### 4. Medium Impact - Moderate Price (Score: 7.5/10)

**Scenario:**
- **Competitor:** Local Pizza Co
- **User Price:** ₹350
- **Competitor Price:** ₹249
- **Event Type:** price_update
- **Offer:** (none)

**Calculation:**
```
Base Score:              5.0
Price difference:        -101 (28.9% cheaper)
  → 20-30% range:       +2.5
Event type (standard):    0.0
─────────────────────────────
Total Score:             7.5 → MEDIUM IMPACT
```

**Insight:**
> "Local Pizza Co is moderately cheaper (₹101 difference) with price_update. Notable competitive activity that warrants monitoring and potential response."

---

### 5. Low Impact - Higher Price (Score: 5/10)

**Scenario:**
- **Competitor:** Premium Pizza
- **User Price:** ₹350
- **Competitor Price:** ₹450
- **Event Type:** standard
- **Offer:** (none)

**Calculation:**
```
Base Score:              5.0
Price difference:        +100 (more expensive)
  → No price bonus:      0.0
Event type (standard):    0.0
─────────────────────────────
Total Score:             5.0 → MEDIUM IMPACT
```

---

### 6. Edge Case - Missing Price (Score: 7/10)

**Scenario:**
- **Competitor:** Mystery Competitor
- **User Price:** ₹350
- **Competitor Price:** 0 (missing)
- **Event Type:** promotion
- **Offer:** Special deal

**Calculation:**
```
Base Score:              5.0
Price difference:        N/A (invalid price)
  → No price bonus:      0.0
Event type (promotion):  +2.0
─────────────────────────────
Total Score:             7.0 → MEDIUM IMPACT
```

---

## Score Distribution Examples

### Competitive Market Analysis

| Competitor      | Price | Event    | Score | Impact |
|----------------|-------|----------|-------|--------|
| Dominos        | ₹299  | promo    | 8.5   | 🔴 HIGH |
| Pizza Hut      | ₹199  | discount | 10.0  | 🔴 HIGH |
| Papa John's    | ₹399  | launch   | 6.0   | 🟡 MED  |
| Local Pizza Co | ₹249  | price    | 7.5   | 🟡 MED  |

**Average Score:** 8.0/10  
**Market Threat Level:** HIGH

---

## Usage Examples

### Python Code

```python
from agents.analyst_agent import calculate_opportunity_score, classify_impact

# Business profile
business = {
    "business_name": "Tony's Pizza",
    "product": "Veg Pizza",
    "price": 350
}

# Competitor signal
signal = {
    "competitor": "Dominos",
    "product": "Farmhouse Pizza",
    "event_type": "promotion",
    "price": 299,
    "offer": "Buy 1 Get 1"
}

# Calculate score
score = calculate_opportunity_score(signal, business)
print(f"Opportunity Score: {score}/10")  # 8.5/10

# Get impact level
impact = classify_impact(score)
print(f"Impact Level: {impact.upper()}")  # HIGH
```

### Command Line

```bash
# Run full analysis
python agents/analyst_agent.py

# Output:
# 🔴 Dominos - Score: 8.5/10 (HIGH Impact)
# 🔴 Pizza Hut - Score: 10.0/10 (HIGH Impact)
# 🟡 Papa John's - Score: 6.0/10 (MEDIUM Impact)
# 🟡 Local Pizza Co - Score: 7.5/10 (MEDIUM Impact)
```

---

## Strategic Interpretation

### High Score (8-10): Immediate Action Required
- Competitor poses serious threat
- Consider: Price match, counter-promotion, value messaging
- Monitor customer response closely
- May require emergency strategy session

### Medium Score (5-7): Watch & Prepare
- Notable competitive activity
- Consider: Differentiation messaging, quality emphasis
- Prepare contingency responses
- Standard monitoring protocols

### Low Score (0-4): Monitor Only
- Minimal immediate threat
- Consider: Maintain current strategy
- Routine competitive tracking
- Focus on retention & quality

---

## Integration with Strategist Agent

The opportunity score flows into the Strategist Agent for action planning:

```
Analyst Output → Strategist Input
{
  "opportunity_score": 8.5,   ← Used for strategy priority
  "impact_level": "high",      ← Triggers response type
  "insight": "..."             ← Context for strategy
}
```

Strategist uses score to:
1. Prioritize responses (8-10 = urgent)
2. Select strategy type (defensive vs offensive)
3. Allocate resources (high score = more budget)
4. Set timelines (high score = faster action)

---

## Testing Different Scenarios

```bash
# Test with custom signals
python test_analyst_agent.py

# Run demo scenarios
python demo_analyst_scenarios.py
```

See `test_analyst_agent.py` for comprehensive testing examples.
