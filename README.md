# Marketing AI - Market Intelligence System

A multi-agent AI system for analyzing competitor activity and market intelligence for small businesses.

## Overview

This system uses multiple specialized agents to monitor competitors and provide strategic insights:

- **Agent A: The Scout** - Discovers and collects competitor data
- **Agent B: The Analyst** - Analyzes competitor impact on your business ✅ **IMPROVED**
- **Agent C: The Strategist** - Recommends actions based on analysis

## What's New in Agent B (v2)

🎯 **More Strategic** - Priority-ranked insights with specific actions and timeframes  
🔍 **Smarter Detection** - Automatically detects aggressive offers using advanced pattern matching  
💰 **Better Pricing Analysis** - Identifies cheapest/most expensive competitors with strategic context  
📊 **Clearer Insights** - Every insight includes specific numbers, competitor names, and recommendations  
🛡️ **Rock Solid** - Always returns valid JSON, handles all edge cases gracefully

[See detailed improvements →](IMPROVEMENTS.md)

## Agent B: The Analyst

### Purpose
Evaluates how competitor activity affects your business and identifies strategic risks and opportunities.

### What It Analyzes
- **Price Differences** - Compares your pricing against competitors
- **Promotions & Offers** - Identifies aggressive competitor promotions
- **Product Launches** - Tracks new products and bundles
- **Target Audience** - Measures customer overlap with competitors
- **Market Positioning** - Evaluates differentiation strength

### Impact Assessment
- **Impact Level**: low, medium, or high competitive pressure
- **Market Risk**: Likelihood of customer loss
- **Urgency**: How quickly you need to respond

## Usage

### Basic Example

```python
from agent_b_analyst import AgentBAnalyst
import json

# Initialize the agent
agent = AgentBAnalyst()

# Load your business profile
with open('example_business_profile.json', 'r') as f:
    business_profile = json.load(f)

# Load competitor findings (from Scout Agent)
with open('example_competitor_findings.json', 'r') as f:
    competitor_findings = json.load(f)

# Run analysis
result = agent.analyze(business_profile, competitor_findings)
print(result)
```

### Output Format

```json
{
  "impact_level": "medium",
  "summary": "Moderate competitive activity from 2 competitor(s)...",
  "pricing_gap": "Your prices are 18.2% higher than competitors...",
  "market_risk": "Moderate risk due to high competitive pressure...",
  "recommended_urgency": "medium",
  "key_insights": [
    "8 aggressive competitor promotions active",
    "You're 16% more expensive than market average",
    "Competitors launched 11 new products/bundles"
  ],
  "price_difference_percent": 18.2
}
```

**New Field:** `price_difference_percent` shows your price vs competitors:
- **Positive** (e.g., 15.79) = You're 15.79% more expensive
- **Negative** (e.g., -25.5) = You're 25.5% cheaper
- **Near zero** (e.g., 0.5) = Competitive pricing
- **null** = No pricing data available

## Input Formats

### Business Profile Structure

```json
{
  "name": "Your Business Name",
  "pricing": {
    "average_price": 5.50,
    "min_price": 3.00,
    "max_price": 8.00
  },
  "products": ["Product 1", "Product 2"],
  "target_audience": {
    "demographics": ["demographic1", "demographic2"],
    "interests": ["interest1", "interest2"]
  },
  "positioning": "Your unique value proposition"
}
```

### Competitor Findings Structure (from Scout Agent)

```json
{
  "competitors": [
    {
      "name": "Competitor Name",
      "pricing": {
        "average_price": 4.50
      },
      "promotions": ["Promotion 1", "Promotion 2"],
      "new_offers": ["New offer"],
      "new_products": ["Product 1"],
      "bundles": ["Bundle 1"],
      "target_audience": {
        "demographics": ["demo1", "demo2"],
        "interests": ["interest1", "interest2"]
      },
      "positioning": "Competitor's positioning statement"
    }
  ]
}
```

## Key Features

✅ **Strategic Analysis** - Priority-ranked insights with specific competitor names and numbers  
✅ **Automatic Detection** - Detects price gaps, aggressive offers, and market positioning automatically  
✅ **Risk Assessment** - Identifies threats with specific actions and timeframes  
✅ **Pricing Intelligence** - Compares against cheapest, most expensive, and average competitors  
✅ **Offer Classification** - Categorizes promotions (BOGO, discount, loyalty, bundle, etc.)  
✅ **Robust & Reliable** - Always returns valid JSON, handles all edge cases  
✅ **No Data Invention** - Only analyzes provided information  

## Design Principles

1. **No Guessing** - Analysis based only on provided data
2. **Small Business Focus** - Practical insights for limited resources
3. **Clear Communication** - Non-technical language
4. **Actionable Output** - Strategic recommendations, not just observations
5. **Risk-Aware** - Highlights threats and opportunities

## Testing

### Quick Test
Run the built-in example:
```bash
python test_agent_b.py
```

### High Competition Scenario
Test with aggressive competitive scenario:
```bash
python demo_high_competition.py
```

### Edge Cases & Robustness
Test error handling and edge cases:
```bash
python test_edge_cases.py
```

**All tests pass ✓** - Agent B handles empty data, malformed inputs, extreme values, and always returns valid JSON.

## Integration

Agent B is designed to work with:
- **Input**: Competitor data from Scout Agent (Agent A)
- **Output**: Analysis consumed by Strategist Agent (Agent C)

## Future Enhancements

- [ ] Historical trend analysis
- [ ] Sentiment analysis of competitor reviews
- [ ] Industry benchmark comparisons
- [ ] Seasonal pattern detection
- [ ] Custom weighting for analysis factors

## License

MIT License

## Current Status

✅ **Agent B: The Analyst** - COMPLETE & IMPROVED (v2)
- Strategic analysis with priority-ranked insights
- Automatic price and offer detection
- Always-valid JSON output
- Comprehensive edge case handling
- Production-ready

📋 **Next Steps:**
- Implement Agent A (Scout) - Data collection
- Implement Agent C (Strategist) - Action recommendations
- Build orchestrator to connect all agents

---

**Status**: Agent B v2 implementation complete and tested ✅  
**Ready for**: Integration with Scout and Strategist agents
