# Agent C: The Strategist

## Overview

Agent C is the final agent in the Multi-Agent Market Intelligence system. It takes competitive analysis and converts it into **practical, actionable business recommendations** with ready-to-use marketing content.

## What It Does

**Input:**
- Business profile (from system)
- Scout findings (from Agent A)
- Analyst output (from Agent B)

**Output:**
- Clear action recommendation
- Response strategy type
- Specific pricing guidance
- Campaign idea
- Ready-to-use marketing post
- Call-to-action (CTA)
- 3-5 execution steps
- Strategy rationale (3-4 reasons)

## Response Strategy Types

Agent C chooses one of four response strategies based on the competitive situation:

### 1. **hold_position**
- **When:** Pricing is competitive, low threat
- **Action:** Maintain current strategy, stay alert
- **Best for:** Stable market conditions

### 2. **promotion_response**
- **When:** Competitors are using promotions as main tactic
- **Action:** Launch limited-time promotion
- **Best for:** Quick competitive response without changing base prices

### 3. **price_adjustment**
- **When:** Significantly more expensive than competitors
- **Action:** Reduce prices or add value
- **Best for:** High price gap with high threat

### 4. **product_differentiation**
- **When:** Unique strengths justify premium pricing
- **Action:** Emphasize quality and unique features
- **Best for:** Avoiding price wars, maintaining margins

## Decision Logic

Agent C uses this logic to determine the best strategy:

```
IF price_diff > 20% AND threat_score >= 7
  → price_adjustment

ELSE IF promotions detected AND price_diff <= 15%
  → promotion_response

ELSE IF price_diff > 15% AND impact = high
  IF has unique strengths
    → product_differentiation
  ELSE
    → price_adjustment

ELSE IF unique strengths AND price_diff <= 10%
  → product_differentiation

ELSE IF threat_score < 5 AND price_diff <= 10%
  → hold_position

ELSE
  → promotion_response (default)
```

## Usage

### Basic Usage

```python
from agent_c_strategist import AgentCStrategist

strategist = AgentCStrategist()

# Prepare inputs
business_profile = {
    "name": "Tony's Pizza",
    "business_type": "pizza restaurant",
    "unique_selling_points": ["Wood-fired oven", "Family recipes"],
    "pricing": {"large_pizza": 17.99}
}

scout_findings = {
    "competitors": [
        {"name": "Domino's", "price": 15.99, "promotion": "50% off"}
    ]
}

analyst_output = {
    "impact_level": "medium",
    "price_difference_percent": 8.0,
    "threat_score": 6.5,
    "recommended_urgency": "medium",
    "response_type": "promotion_response",
    "key_insights": [
        "Competitors running aggressive promotions",
        "Your base pricing is still competitive"
    ]
}

# Generate strategy
result_json = strategist.strategize(
    business_profile,
    scout_findings,
    analyst_output
)

print(result_json)
```

### Output Format

```json
{
  "recommended_action": "Launch a limited-time promotion for Tony's Pizza to compete with current competitor offers. Keep base prices unchanged.",
  "response_type": "promotion_response",
  "price_action": "Keep base prices. Launch a 15-20% limited-time promotion (2-4 weeks) to match competitor offers.",
  "campaign_idea": "Feast Mode: Limited Time Offer",
  "marketing_post": "🔥 FLASH SALE AT TONY'S PIZZA! 🔥\n\nGet 20% OFF your order this week only! Don't miss out on your favorite pizza restaurant. Limited time. Order now!",
  "cta": "Claim your discount before it's gone!",
  "execution_steps": [
    "Design a 15-20% discount offer for your best-selling items",
    "Create social media posts and email campaign announcing the promotion",
    "Set a clear deadline (2-4 weeks) and promote urgency",
    "Track response rate and sales during promotion period"
  ],
  "why_this_strategy": [
    "Competitors are using promotions as their main tactic",
    "Your base pricing is competitive; temporary promotion is lower risk",
    "Promotions are quick to implement and test",
    "Keeps base prices stable for long-term positioning"
  ]
}
```

## Integration with Full Pipeline

### Option 1: Sequential Calls

```python
from agents.scout_agent.scout_agent import ScoutAgent
from agent_b_analyst import AgentBAnalyst
from agent_c_strategist import AgentCStrategist

# Step 1: Scout finds competitors
scout = ScoutAgent()
scout_findings = scout.analyze("competitor_promo.txt")

# Step 2: Analyst evaluates impact
analyst = AgentBAnalyst()
analysis = analyst.analyze(business_profile, scout_findings)

# Step 3: Strategist generates action plan
strategist = AgentCStrategist()
strategy = strategist.strategize(business_profile, scout_findings, analysis)

print(strategy)
```

### Option 2: Use War Room Demo

```python
# Run the complete pipeline
python war_room_demo.py
```

## Key Features

### ✅ Practical Recommendations
- Designed for small businesses
- Low-cost, high-impact actions
- Ready to implement

### ✅ Marketing Content Generation
- Social media posts ready to use
- Clear, engaging CTAs
- Campaign ideas included

### ✅ Clear Execution Steps
- 3-5 actionable steps
- Prioritized and sequenced
- Suitable for non-technical users

### ✅ Strategy Rationale
- Explains why the strategy was chosen
- Based on data analysis
- Transparent decision-making

### ✅ Dashboard-Ready Output
- Clean JSON format
- All fields populated
- Easy to display in UI

## Design Principles

1. **Simplicity:** Recommendations are easy to understand
2. **Practicality:** Actions are feasible for small businesses
3. **Clarity:** No jargon, business-friendly language
4. **Actionability:** Every recommendation is executable
5. **Transparency:** Rationale explains the "why"

## Testing

Run the test suite:

```bash
python test_agent_c.py
```

Run demo scenarios:

```bash
python demo_strategist.py
```

## File Structure

```
agent_c_strategist.py      # Main Agent C implementation
test_agent_c.py            # Test suite
demo_strategist.py         # Demo scenarios
AGENT_C_README.md          # This file
```

## Common Use Cases

### Use Case 1: Price War Scenario
**Input:** Competitor undercuts by 30%  
**Output:** `price_adjustment` with specific % reduction recommendation

### Use Case 2: Promotion Battle
**Input:** Multiple competitors running promotions  
**Output:** `promotion_response` with campaign idea and ready post

### Use Case 3: Premium Positioning
**Input:** Higher prices but unique quality  
**Output:** `product_differentiation` with USP messaging

### Use Case 4: Stable Market
**Input:** Low threat, competitive pricing  
**Output:** `hold_position` with monitoring recommendations

## Limitations

- Designed for **small businesses** not enterprise
- Focused on **tactical responses** not long-term strategy
- Works best with **local/regional competition**
- Recommendations are **suggestions** not guaranteed outcomes

## Tips for Best Results

1. **Provide complete data:** More context = better strategy
2. **Update regularly:** Market changes require strategy updates
3. **Test recommendations:** Start small, measure results
4. **Customize output:** Adapt marketing posts to your brand voice
5. **Monitor outcomes:** Track what works

## Support

For issues or questions:
- Check `demo_strategist.py` for examples
- Review `test_agent_c.py` for expected behavior
- See `war_room_demo.py` for full pipeline integration

## Version

**Current Version:** 2.0  
**Last Updated:** Project implementation

---

**Part of the Multi-Agent Market Intelligence System**
- Agent A: Scout (finds competitors)
- Agent B: Analyst (evaluates impact)
- Agent C: Strategist (recommends action) ← You are here
