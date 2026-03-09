# Agent B Quick Reference

## Installation
No installation needed - pure Python with standard library only.

## Quick Start

```python
from agent_b_analyst import AgentBAnalyst
import json

agent = AgentBAnalyst()
result_json = agent.analyze(business_profile, competitor_findings)
result = json.loads(result_json)
```

## Input Format

### Business Profile
```json
{
  "name": "Your Business Name",
  "pricing": {
    "average_price": 10.00,
    "min_price": 5.00,
    "max_price": 15.00
  },
  "products": ["Product A", "Product B"],
  "target_audience": {
    "demographics": ["millennials", "professionals"],
    "interests": ["quality", "value"]
  },
  "positioning": "Your unique value proposition"
}
```

### Competitor Findings
```json
{
  "competitors": [
    {
      "name": "Competitor Name",
      "pricing": {
        "average_price": 8.00,
        "min_price": 5.00,
        "max_price": 12.00
      },
      "promotions": ["20% off sale", "Loyalty program"],
      "new_offers": ["Student discount"],
      "new_products": ["New product line"],
      "bundles": ["Value bundle"],
      "target_audience": {
        "demographics": ["millennials"],
        "interests": ["convenience"]
      },
      "positioning": "Fast and affordable"
    }
  ]
}
```

## Output Fields

| Field | Type | Values | Description |
|-------|------|--------|-------------|
| `impact_level` | string | low, medium, high | Overall competitive pressure |
| `summary` | string | - | Executive summary with key facts |
| `pricing_gap` | string | - | Detailed pricing analysis |
| `market_risk` | string | - | Customer loss risk assessment |
| `recommended_urgency` | string | low, medium, high | Response timeframe |
| `key_insights` | array | - | Top 3 strategic insights |
| `price_difference_percent` | number/null | - | **NEW:** Percent difference vs competitors (positive=expensive, negative=cheaper, null=no data) |

## Interpreting Results

### Price Difference Percent (NEW)
- **Positive value** (e.g., +15.79): You're 15.79% more expensive than market average
- **Negative value** (e.g., -25.5): You're 25.5% cheaper than market average
- **Near zero** (e.g., 0.5): Within 0.5% of market average - competitive pricing
- **null**: No pricing data available for comparison

**Strategic Implications:**
- `> 20%`: High risk, consider price adjustments or justify premium
- `10-20%`: Moderate concern, emphasize value proposition
- `Within ±10%`: Competitive range, maintain positioning
- `< -10%`: Price advantage, leverage in marketing

### Impact Levels
- **high**: Significant threat, immediate action needed
- **medium**: Notable activity, prepare response
- **low**: Minimal threat, maintain strategy

### Urgency Levels
- **high**: Respond within 48-72 hours
- **medium**: Respond within 1-2 weeks
- **low**: Monitor monthly

### Pricing Position
Automatically detected in analysis:
- **highest**: Most expensive option
- **above_average**: Premium pricing
- **at_average**: Competitive
- **below_average**: Value pricing
- **lowest**: Most affordable

### Offer Types
Automatically classified:
- **discount**: % off, sales
- **bogo**: Buy one get one
- **loyalty**: Rewards programs
- **bundle**: Package deals
- **free**: Complimentary offers
- **subscription**: Monthly/recurring
- **segment_discount**: Student/senior/military

## Key Improvements in v2

### 1. More Specific Insights
```
Before: "High pricing risk"
After:  "CRITICAL: You're 22.1% more expensive than market average ($4.50). 
         Risk of losing price-sensitive customers to Chain Coffee Co."
```

### 2. Competitor Names
All insights include specific competitor names:
- "MegaChain Coffee is cheapest at $3.75"
- "5 promotions from 2 competitors"

### 3. Action Timeframes
Every insight includes when to act:
- "Response needed within 48-72 hours"
- "Schedule product review within 2 weeks"
- "Monitor sales data daily"

### 4. Strategic Context
Explains WHY something matters:
- "Price-sensitive customers may switch"
- "Your offerings may appear stale"
- "Direct competition for same customers"

## Common Use Cases

### Price Comparison
```python
# Automatically detects:
# - Your position vs market
# - Cheapest competitor
# - Most expensive competitor  
# - Strategic implications
```

### Promotion Detection
```python
# Automatically identifies:
# - BOGO offers (50% off, buy 1 get 1)
# - High discounts (30%+)
# - Free offers
# - Time-sensitive deals
```

### Risk Assessment
```python
# Evaluates:
# - Customer overlap
# - Price disadvantage
# - Aggressive promotions
# - Provides action steps
```

## Error Handling

Agent B v2 is bulletproof:

```python
# All these return valid JSON:
agent.analyze({}, {})                        # Empty
agent.analyze(None, None)                    # None values
agent.analyze({"pricing": "bad"}, {...})     # Wrong types
agent.analyze(business, {"competitors": []}) # No data
```

## Testing

```bash
# Quick test
python test_agent_b.py

# High competition
python demo_high_competition.py

# Edge cases
python test_edge_cases.py

# Full demonstration
python demo_comprehensive.py
```

## Tips for Best Results

### 1. Complete Data
Provide all fields when available:
- Average, min, and max prices
- Full competitor lists
- Target audience details

### 2. Regular Analysis
Run analysis:
- Weekly in competitive markets
- Monthly in stable industries
- Immediately when competitors launch promotions

### 3. Act on Insights
Insights are prioritized by urgency:
1. First insight = highest priority
2. Second insight = medium priority
3. Third insight = important but less urgent

### 4. Track Over Time
Compare analyses month-over-month:
- Are threats increasing?
- Is your position improving?
- Are new competitors emerging?

## Integration

### With Scout Agent (Future)
```python
# Scout collects data
competitor_data = scout.collect()

# Analyst evaluates impact
analysis = analyst.analyze(business, competitor_data)

# Strategist recommends actions
actions = strategist.recommend(analysis)
```

### With APIs
```python
# As REST endpoint
@app.post("/analyze")
def analyze_competitors(request):
    result = agent.analyze(
        request.business_profile,
        request.competitor_findings
    )
    return JSONResponse(result)
```

### With Databases
```python
# Store results
analysis = agent.analyze(business, competitors)
db.save("analysis_history", {
    "timestamp": datetime.now(),
    "analysis": json.loads(analysis),
    "business_id": business_id
})
```

## Support

- **Documentation**: README.md
- **Improvements**: IMPROVEMENTS.md  
- **Quick Start**: QUICKSTART.md
- **Examples**: example_*.json files

## Version

**Agent B v2** - Production Ready ✅
- Strategic analysis
- Automatic detection
- Always valid JSON
- Comprehensive testing
