"""
Demo: Simplified Key Insights
Shows the new concise insight format
"""

import json
from agent_b_analyst import AgentBAnalyst


def print_insights_demo(title, business, competitors):
    """Print insights in a clean format"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)
    
    agent = AgentBAnalyst()
    result_json = agent.analyze(business, competitors)
    result = json.loads(result_json)
    
    print("\n📊 KEY INSIGHTS (Concise Format):")
    for i, insight in enumerate(result['key_insights'], 1):
        print(f"   {i}. {insight}")
    
    print(f"\n   Impact: {result['impact_level'].upper()}")
    print(f"   Urgency: {result['recommended_urgency'].upper()}")


def main():
    print("\n" + "█" * 70)
    print("  SIMPLIFIED KEY INSIGHTS - NEW FORMAT")
    print("█" * 70)
    print("\n  Key insights are now concise, fact-based statements")
    print("  that highlight the most important competitive factors.\n")
    
    # Example 1: Price-focused
    print_insights_demo(
        "EXAMPLE 1: Price Competition",
        {
            "name": "Premium Coffee",
            "pricing": {"average_price": 7.00},
            "target_audience": {
                "demographics": ["professionals"],
                "interests": ["quality"]
            }
        },
        {
            "competitors": [
                {
                    "name": "Budget Coffee",
                    "pricing": {"average_price": 4.00},
                    "target_audience": {
                        "demographics": ["professionals"],
                        "interests": ["value"]
                    }
                }
            ]
        }
    )
    
    # Example 2: Promotion-focused
    print_insights_demo(
        "EXAMPLE 2: Promotional Competition",
        {
            "name": "Local Cafe",
            "pricing": {"average_price": 5.00}
        },
        {
            "competitors": [
                {
                    "name": "Chain Coffee",
                    "pricing": {"average_price": 4.50},
                    "promotions": [
                        "Buy one get one free",
                        "50% off all drinks",
                        "Free loyalty program"
                    ]
                }
            ]
        }
    )
    
    # Example 3: Product innovation
    print_insights_demo(
        "EXAMPLE 3: Product Innovation",
        {
            "name": "Traditional Cafe",
            "pricing": {"average_price": 5.00},
            "products": ["Coffee", "Tea", "Pastries"]
        },
        {
            "competitors": [
                {
                    "name": "Innovative Cafe",
                    "pricing": {"average_price": 5.50},
                    "new_products": [
                        "Nitro cold brew",
                        "Oat milk lattes",
                        "Vegan pastries",
                        "CBD coffee"
                    ],
                    "bundles": [
                        "Breakfast bundle",
                        "Afternoon snack pack"
                    ]
                }
            ]
        }
    )
    
    # Example 4: Multiple factors
    print_insights_demo(
        "EXAMPLE 4: Complex Competitive Scenario",
        {
            "name": "Your Business",
            "pricing": {"average_price": 6.00},
            "target_audience": {
                "demographics": ["millennials", "professionals"],
                "interests": ["coffee", "workspace"]
            },
            "positioning": "Premium coffee with co-working space"
        },
        {
            "competitors": [
                {
                    "name": "Discount Coffee",
                    "pricing": {"average_price": 3.50},
                    "promotions": ["50% off all week"],
                    "target_audience": {
                        "demographics": ["millennials", "students"],
                        "interests": ["value", "convenience"]
                    }
                },
                {
                    "name": "Premium Roasters",
                    "pricing": {"average_price": 7.00},
                    "new_products": ["Single-origin beans", "Coffee tasting classes"],
                    "target_audience": {
                        "demographics": ["professionals"],
                        "interests": ["specialty coffee", "quality"]
                    },
                    "positioning": "Premium coffee experience"
                }
            ]
        }
    )
    
    print("\n" + "=" * 70)
    print("  INSIGHT FORMAT BENEFITS")
    print("=" * 70)
    print("""
  ✓ Concise - Easy to scan and understand quickly
  ✓ Factual - Based on real data, not assumptions
  ✓ Actionable - Clear what needs attention
  ✓ Prioritized - Most important insights shown first
  ✓ Quantified - Includes specific numbers when available
  
  Example insights:
    - "You're 20% more expensive than market average"
    - "5 aggressive competitor promotions active"
    - "Same target audience as competitors"
    - "Competitors launched 8 new products/bundles"
    - "Similar positioning to competitors"
    """)
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
