"""
Test Agent C: The Strategist
Run the strategist with sample data and display results in business report format
"""

import json
from agent_c_strategist import AgentCStrategist


def print_business_report(strategy):
    """Print strategy in clean business report format"""
    print("\n" + "=" * 80)
    print("STRATEGIC RECOMMENDATION REPORT")
    print("=" * 80)
    
    print("\n📋 RECOMMENDED ACTION")
    print("-" * 80)
    print(f"{strategy['recommended_action']}")
    
    print(f"\n🎯 RESPONSE TYPE: {strategy['response_type'].upper().replace('_', ' ')}")
    
    print("\n💰 PRICING ACTION")
    print("-" * 80)
    print(f"{strategy['price_action']}")
    
    print("\n📢 CAMPAIGN IDEA")
    print("-" * 80)
    print(f"{strategy['campaign_idea']}")
    
    print("\n📱 MARKETING POST (Ready to publish)")
    print("-" * 80)
    print(strategy['marketing_post'])
    
    print("\n✅ CALL TO ACTION")
    print("-" * 80)
    print(f"{strategy['cta']}")
    
    print("\n📝 EXECUTION STEPS")
    print("-" * 80)
    for i, step in enumerate(strategy['execution_steps'], 1):
        print(f"{i}. {step}")
    
    print("\n💡 WHY THIS STRATEGY")
    print("-" * 80)
    for i, reason in enumerate(strategy['why_this_strategy'], 1):
        print(f"{i}. {reason}")
    
    print("\n" + "=" * 80)


def run_test():
    """Run test with sample data"""
    print("\n" + "#" * 80)
    print("# AGENT C: THE STRATEGIST - TEST RUN")
    print("#" * 80)
    
    # Sample business profile
    print("\n📋 Loading Business Profile...")
    business_profile = {
        "name": "Tony's Pizza Palace",
        "business_type": "pizza restaurant",
        "location": "Downtown",
        "unique_selling_points": [
            "Wood-fired oven",
            "Fresh ingredients daily",
            "Family recipes since 1985"
        ],
        "pricing": {
            "large_pizza": 17.99,
            "medium_pizza": 13.99,
            "small_pizza": 10.99
        },
        "target_audience": "families, young professionals, food enthusiasts"
    }
    print(f"   Business: {business_profile['name']}")
    print(f"   Type: {business_profile['business_type']}")
    print(f"   USPs: {', '.join(business_profile['unique_selling_points'])}")
    
    # Sample scout findings
    print("\n🔍 Loading Scout Findings...")
    scout_findings = {
        "scan_date": "2026-03-10",
        "competitors_found": 3,
        "competitors": [
            {
                "name": "Domino's Pizza",
                "prices": {"large": 14.99, "medium": 11.99},
                "promotions": ["50% off online orders - limited time"],
                "location": "2 blocks away"
            },
            {
                "name": "Pizza Hut",
                "prices": {"large": 16.99, "medium": 13.49},
                "promotions": ["Buy one get one 50% off"],
                "location": "Downtown"
            },
            {
                "name": "Papa John's",
                "prices": {"large": 15.99, "medium": 12.99},
                "promotions": [],
                "location": "Main Street"
            }
        ],
        "market_summary": "Competitive market with active promotional campaigns"
    }
    print(f"   Found {scout_findings['competitors_found']} competitors")
    for comp in scout_findings['competitors']:
        promo_info = f" (Promo: {comp['promotions'][0]})" if comp['promotions'] else ""
        print(f"   - {comp['name']}: ${comp['prices']['large']}{promo_info}")
    
    # Sample analyst output
    print("\n📊 Loading Analyst Output...")
    analyst_output = {
        "timestamp": "2026-03-10T14:30:00",
        "impact_level": "medium",
        "summary": "Two competitors running aggressive promotions creating temporary pricing pressure",
        "pricing_gap": "Your pricing is 15% above promotional prices but competitive with base pricing",
        "market_risk": "Medium risk - promotional activity from Domino's and Pizza Hut",
        "recommended_urgency": "medium",
        "key_insights": [
            "Domino's 50% off promotion poses immediate competitive threat",
            "Pizza Hut BOGO campaign targeting price-sensitive customers",
            "Your unique selling points (wood-fired, fresh ingredients) provide differentiation",
            "Base pricing remains competitive with Papa John's and Pizza Hut"
        ],
        "price_difference_percent": 15.0,
        "threat_score": 6.8,
        "response_type": "promotion_response",
        "competitor_breakdown": [
            {"name": "Domino's", "threat_level": "high", "reason": "Aggressive 50% off promotion"},
            {"name": "Pizza Hut", "threat_level": "medium", "reason": "BOGO campaign active"},
            {"name": "Papa John's", "threat_level": "low", "reason": "No active promotions"}
        ]
    }
    print(f"   Impact Level: {analyst_output['impact_level'].upper()}")
    print(f"   Threat Score: {analyst_output['threat_score']}/10")
    print(f"   Price Difference: {analyst_output['price_difference_percent']}%")
    print(f"   Urgency: {analyst_output['recommended_urgency'].upper()}")
    
    # Run the strategist
    print("\n🎯 Running Strategist Agent...")
    strategist = AgentCStrategist()
    strategy_json = strategist.strategize(
        business_profile,
        scout_findings,
        analyst_output
    )
    
    # Parse and display results
    strategy = json.loads(strategy_json)
    print("   ✓ Strategy generated successfully")
    
    # Print business report
    print_business_report(strategy)
    
    # Summary
    print("\n" + "#" * 80)
    print("# TEST COMPLETE")
    print("#" * 80)
    print(f"\n✓ Business: {business_profile['name']}")
    print(f"✓ Strategy Type: {strategy['response_type']}")
    print(f"✓ All fields generated successfully")
    print(f"✓ Ready for dashboard display")
    
    return strategy


if __name__ == "__main__":
    try:
        strategy = run_test()
        
        # Optional: Save to file
        print("\n💾 Saving strategy to file...")
        with open("strategy_output.json", "w", encoding="utf-8") as f:
            json.dump(strategy, f, indent=2, ensure_ascii=False)
        print("   ✓ Saved to strategy_output.json")
        
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
