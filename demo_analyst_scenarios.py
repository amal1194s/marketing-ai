"""
ScoutIQ Analyst Agent - Demo Scenarios
Demonstrates different competitive scenarios and analysis outputs
"""

import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).parent))

from agents.analyst_agent import analyze_signal


def print_scenario(title, description, business, signals):
    """Print a demo scenario with analysis"""
    print("\n" + "=" * 75)
    print(f"  {title}")
    print("=" * 75)
    print(f"  {description}")
    print()
    
    print(f"📊 Your Business: {business.get('business_name', 'Unknown')}")
    print(f"   Product: {business.get('product', 'N/A')}")
    print(f"   Price: ₹{business.get('price', 0)}")
    print()
    
    print(f"🔍 Analyzing {len(signals)} competitor signal(s)...")
    print()
    
    for i, signal in enumerate(signals, 1):
        result = analyze_signal(signal, business)
        
        # Impact emoji
        impact_emoji = {
            "high": "🔴",
            "medium": "🟡",
            "low": "🟢"
        }.get(result['impact_level'], "⚪")
        
        print(f"{i}. {impact_emoji} {result['competitor']} - {result['impact_level'].upper()}")
        print(f"   Event: {result['event_type']}")
        print(f"   Price: ₹{result['competitor_price']} (Difference: ₹{result['price_difference']})")
        if result['offer']:
            print(f"   Offer: {result['offer']}")
        print(f"   💡 Insight: {result['insight']}")
        print()


def main():
    """Run demo scenarios"""
    print()
    print("█" * 75)
    print("  ScoutIQ Analyst Agent - Demo Scenarios")
    print("█" * 75)
    
    # Scenario 1: Aggressive Price War
    print_scenario(
        "SCENARIO 1: Price War",
        "Multiple competitors launch aggressive pricing campaigns",
        {
            "business_name": "Premium Pizza Co",
            "product": "Margherita Pizza",
            "price": 450
        },
        [
            {
                "competitor": "Budget Pizza",
                "product": "Margherita",
                "event_type": "discount",
                "price": 199,
                "offer": "50% off all pizzas",
                "timestamp": "2026-03-09T10:00:00"
            },
            {
                "competitor": "Quick Pizza",
                "product": "Margherita",
                "event_type": "promotion",
                "price": 249,
                "offer": "Buy 1 Get 1",
                "timestamp": "2026-03-09T10:30:00"
            },
            {
                "competitor": "Local Pizza",
                "product": "Margherita",
                "event_type": "price_update",
                "price": 299,
                "offer": "",
                "timestamp": "2026-03-09T11:00:00"
            }
        ]
    )
    
    # Scenario 2: Premium Competition
    print_scenario(
        "SCENARIO 2: Premium Positioning",
        "Upmarket competitors enter with higher pricing",
        {
            "business_name": "Tony's Pizza",
            "product": "Veg Pizza",
            "price": 350
        },
        [
            {
                "competitor": "Gourmet Pizza House",
                "product": "Artisan Veg Pizza",
                "event_type": "launch",
                "price": 699,
                "offer": "Grand opening - Free dessert",
                "timestamp": "2026-03-09T09:00:00"
            },
            {
                "competitor": "Luxury Pizza",
                "product": "Truffle Veg Pizza",
                "event_type": "launch",
                "price": 899,
                "offer": "New premium line",
                "timestamp": "2026-03-09T09:30:00"
            }
        ]
    )
    
    # Scenario 3: Mixed Competition
    print_scenario(
        "SCENARIO 3: Mixed Market Dynamics",
        "Various competitive activities at different price points",
        {
            "business_name": "Metro Pizza",
            "product": "Classic Pizza",
            "price": 400
        },
        [
            {
                "competitor": "Dominos",
                "product": "Farmhouse Pizza",
                "event_type": "discount",
                "price": 299,
                "offer": "30% off",
                "timestamp": "2026-03-09T08:00:00"
            },
            {
                "competitor": "Pizza Hut",
                "product": "Veggie Pizza",
                "event_type": "promotion",
                "price": 380,
                "offer": "Free drink combo",
                "timestamp": "2026-03-09T08:30:00"
            },
            {
                "competitor": "Papa John's",
                "product": "Garden Special",
                "event_type": "launch",
                "price": 450,
                "offer": "New recipe launch",
                "timestamp": "2026-03-09T09:00:00"
            },
            {
                "competitor": "Local Pizzeria",
                "product": "Home Style Pizza",
                "event_type": "price_update",
                "price": 320,
                "offer": "",
                "timestamp": "2026-03-09T09:30:00"
            }
        ]
    )
    
    # Scenario 4: New Market Entrant
    print_scenario(
        "SCENARIO 4: New Competitor Entry",
        "Well-funded new player enters market with aggressive strategy",
        {
            "business_name": "Established Pizza",
            "product": "Pizza",
            "price": 500
        },
        [
            {
                "competitor": "NewCo Pizza",
                "product": "Signature Pizza",
                "event_type": "launch",
                "price": 199,
                "offer": "Launch week - 60% off + Free delivery",
                "timestamp": "2026-03-09T07:00:00"
            },
            {
                "competitor": "NewCo Pizza",
                "product": "Combo Deal",
                "event_type": "promotion",
                "price": 299,
                "offer": "2 Pizzas + 2 Drinks",
                "timestamp": "2026-03-09T07:30:00"
            }
        ]
    )
    
    # Scenario 5: Stable Market
    print_scenario(
        "SCENARIO 5: Stable Market",
        "Minor competitive activity, no major threats",
        {
            "business_name": "Steady Pizza",
            "product": "Classic Pizza",
            "price": 380
        },
        [
            {
                "competitor": "Regular Pizza Co",
                "product": "Basic Pizza",
                "event_type": "price_update",
                "price": 420,
                "offer": "",
                "timestamp": "2026-03-09T06:00:00"
            },
            {
                "competitor": "Standard Pizza",
                "product": "Traditional Pizza",
                "event_type": "menu_update",
                "price": 390,
                "offer": "Seasonal toppings added",
                "timestamp": "2026-03-09T06:30:00"
            }
        ]
    )
    
    print("=" * 75)
    print("✅ Demo scenarios completed")
    print("=" * 75)
    print("\n📝 Key Takeaways:")
    print("  • HIGH impact (🔴): Significant price advantage or aggressive promotion")
    print("  • MEDIUM impact (🟡): Notable activity or moderate price difference")
    print("  • LOW impact (🟢): Higher pricing or minimal competitive threat")
    print()


if __name__ == "__main__":
    main()
