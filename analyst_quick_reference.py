"""
ScoutIQ Analyst Agent - Quick Reference
Copy-paste examples for immediate use
"""

# =============================================================================
# EXAMPLE 1: Run the full pipeline
# =============================================================================

from agents.analyst_agent import run_analyst_agent

# Reads competitor_signals.json and business_profile.json
# Outputs market_analysis.json
results = run_analyst_agent()

# Access results
for result in results:
    print(f"{result['competitor']}: {result['impact_level'].upper()}")


# =============================================================================
# EXAMPLE 2: Analyze a single signal
# =============================================================================

from agents.analyst_agent import analyze_signal

business = {
    "business_name": "My Store",
    "product": "Widget",
    "price": 500
}

signal = {
    "competitor": "Rival Store",
    "product": "Widget",
    "event_type": "discount",
    "price": 350,
    "offer": "30% off"
}

result = analyze_signal(signal, business)

print(f"Impact: {result['impact_level']}")
print(f"Price difference: ₹{result['price_difference']}")
print(f"Insight: {result['insight']}")


# =============================================================================
# EXAMPLE 3: Batch processing with custom logic
# =============================================================================

from agents.analyst_agent import load_json, analyze_signal

# Load data
signals = load_json("data/outputs/competitor_signals.json")
business = load_json("data/inputs/business_profile.json")

# Analyze with filtering
high_impact_signals = []
for signal in signals:
    result = analyze_signal(signal, business)
    
    # Filter for high-impact only
    if result['impact_level'] == 'high':
        high_impact_signals.append(result)

print(f"High-impact threats: {len(high_impact_signals)}")


# =============================================================================
# EXAMPLE 4: Custom impact classification
# =============================================================================

from agents.analyst_agent import classify_impact

signal = {
    "event_type": "promotion",
    "price": 250,
    "offer": "Buy 1 Get 1"
}

price_difference = 250 - 350  # competitor - user
user_price = 350

impact = classify_impact(signal, price_difference, user_price)
print(f"Impact level: {impact}")  # "high"


# =============================================================================
# EXAMPLE 5: Generate custom insight
# =============================================================================

from agents.analyst_agent import generate_insight

signal = {
    "competitor": "Test Competitor",
    "event_type": "discount",
    "price": 200,
    "offer": "50% off",
    "product": "Widget"
}

business = {
    "business_name": "My Business",
    "product": "Widget",
    "price": 400
}

price_diff = -200
impact = "high"

insight = generate_insight(signal, business, price_diff, impact)
print(insight)


# =============================================================================
# EXAMPLE 6: Save custom analysis
# =============================================================================

from agents.analyst_agent import save_json

custom_results = [
    {
        "competitor": "A",
        "impact_level": "high",
        "insight": "Custom insight here"
    }
]

save_json(custom_results, "data/outputs/my_analysis.json")


# =============================================================================
# COMMAND LINE USAGE
# =============================================================================

# Run from project root:
# python agents/analyst_agent.py

# Run tests:
# python test_analyst_agent.py

# Run demos:
# python demo_analyst_scenarios.py


# =============================================================================
# INPUT FILE FORMATS
# =============================================================================

# business_profile.json
example_business = {
    "business_name": "Tony's Pizza",
    "product": "Veg Pizza",
    "price": 350,
    "location": "Coimbatore"
}

# competitor_signals.json
example_signals = [
    {
        "competitor": "Dominos",
        "product": "Farmhouse Pizza",
        "event_type": "promotion",
        "price": 299,
        "offer": "Buy 1 Get 1",
        "source": "website",
        "summary": "Dominos launched Buy 1 Get 1 offer",
        "timestamp": "2026-03-09T10:30:00"
    }
]


# =============================================================================
# OUTPUT FORMAT
# =============================================================================

# market_analysis.json
example_output = [
    {
        "competitor": "Dominos",
        "event_type": "promotion",
        "competitor_price": 299,
        "user_price": 350,
        "price_difference": -51,
        "impact_level": "high",
        "insight": "Dominos promotion offers a significantly lower price...",
        "timestamp": "2026-03-09T10:30:00",
        "offer": "Buy 1 Get 1",
        "product": "Farmhouse Pizza"
    }
]


