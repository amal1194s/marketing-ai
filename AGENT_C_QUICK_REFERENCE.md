# Agent C: The Strategist - Quick Reference

## 30-Second Overview

Agent C takes competitive analysis and generates **actionable business strategy** with **ready-to-use marketing content**.

**Input:** Business profile + Scout findings + Analyst report  
**Output:** Action plan + Pricing guidance + Marketing post + CTA + Steps + Rationale

## Minimal Usage Example

```python
from agent_c_strategist import AgentCStrategist
import json

# Initialize
strategist = AgentCStrategist()

# Prepare inputs (minimal required data)
business = {"name": "Mike's Pizza", "business_type": "pizza"}
scout = {"competitors": []}  # Can be empty
analyst = {
    "impact_level": "medium",
    "price_difference_percent": 10,
    "threat_score": 6.0,
    "key_insights": []
}

# Generate strategy
result = strategist.strategize(business, scout, analyst)

# Use result
strategy = json.loads(result)
print(strategy["marketing_post"])  # Ready to post!
```

## Four Strategy Types

| Type | When Used | Action |
|------|-----------|--------|
| **hold_position** | Competitive pricing, low threat | Maintain current strategy |
| **promotion_response** | Competitor promotions active | Launch counter-promotion |
| **price_adjustment** | Much more expensive (>20%) | Reduce prices tactically |
| **product_differentiation** | Unique strengths available | Emphasize quality/service |

## Output Fields

```javascript
{
  "recommended_action": "One clear summary",      // Main recommendation
  "response_type": "promotion_response",          // Strategy type
  "price_action": "Keep prices, launch promo",    // Pricing guidance
  "campaign_idea": "Flash Sale Alert",            // Campaign name
  "marketing_post": "🔥 FLASH SALE...",          // Copy & paste post
  "cta": "Claim discount now!",                   // Call to action
  "execution_steps": [...],                       // 3-5 action items
  "why_this_strategy": [...]                      // 2-4 reasons
}
```

## Decision Logic Cheat Sheet

```
Price diff >20% + Threat >7 → price_adjustment
Promotions + Price diff ≤15% → promotion_response
Unique strengths + Price ≤10% → product_differentiation
Threat <5 + Price ≤10% → hold_position
Otherwise → promotion_response (default)
```

## Common Patterns

### Pattern 1: Price War
```python
analyst = {
    "price_difference_percent": 30,
    "threat_score": 8.5,
    "impact_level": "high"
}
# → Returns: price_adjustment with reduction recommendation
```

### Pattern 2: Promo Battle
```python
analyst = {
    "price_difference_percent": 8,
    "threat_score": 6.5,
    "key_insights": ["Competitor promotions active"]
}
# → Returns: promotion_response with campaign idea
```

### Pattern 3: Premium Brand
```python
business = {
    "name": "Artisan Pizza",
    "unique_selling_points": ["Organic ingredients", "Chef-crafted"]
}
analyst = {"price_difference_percent": 25, "threat_score": 5.5}
# → Returns: product_differentiation with quality messaging
```

## Testing

```bash
# Run all tests
python test_agent_c.py

# Run demos
python demo_strategist.py

# See full pipeline
python integration_example.py
```

## Key Files

- `agent_c_strategist.py` - Main implementation
- `AGENT_C_README.md` - Full documentation
- `test_agent_c.py` - 12 test cases
- `demo_strategist.py` - 4 scenario demos
- `integration_example.py` - Full pipeline example

## Tips

✅ **DO:**
- Provide complete business profile for best results
- Use analyst's response_type suggestion if available
- Customize marketing posts to match brand voice
- Run tests after any modifications

❌ **DON'T:**
- Expect perfect results with minimal data
- Skip the rationale section (it explains "why")
- Forget to handle the JSON output properly
- Use this for enterprise-level strategy

## Emergency Troubleshooting

### Problem: Import error
```bash
# Make sure you're in the right directory
cd d:\marketing-ai
python -c "from agent_c_strategist import AgentCStrategist; print('OK')"
```

### Problem: Invalid output
```python
# Enable error checking
result = strategist.strategize(business, scout, analyst)
data = json.loads(result)
if data.get("error"):
    print(f"Error: {data['message']}")
```

### Problem: Wrong strategy type
```python
# Override by setting response_type in analyst_output
analyst["response_type"] = "price_adjustment"  # Force this strategy
```

## Performance

- **Speed:** < 100ms typical
- **Memory:** < 5MB
- **Dependencies:** None (stdlib only)
- **Python:** 3.7+

## Integration Checklist

- [ ] Import AgentCStrategist
- [ ] Prepare business_profile dict
- [ ] Get scout_findings from Agent A
- [ ] Get analyst_output from Agent B
- [ ] Call strategist.strategize()
- [ ] Parse JSON result
- [ ] Display in dashboard UI
- [ ] Let user execute recommendations

## One-Liner Examples

```python
# Simplest possible usage
json.loads(AgentCStrategist().strategize({}, {}, {}))

# With error handling
try: strategy = json.loads(strategist.strategize(b, s, a))
except: strategy = {"error": "Failed to generate strategy"}

# Direct field access
action = json.loads(result)["recommended_action"]
```

## Quick Validation

```python
# Verify output has all required fields
required = ["recommended_action", "response_type", "price_action", 
            "campaign_idea", "marketing_post", "cta", 
            "execution_steps", "why_this_strategy"]

strategy = json.loads(result)
assert all(field in strategy for field in required), "Missing fields!"
```

## Support

- **Docs:** See AGENT_C_README.md
- **Tests:** Run test_agent_c.py
- **Examples:** Run demo_strategist.py
- **Integration:** See integration_example.py

---

**Version:** 2.0  
**Status:** ✅ Production Ready  
**Last Updated:** March 10, 2026
