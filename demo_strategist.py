"""
Demo: Agent C The Strategist
Shows how to use the strategist agent with different scenarios
"""

import json
from agent_c_strategist import AgentCStrategist


def demo_hold_position():
    """Demo: Hold position when pricing is competitive"""
    print("\n" + "="*60)
    print("SCENARIO 1: HOLD POSITION")
    print("="*60)
    
    business_profile = {
        "name": "Mike's Pizza Palace",
        "business_type": "pizza restaurant",
        "unique_selling_points": [
            "Fresh ingredients daily",
            "Family recipes since 1985"
        ],
        "pricing": {"large_pizza": 16.99}
    }
    
    scout_findings = {
        "competitors": [
            {"name": "Pizza Hut", "price": 15.99},
            {"name": "Domino's", "price": 17.99}
        ]
    }
    
    analyst_output = {
        "impact_level": "low",
        "price_difference_percent": 2.5,
        "threat_score": 3.5,
        "recommended_urgency": "low",
        "response_type": "hold_position",
        "key_insights": [
            "Pricing is competitive within market range",
            "No aggressive promotions detected"
        ]
    }
    
    strategist = AgentCStrategist()
    result = strategist.strategize(business_profile, scout_findings, analyst_output)
    
    print(result)
    return result


def demo_promotion_response():
    """Demo: Respond to competitor promotions"""
    print("\n" + "="*60)
    print("SCENARIO 2: PROMOTION RESPONSE")
    print("="*60)
    
    business_profile = {
        "name": "Tony's Pizza",
        "business_type": "pizza restaurant",
        "unique_selling_points": ["Wood-fired oven"],
        "pricing": {"large_pizza": 17.99}
    }
    
    scout_findings = {
        "competitors": [
            {"name": "Domino's", "promotion": "50% off online orders"},
            {"name": "Papa Johns", "promotion": "Buy one get one free"}
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
            "Your base pricing is still competitive",
            "Promotion-based competition detected"
        ]
    }
    
    strategist = AgentCStrategist()
    result = strategist.strategize(business_profile, scout_findings, analyst_output)
    
    print(result)
    return result


def demo_price_adjustment():
    """Demo: Price adjustment needed"""
    print("\n" + "="*60)
    print("SCENARIO 3: PRICE ADJUSTMENT")
    print("="*60)
    
    business_profile = {
        "name": "Quick Pizza",
        "business_type": "pizza restaurant",
        "unique_selling_points": [],
        "pricing": {"large_pizza": 19.99}
    }
    
    scout_findings = {
        "competitors": [
            {"name": "Budget Pizza", "price": 12.99},
            {"name": "Cheap Eats Pizza", "price": 13.99}
        ]
    }
    
    analyst_output = {
        "impact_level": "high",
        "price_difference_percent": 35.0,
        "threat_score": 8.5,
        "recommended_urgency": "high",
        "response_type": "price_adjustment",
        "key_insights": [
            "You're 35% more expensive than competitors",
            "High risk of losing price-sensitive customers",
            "No unique differentiators identified"
        ]
    }
    
    strategist = AgentCStrategist()
    result = strategist.strategize(business_profile, scout_findings, analyst_output)
    
    print(result)
    return result


def demo_product_differentiation():
    """Demo: Differentiate on quality/features"""
    print("\n" + "="*60)
    print("SCENARIO 4: PRODUCT DIFFERENTIATION")
    print("="*60)
    
    business_profile = {
        "name": "Artisan Pizza Co.",
        "business_type": "gourmet pizza restaurant",
        "unique_selling_points": [
            "Organic ingredients",
            "Chef-crafted recipes",
            "Award-winning pizzaiolo"
        ],
        "pricing": {"large_pizza": 22.99}
    }
    
    scout_findings = {
        "competitors": [
            {"name": "Chain Pizza A", "price": 15.99},
            {"name": "Chain Pizza B", "price": 16.99}
        ]
    }
    
    analyst_output = {
        "impact_level": "medium",
        "price_difference_percent": 35.0,
        "threat_score": 5.5,
        "recommended_urgency": "medium",
        "response_type": "product_differentiation",
        "key_insights": [
            "Premium positioning with unique selling points",
            "Different target audience than budget competitors",
            "Quality-focused customers less price-sensitive"
        ]
    }
    
    strategist = AgentCStrategist()
    result = strategist.strategize(business_profile, scout_findings, analyst_output)
    
    print(result)
    return result


def demo_all_scenarios():
    """Run all demo scenarios"""
    print("\n" + "#"*60)
    print("# AGENT C: THE STRATEGIST - DEMO")
    print("# Testing all response strategy types")
    print("#"*60)
    
    scenarios = [
        ("Hold Position", demo_hold_position),
        ("Promotion Response", demo_promotion_response),
        ("Price Adjustment", demo_price_adjustment),
        ("Product Differentiation", demo_product_differentiation)
    ]
    
    results = {}
    for name, demo_func in scenarios:
        try:
            result = demo_func()
            results[name] = json.loads(result)
        except Exception as e:
            print(f"\nError in {name}: {e}")
            results[name] = {"error": str(e)}
    
    print("\n" + "="*60)
    print("SUMMARY: All Strategies Tested")
    print("="*60)
    for name, result in results.items():
        if "error" not in result:
            print(f"✓ {name}: {result['response_type']}")
        else:
            print(f"✗ {name}: Error")
    
    return results


if __name__ == "__main__":
    # Run all scenarios
    demo_all_scenarios()
    
    print("\n" + "#"*60)
    print("# Demo complete!")
    print("# Agent C generates:")
    print("#   - Clear action recommendations")
    print("#   - Pricing guidance")
    print("#   - Campaign ideas")
    print("#   - Ready-to-use marketing posts")
    print("#   - Execution steps")
    print("#   - Strategy rationale")
    print("#"*60)
