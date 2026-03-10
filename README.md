# RivalSense AI - Market Intelligence System

**AI-powered market intelligence for small businesses** - Monitor competitors, assess threats, and generate strategies automatically.

## 🎯 What is RivalSense AI?

RivalSense AI is a complete market intelligence platform that helps small businesses compete by:
- 🔍 **Monitoring** competitors 24/7 (pricing, promotions, campaigns)
- 🔬 **Analyzing** market threats with quantified scoring (0-10 scale)
- 🎯 **Strategizing** with AI-generated action plans and marketing content
- ⚡ **Delivering** results in seconds, not hours or days

## 🚀 Quick Start

### 1. Install Dependencies
```bash
.\install.ps1
```

### 2. Start the System
```bash
.\start.ps1
```

### 3. Open War Room
Navigate to `http://localhost:3000/war-room` and click "Start Analysis"

**That's it!** Your AI agents will analyze the market and generate strategies.

---

## 🏗️ Architecture

### System Pipeline

```
Scout Agent (Competitor Monitoring)
    ↓
Analyst Agent (Threat Analysis)
    ↓
Strategist Agent (Strategy Generation)
    ↓
Dashboard UI (Results Display)
```

### Tech Stack

**Backend (Python):**
- FastAPI for REST API
- Multi-agent system (Scout, Analyst, Strategist)
- JSON-based data pipeline

**Frontend (Next.js):**
- React 18 with TypeScript
- Tailwind CSS + shadcn/ui
- Framer Motion animations
- Real-time War Room visualization

---

## 📊 Agent System

### Key Features
- ✅ Multi-Source Monitoring (websites, APIs, social media, text feeds)
- ✅ Event Detection (promotions, discounts, bundles, price changes, new products, campaigns)
- ✅ Price Extraction from text and structured data
- ✅ Batch Processing for multiple signals
- ✅ Structured JSON Output

### Quick Usage

```python
from agents.scout_agent import ScoutAgent

agent = ScoutAgent()
text = "Dominos launched Buy 1 Get 1 offer on Pizza at ₹299"
signals = agent.process_text(text, competitor="Dominos", source="website")
agent.export_signals("data/outputs/competitor_signals.json")
```

---

## 📊 Analyst Agent - Market Opportunity Scoring

### What's New: Market Opportunity Score (0-10)

🎯 **Quantified Threats** - Each competitor signal gets a 0-10 score  
📈 **Smart Scoring** - Based on price differences, event types, and market conditions  
🎨 **Visual Console** - Color-coded output (🔴 HIGH, 🟡 MEDIUM, 🟢 LOW)  
💡 **Strategic Insights** - Actionable recommendations for each threat

### Opportunity Score Logic

```
Base Score: 5
+ Price Advantage (if competitor cheaper):
  0-10%: +0.5  |  10-20%: +1.5  |  20-30%: +2.5  |  >30%+3.0
+ Event Bonus: promotion/discount +2 | launch +1
+ Extreme Discount (>30% cheaper): +3
= Total (capped at 10)
```

**Impact Mapping:** 8-10 = 🔴 HIGH | 5-7 = 🟡 MEDIUM | 0-4 = 🟢 LOW

### Quick Usage

```python
from agents.analyst_agent import run_analyst_agent, calculate_opportunity_score

# Run full analysis
results = run_analyst_agent()

# Calculate custom score
signal = {"competitor": "Dominos", "price": 299, "event_type": "promotion"}
business = {"price": 350}
score = calculate_opportunity_score(signal, business)
print(f"Score: {score}/10")  # 8.5/10
```

### Example Output

**Terminal:**
```
  1. 🔴 Dominos - Score: 8.5/10 (HIGH Impact)
  2. 🔴 Pizza Hut - Score: 10.0/10 (HIGH Impact)
  3. 🟡 Papa John's - Score: 6.0/10 (MEDIUM Impact)
```

**JSON (data/outputs/market_analysis.json):**
```json
{
  "competitor": "Dominos",
  "opportunity_score": 8.5,
  "impact_level": "high",
  "price_difference": -51,
  "insight": "Dominos promotion creates strong competitive pressure..."
}
```

---

## 🚀 Quick Start

### Installation

```bash
cd marketing-ai
pip install -r requirements.txt  # For Scout Agent
# Analyst Agent uses pure Python stdlib (no dependencies)
```

### Run Complete Pipeline

```bash
# Step 1: Scout collects data
python main.py

# Step 2: Analyst analyzes threats
python agents/analyst_agent.py
```

### Run Tests

```bash
# Scout Agent
python -m pytest tests/ -v

# Analyst Agent
python test_opportunity_score.py  # 21/21 tests passing ✅
```

---

## 📁 Project Structure

```
marketing-ai/
├── agents/
│   ├── scout_agent/              # Scout module
│   └── analyst_agent.py          # Analyst with opportunity scoring
├── data/
│   ├── inputs/
│   │   └── business_profile.json
│   └── outputs/
│       ├── competitor_signals.json    # Scout → Analyst  
│       └── market_analysis.json       # Analyst output
├── tests/
│   └── test_scout_agent.py
├── test_opportunity_score.py
├── main.py
└── README.md
```

---

## 📖 Documentation

**Scout Agent:**
- ARCHITECTURE.md
- SCOUT_AGENT_PROMPT.md
- PROJECT_SUMMARY.md

**Analyst Agent:**
- README_OPPORTUNITY_SCORE.md
- OPPORTUNITY_SCORE_EXAMPLES.md
- ANALYST_IMPLEMENTATION.md

---

## ✨ Features

### Scout Agent
✅ Multi-source monitoring  
✅ 6 event types detected  
✅ Price extraction  
✅ Batch processing

### Analyst Agent
✅ Market Opportunity Scores (0-10)  
✅ Smart threat classification  
✅ Price-based scoring  
✅ Actionable insights  
✅ 100% test coverage

---

## 🛣️ Roadmap

**Completed** ✅
- Scout Agent with multi-source monitoring
- Analyst Agent with Market Opportunity Scores
- Complete test coverage

**In Progress** 🚧
- Strategist Agent
- Real-time monitoring dashboard

**Planned** 📋
- Automated alert system
- Historical trend analysis
- Mobile app integration

---

## Purpose
Evaluates how competitor activity affects your business and identifies strategic risks and opportunities using Market Opportunity Scores.

### What It Analyzes
- **Price Differences** - Calculates opportunity scores  based on competitor pricing
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