# =============================================================================
# ERROR HANDLING EXAMPLES
# =============================================================================

from agents.analyst_agent import load_json
import json

# Handle missing files
try:
    data = load_json("missing_file.json")
except FileNotFoundError as e:
    print(f"File not found: {e}")

# Handle invalid JSON
try:
    data = load_json("malformed.json")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")

# Handle invalid business profile
try:
    result = analyze_signal(signal, {"price": 0})
except ValueError as e:
    print(f"Validation error: {e}")


# =============================================================================
# INTEGRATION PATTERNS
# =============================================================================

# Pattern 1: Sequential pipeline
# 1. Scout generates competitor_signals.json
# 2. Run analyst agent
# 3. Strategist reads market_analysis.json

# Pattern 2: Real-time processing
import time
from pathlib import Path
from agents.analyst_agent import run_analyst_agent

def monitor_and_analyze():
    """Monitor for new signals and analyze automatically"""
    signal_file = Path("data/outputs/competitor_signals.json")
    last_modified = 0
    
    while True:
        if signal_file.exists():
            current_modified = signal_file.stat().st_mtime
            
            if current_modified > last_modified:
                print("New signals detected, analyzing...")
                run_analyst_agent()
                last_modified = current_modified
        
        time.sleep(60)  # Check every minute


# Pattern 3: Webhook integration
from agents.analyst_agent import analyze_signal

def webhook_handler(signal_data, business_profile):
    """Analyze signal from webhook payload"""
    result = analyze_signal(signal_data, business_profile)
    
    # Send to notification system if high impact
    if result['impact_level'] == 'high':
        send_alert(result)
    
    return result


# =============================================================================
# CUSTOMIZATION EXAMPLES
# =============================================================================

# Customize impact thresholds
def my_classify_impact(signal, price_diff, user_price):
    """Custom impact classification"""
    if abs(price_diff) > 100:  # Your threshold
        return "high"
    elif abs(price_diff) > 30:
        return "medium"
    else:
        return "low"

# Add custom fields to output
def enhanced_analyze_signal(signal, business):
    """Add custom analysis fields"""
    result = analyze_signal(signal, business)
    
    # Add your custom fields
    result['custom_metric'] = calculate_my_metric(signal)
    result['recommendation'] = get_recommendation(result)
    
    return result


# =============================================================================
# TESTING UTILITIES
# =============================================================================

def create_test_signal(competitor="Test", price=300, event="discount"):
    """Helper to create test signals"""
    return {
        "competitor": competitor,
        "product": "Test Product",
        "event_type": event,
        "price": price,
        "offer": "Test offer",
        "timestamp": "2026-03-09T10:00:00"
    }

def assert_impact_level(signal, business, expected_impact):
    """Test helper to verify impact classification"""
    result = analyze_signal(signal, business)
    assert result['impact_level'] == expected_impact, \
        f"Expected {expected_impact}, got {result['impact_level']}"


# =============================================================================
# PERFORMANCE OPTIMIZATION
# =============================================================================

# For large datasets, process in batches
def analyze_large_dataset(signals, business, batch_size=100):
    """Process signals in batches"""
    results = []
    
    for i in range(0, len(signals), batch_size):
        batch = signals[i:i + batch_size]
        
        for signal in batch:
            try:
                result = analyze_signal(signal, business)
                results.append(result)
            except Exception as e:
                print(f"Error in batch {i}: {e}")
    
    return results


# =============================================================================
# SUMMARY STATISTICS
# =============================================================================

def get_analysis_summary(results):
    """Generate summary statistics"""
    total = len(results)
    high = sum(1 for r in results if r['impact_level'] == 'high')
    medium = sum(1 for r in results if r['impact_level'] == 'medium')
    low = sum(1 for r in results if r['impact_level'] == 'low')
    
    avg_price_diff = sum(r['price_difference'] for r in results) / total if total > 0 else 0
    
    return {
        "total_signals": total,
        "high_impact": high,
        "medium_impact": medium,
        "low_impact": low,
        "average_price_difference": avg_price_diff,
        "competitors": list(set(r['competitor'] for r in results))
    }


if __name__ == "__main__":
    print("ScoutIQ Analyst Agent - Quick Reference")
    print("Copy examples above for your use case")
