"""
Test script for Agent B: The Analyst
Easily test the agent with custom data
"""

import json
from agent_b_analyst import AgentBAnalyst


def test_agent():
    """Test Agent B with example data"""
    
    print()
    print("=" * 70)
    print(" Agent B: The Analyst - Market Intelligence System")
    print("=" * 70)
    
    # Initialize agent
    agent = AgentBAnalyst()
    
    # Load business profile
    with open('example_business_profile.json', 'r') as f:
        business_profile = json.load(f)
    
    # Load competitor findings
    with open('example_competitor_findings.json', 'r') as f:
        competitor_findings = json.load(f)
    
    # Display business info
    print()
    print("=" * 70)
    print(" COMPETITIVE ANALYSIS REPORT")
    print("=" * 70)
    print()
    print(f"Business: {business_profile['name']}")
    print(f"Your Average Price: ${business_profile['pricing']['average_price']}")
    
    comp_names = [c['name'] for c in competitor_findings['competitors']]
    print(f"Competitors: {', '.join(comp_names)}")
    print()
    print("-" * 70)
    print("RUNNING ANALYSIS...")
    print("-" * 70)
    
    # Run analysis
    result_json = agent.analyze(business_profile, competitor_findings)
    result = json.loads(result_json)
    
    # Display results with improved formatting
    print()
    print("=" * 70)
    print(" ANALYSIS RESULTS")
    print("=" * 70)
    print()
    
    # Impact and Urgency with color indicators
    impact_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}.get(result['impact_level'].lower(), "⚪")
    urgency_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}.get(result['recommended_urgency'].lower(), "⚪")
    
    print(f"{impact_emoji} IMPACT LEVEL: {result['impact_level'].upper()}")
    print(f"{urgency_emoji} URGENCY: {result['recommended_urgency'].upper()}")
    
    # Threat Score with visual indicator
    if result.get('threat_score') is not None:
        threat_score = result['threat_score']
        if threat_score >= 8.0:
            threat_emoji = "🔴"
            threat_level = "CRITICAL"
        elif threat_score >= 6.0:
            threat_emoji = "🟠"
            threat_level = "HIGH"
        elif threat_score >= 4.0:
            threat_emoji = "🟡"
            threat_level = "MODERATE"
        else:
            threat_emoji = "🟢"
            threat_level = "LOW"
        
        print(f"{threat_emoji} THREAT SCORE: {threat_score:.1f}/10 ({threat_level})")
        if result.get('threat_score_formula'):
            print(f"   Formula: {result['threat_score_formula']}")
    
    # Recommended Response
    if result.get('response_type'):
        response_type = result['response_type']
        response_emoji = {
            "hold_position": "🛡️",
            "promotion_response": "🎯",
            "price_adjustment": "💵",
            "product_differentiation": "🚀"
        }.get(response_type, "📋")
        
        response_label = response_type.replace("_", " ").title()
        print(f"{response_emoji} RECOMMENDED RESPONSE: {response_label}")
    print()
    
    # Executive Summary
    print("📊 EXECUTIVE SUMMARY")
    print("-" * 70)
    print(result['summary'])
    print()
    
    # Pricing Analysis
    print("💰 PRICING ANALYSIS")
    print("-" * 70)
    print(result['pricing_gap'])
    if result.get('price_difference_percent') is not None:
        print(f"Price Difference: {result['price_difference_percent']:.1f}%")
    print()
    
    # Market Risk
    print("⚠️  MARKET RISK ASSESSMENT")
    print("-" * 70)
    print(result['market_risk'])
    print()
    
    # Key Insights
    print("💡 KEY STRATEGIC INSIGHTS")
    print("-" * 70)
    for i, insight in enumerate(result['key_insights'], 1):
        print(f"{i}. {insight}")
    print()
    
    # Competitor Breakdown
    if result.get('competitor_breakdown'):
        print("🎯 COMPETITOR BREAKDOWN")
        print("-" * 70)
        for comp in result['competitor_breakdown']:
            comp_name = comp.get('competitor_name', 'Unknown')
            threat_level = comp.get('threat_level', 'unknown').upper()
            reasons = comp.get('reasons', [])
            
            # Threat level emoji
            threat_emoji = {
                "HIGH": "🔴",
                "MEDIUM": "🟡",
                "LOW": "🟢"
            }.get(threat_level, "⚪")
            
            print(f"\n{threat_emoji} {comp_name} - {threat_level} Threat")
            for reason in reasons:
                print(f"   • {reason}")
        print()
    
    print("=" * 70)
    print()


if __name__ == "__main__":
    test_agent()
