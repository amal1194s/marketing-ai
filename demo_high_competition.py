"""
Demo: High Competition Scenario
Shows Agent B analyzing a serious competitive threat
"""

import json
from agent_b_analyst import AgentBAnalyst


def run_high_competition_scenario():
    """Demonstrate analysis of aggressive competitive environment"""
    
    print("\n" + "=" * 70)
    print(" HIGH COMPETITION SCENARIO - Agent B Analysis Demo")
    print("=" * 70)
    
    agent = AgentBAnalyst()
    
    # Load standard business profile
    with open('example_business_profile.json', 'r') as f:
        business = json.load(f)
    
    # Load high competition scenario
    with open('scenario_high_competition.json', 'r') as f:
        competitors = json.load(f)
    
    print(f"\nBusiness: {business['name']}")
    print(f"Your Average Price: ${business['pricing']['average_price']:.2f}")
    print(f"Your Positioning: {business['positioning']}")
    print(f"\nCompetitors Detected: {len(competitors['competitors'])}")
    
    for comp in competitors['competitors']:
        print(f"  - {comp['name']} (avg ${comp['pricing']['average_price']:.2f})")
    
    print("\n" + "-" * 70)
    print("RUNNING COMPETITIVE ANALYSIS...")
    print("-" * 70 + "\n")
    
    # Analyze
    result_json = agent.analyze(business, competitors)
    result = json.loads(result_json)
    
    # Display results with formatting
    impact_emoji = {
        "high": "🔴",
        "medium": "🟡", 
        "low": "🟢"
    }
    
    print(f"\n{'=' * 70}")
    print(f" ANALYSIS RESULTS")
    print(f"{'=' * 70}\n")
    
    print(f"{impact_emoji.get(result['impact_level'], '')} IMPACT LEVEL: {result['impact_level'].upper()}")
    print(f"{impact_emoji.get(result['recommended_urgency'], '')} URGENCY: {result['recommended_urgency'].upper()}")
    print()
    
    print("📊 EXECUTIVE SUMMARY")
    print("-" * 70)
    print(f"{result['summary']}")
    print()
    
    print("💰 PRICING ANALYSIS")
    print("-" * 70)
    print(f"{result['pricing_gap']}")
    print()
    
    print("⚠️  MARKET RISK ASSESSMENT")
    print("-" * 70)
    print(f"{result['market_risk']}")
    print()
    
    print("💡 KEY STRATEGIC INSIGHTS")
    print("-" * 70)
    for i, insight in enumerate(result['key_insights'], 1):
        print(f"{i}. {insight}")
    print()
    
    print("=" * 70)
    print(" RECOMMENDED ACTIONS")
    print("=" * 70)
    
    # Provide scenario-specific recommendations
    if result['recommended_urgency'] == 'high':
        print("""
✓ Schedule emergency strategy meeting within 48 hours
✓ Review pricing strategy - consider competitive matching
✓ Launch counter-promotion to retain customers
✓ Strengthen value proposition messaging
✓ Increase customer engagement and loyalty efforts
✓ Monitor competitor activity daily
        """)
    elif result['recommended_urgency'] == 'medium':
        print("""
✓ Review strategy within 1-2 weeks
✓ Evaluate promotional calendar
✓ Consider product menu refresh
✓ Enhance customer communication
✓ Monitor competitor activity weekly
        """)
    else:
        print("""
✓ Continue current strategy
✓ Maintain quality and service standards
✓ Monitor competitor activity monthly
✓ Focus on customer retention
        """)
    
    print("\n" + "=" * 70)
    print("\nFull JSON Output:")
    print(result_json)
    print()


if __name__ == "__main__":
    run_high_competition_scenario()
