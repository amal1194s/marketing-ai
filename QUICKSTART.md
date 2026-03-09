# Agent B: Quick Start Guide

## Running the Agent

### Option 1: Test with Example Data
```bash
python test_agent_b.py
```
This runs a formatted test with the example coffee shop scenario.

### Option 2: Use in Your Code
```python
from agent_b_analyst import AgentBAnalyst
import json

agent = AgentBAnalyst()

# Your business data
business_profile = {
    "name": "My Business",
    "pricing": {
        "average_price": 50.00,
        "min_price": 30.00,
        "max_price": 80.00
    },
    "products": ["Product A", "Product B"],
    "target_audience": {
        "demographics": ["millennials", "professionals"],
        "interests": ["sustainability", "quality"]
    },
    "positioning": "Premium eco-friendly products"
}

# Competitor data (from Scout Agent)
competitor_findings = {
    "competitors": [
        {
            "name": "Competitor X",
            "pricing": {"average_price": 40.00},
            "promotions": ["20% off sale"],
            "new_products": ["New product line"],
            "target_audience": {
                "demographics": ["millennials"],
                "interests": ["value", "convenience"]
            },
            "positioning": "Affordable quality"
        }
    ]
}

# Analyze
result = agent.analyze(business_profile, competitor_findings)
print(result)
```

## Understanding the Output

### Impact Levels
- **High**: Significant competitive threat - immediate action needed
- **Medium**: Notable competitive activity - monitor and prepare
- **Low**: Minimal threat - maintain current strategy

### Urgency Levels
- **High**: Respond within days - competitors taking aggressive action
- **Medium**: Respond within weeks - strategic adjustment recommended
- **Low**: Monitor situation - no immediate action required

## What the Agent Analyzes

### 1. Pricing Gap
Compares your average price to competitors:
- \>20% higher = HIGH risk
- 10-20% higher = MEDIUM risk
- Within 10% = Competitive
- Lower than competitors = Advantage

### 2. Competitor Promotions
Tracks aggressive offers:
- BOGO (Buy One Get One)
- 30%+ discounts
- Multiple simultaneous promotions
- New loyalty programs

### 3. Product Innovation
Monitors new competitive offerings:
- New product launches
- Bundle deals
- Limited edition items
- Seasonal offerings

### 4. Audience Overlap
Measures how much your customers overlap with competitors:
- High overlap = direct competition
- Low overlap = distinct market segment

### 5. Market Positioning
Evaluates how unique your value proposition is:
- Weak differentiation = similar to competitors
- Strong differentiation = clear unique value

## Example Scenarios

### Scenario 1: Price War
**Input**: Competitor drops prices 30%  
**Output**: High impact, high urgency, pricing gap warning  
**Action**: Consider matching, bundling, or value messaging

### Scenario 2: New Product Launch
**Input**: Competitor launches 5 new products  
**Output**: Medium-high impact, product innovation alert  
**Action**: Evaluate if product refresh needed

### Scenario 3: Aggressive Promotion
**Input**: Competitor runs BOGO + 40% off  
**Output**: High urgency, promotion threat identified  
**Action**: Counter with promotion or emphasize quality

### Scenario 4: Stable Market
**Input**: Minor competitive activity  
**Output**: Low impact, low urgency  
**Action**: Maintain strategy, focus on retention

## Tips for Best Results

### Provide Complete Data
- Include all pricing tiers (min, max, average)
- List key products and services
- Define target audience clearly
- State your unique positioning

### Keep Data Current
- Update pricing monthly
- Track new competitor promotions weekly
- Monitor product launches immediately

### Use Consistent Format
- Follow the JSON structure exactly
- Use numeric values for prices
- Use arrays for lists
- Use strings for descriptions

### Interpret Insights
- Don't panic at "high" impact - read the details
- Consider your business context
- Balance cost of action vs. risk of inaction
- Use insights to inform, not dictate, strategy

## Common Questions

**Q: What if I don't have competitor pricing data?**  
A: The agent will still analyze promotions, products, and positioning. Pricing analysis will be skipped.

**Q: How many competitors should I track?**  
A: Focus on 3-5 direct competitors for meaningful analysis.

**Q: What if analysis says "high impact" but I disagree?**  
A: The agent uses objective criteria. Consider if you have additional context (brand loyalty, location advantage, etc.).

**Q: Can I customize the weighting of factors?**  
A: Currently no, but this is planned for future versions. Pricing and promotions are weighted more heavily.

**Q: How often should I run analysis?**  
A: Weekly for fast-moving markets, monthly for stable industries.

## Need Help?

- Check the example files for proper data format
- Review README.md for detailed documentation
- Test with the provided examples first
- Ensure your JSON is valid (use a JSON validator)

---

**Ready to analyze?** Run `python test_agent_b.py`
