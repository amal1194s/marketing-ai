# 🚀 Quick Start Guide - Scout Agent

Get started with Scout Agent in 5 minutes!

---

## Step 1: Verify Installation

```bash
cd "c:\Users\Remigius_Paul_Antony\OneDrive\Desktop\TEAM 25\Team 25 - 2\marketing-ai"
```

---

## Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: Only `pyyaml` and `pytest` are required. Optional dependencies are commented out.

---

## Step 3: Run Your First Demo

```bash
python main.py
```

**Expected Output:**
- ✅ 4 competitor signals extracted
- ✅ Events detected: promotions, discounts, new products
- ✅ Signals exported to JSON

---

## Step 4: Try File Processing

```bash
python examples/demo_file_processing.py
```

This will:
- Process sample JSON data
- Process text files
- Show statistics
- Export results

---

## Step 5: Run Tests

```bash
python -m pytest tests/ -v
```

Or with unittest:

```bash
python -m unittest tests.test_scout_agent -v
```

---

## Quick Code Examples

### Example 1: Process Text

```python
from agents.scout_agent import ScoutAgent

agent = ScoutAgent()

text = "McDonald's launches new burger at ₹99 with 20% off"
signals = agent.process_text(text, "McDonald's", "website")

print(signals)
```

### Example 2: Process JSON Data

```python
data = {
    "competitor": "Dominos",
    "product": "Pizza",
    "event_type": "promotion",
    "price": "299",
    "offer": "Buy 1 Get 1"
}

signals = agent.process_structured_data(data)
print(signals)
```

### Example 3: Process File

```python
# Process JSON file
signals = agent.process_file("data/inputs/sample_competitor_data.json")

# Export results
agent.export_signals("my_output.json")
```

### Example 4: Get Statistics

```python
stats = agent.get_stats()
print(f"Total signals: {stats['total_signals']}")
print(f"By type: {stats['by_event_type']}")
print(f"Competitors: {stats['unique_competitors']}")
```

---

## File Locations

### Input Files
- `data/inputs/sample_competitor_data.json` - Sample JSON data
- `data/inputs/dominos_promo.txt` - Sample text data

### Output Files
- `data/outputs/competitor_signals.json` - Exported signals
- Created automatically when you run `main.py`

### Configuration
- `config/scout_config.yaml` - Agent settings

---

## Common Tasks

### Task 1: Monitor a Competitor Website

```python
from agents.scout_agent import ScoutAgent

agent = ScoutAgent()

# Website content
website_text = """
Pizza Hut launching new Veggie Supreme at ₹249.
Special offer: Get 30% off on orders above ₹500.
"""

signals = agent.process_text(website_text, "Pizza Hut", "website")
agent.export_signals("pizza_hut_signals.json")
```

### Task 2: Process API Data

```python
# Assuming you have API response
api_data = [
    {"competitor": "KFC", "product": "Bucket", "price": "399", "offer": "20% off"},
    {"competitor": "Subway", "product": "Sub", "price": "120", "offer": "Combo"}
]

signals = agent.process_structured_data(api_data, source="api")
```

### Task 3: Batch Processing

```python
batch = [
    {
        "type": "text",
        "data": "Dominos new offer...",
        "competitor": "Dominos",
        "source": "web"
    },
    {
        "type": "structured",
        "data": {"competitor": "KFC", "product": "Burger", "price": "99"},
        "source": "api"
    }
]

signals = agent.process_batch(batch)
```

### Task 4: Filter Signals

```python
# Get all promotions
promotions = agent.get_signals_by_type("promotion")

# Get all Dominos signals
dominos = agent.get_signals_by_competitor("Dominos")

# Get statistics
stats = agent.get_stats()
```

---

## Troubleshooting

### Issue: Import Error

```bash
# Make sure you're in the project root
cd "c:\Users\Remigius_Paul_Antony\OneDrive\Desktop\TEAM 25\Team 25 - 2\marketing-ai"

# Run with proper path
python main.py
```

### Issue: Module not found

```bash
# Install dependencies
pip install -r requirements.txt
```

### Issue: No signals extracted

- Check competitor name is provided
- Verify text has detectable events
- Check event type keywords are present
- View raw output for debugging

---

## Next Steps

1. ✅ Read [README.md](README.md) for full documentation
2. ✅ Check [SCOUT_AGENT_PROMPT.md](SCOUT_AGENT_PROMPT.md) for specifications
3. ✅ View [ARCHITECTURE.md](ARCHITECTURE.md) for system design
4. ✅ Explore [PROJECT_SUMMARY.md](PROJECT_SUMMARY.md) for build info
5. ✅ Customize `config/scout_config.yaml` for your needs
6. ✅ Add your own data sources
7. ✅ Integrate with your multi-agent system

---

## Integration Example

```python
# Example: Integrate with your system

from agents.scout_agent import ScoutAgent

class CompetitorMonitor:
    def __init__(self):
        self.scout = ScoutAgent()
    
    def monitor_website(self, url, competitor):
        # Fetch website content (using requests, BeautifulSoup, etc.)
        content = self.fetch_content(url)
        
        # Extract signals
        signals = self.scout.process_text(content, competitor, "website")
        
        # Send to downstream agents
        self.send_to_analyzer(signals)
        self.trigger_alerts(signals)
        
        return signals
    
    def fetch_content(self, url):
        # Your scraping logic
        pass
    
    def send_to_analyzer(self, signals):
        # Send to analyzer agent
        pass
    
    def trigger_alerts(self, signals):
        # Trigger alert system
        pass
```

---

## Output Format Reference

```json
{
  "competitor": "string (required)",
  "product": "string (optional)",
  "event_type": "price_change|new_product|promotion|discount|marketing_campaign|bundle_offer",
  "price": "string (optional)",
  "offer": "string (optional)",
  "source": "string (required)",
  "summary": "string (required, 1 sentence)"
}
```

---

## Support

- 📖 Documentation: README.md
- 🏗️ Architecture: ARCHITECTURE.md
- 📋 Summary: PROJECT_SUMMARY.md
- 🎯 Specs: SCOUT_AGENT_PROMPT.md
- 🧪 Tests: tests/test_scout_agent.py

---

**Ready to start monitoring competitors!** 🚀

Run `python main.py` now!
