"""
Demo: Price Difference Percent Field
Shows how the new price_difference_percent field works
"""

import json
from agent_b_analyst import AgentBAnalyst


def print_scenario(title, business, competitors):
    """Print a test scenario and show the price_difference_percent"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)
    
    agent = AgentBAnalyst()
    result_json = agent.analyze(business, competitors)
    result = json.loads(result_json)
    
    print(f"Business Price: ${business.get('pricing', {}).get('average_price', 'N/A')}")
    
    if competitors.get('competitors'):
        comp_prices = [c.get('pricing', {}).get('average_price', 0) 
                      for c in competitors['competitors'] if c.get('pricing')]
        if comp_prices:
            avg_comp_price = sum(comp_prices) / len(comp_prices)
            print(f"Competitor Avg: ${avg_comp_price:.2f}")
    
    print(f"\n📊 price_difference_percent: {result['price_difference_percent']}")
    
    if result['price_difference_percent'] is not None:
        if result['price_difference_percent'] > 0:
            print(f"   → You're {result['price_difference_percent']:.1f}% MORE expensive")
        elif result['price_difference_percent'] < 0:
            print(f"   → You're {abs(result['price_difference_percent']):.1f}% CHEAPER")
        else:
            print(f"   → Your pricing matches the market average")
    else:
        print(f"   → No pricing data available for comparison")
    
    print(f"\nImpact: {result['impact_level'].upper()}")
    print(f"Urgency: {result['recommended_urgency'].upper()}")


def main():
    print("\n" + "█" * 70)
    print("  PRICE DIFFERENCE PERCENT - NEW FIELD DEMO")
    print("█" * 70)
    
    # Scenario 1: Higher priced
    print_scenario(
        "SCENARIO 1: You're More Expensive",
        {
            "name": "Premium Cafe",
            "pricing": {"average_price": 8.00}
        },
        {
            "competitors": [
                {"name": "Budget Coffee", "pricing": {"average_price": 5.00}}
            ]
        }
    )
    
    # Scenario 2: Lower priced
    print_scenario(
        "SCENARIO 2: You're Cheaper",
        {
            "name": "Value Coffee",
            "pricing": {"average_price": 4.00}
        },
        {
            "competitors": [
                {"name": "Premium Cafe", "pricing": {"average_price": 7.00}}
            ]
        }
    )
    
    # Scenario 3: About the same
    print_scenario(
        "SCENARIO 3: Competitive Pricing",
        {
            "name": "Market Average Cafe",
            "pricing": {"average_price": 5.50}
        },
        {
            "competitors": [
                {"name": "Competitor A", "pricing": {"average_price": 5.25}},
                {"name": "Competitor B", "pricing": {"average_price": 5.75}}
            ]
        }
    )
    
    # Scenario 4: No pricing data
    print_scenario(
        "SCENARIO 4: No Pricing Data",
        {
            "name": "Unknown Pricing"
        },
        {
            "competitors": [
                {"name": "Competitor", "promotions": ["Sale"]}
            ]
        }
    )
    
    # Scenario 5: Extreme difference
    print_scenario(
        "SCENARIO 5: Extreme Price Gap (2x more expensive)",
        {
            "name": "Luxury Cafe",
            "pricing": {"average_price": 15.00}
        },
        {
            "competitors": [
                {"name": "Discount Coffee", "pricing": {"average_price": 3.00}},
                {"name": "Regular Cafe", "pricing": {"average_price": 5.00}}
            ]
        }
    )
    
    print("\n" + "=" * 70)
    print("  HOW TO USE THE FIELD")
    print("=" * 70)
    print("""
The 'price_difference_percent' field shows:
  
  - POSITIVE value = You're more expensive than competitors
    Example: 15.79 means you're 15.79% above market average
  
  - NEGATIVE value = You're cheaper than competitors  
    Example: -25.5 means you're 25.5% below market average
  
  - ZERO or near zero = Your pricing matches the market
    Example: 0.5 means within 0.5% of market average
  
  - NULL value = No pricing data available for comparison
    This happens when pricing data is missing or incomplete

Strategic Implications:
  - Above 20%: High risk, consider price adjustments
  - 10-20%: Moderate concern, justify premium with value
  - Within 10%: Competitive, maintain positioning
  - Below 10%: Price advantage, use in marketing
    """)
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
