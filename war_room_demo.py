"""
WAR ROOM DEMO - Complete Intelligence Pipeline
Scout → Analyst → Strategist
"""

import json
from agent_b_analyst import AgentBAnalyst
from agent_c_strategist import AgentCStrategist


def print_header(title):
    """Print section header"""
    print()
    print("=" * 80)
    print(f" {title}")
    print("=" * 80)
    print()


def print_arrow():
    """Print pipeline arrow"""
    print()
    print(" " * 35 + "↓")
    print()


def main():
    """Run complete intelligence pipeline"""
    
    print()
    print("█" * 80)
    print(" " * 25 + "WAR ROOM - MARKET INTELLIGENCE")
    print(" " * 28 + "Complete Analysis Pipeline")
    print("█" * 80)
    
    # Load data
    with open('example_business_profile.json', 'r') as f:
        business_profile = json.load(f)
    
    with open('example_competitor_findings.json', 'r') as f:
        scout_findings = json.load(f)
    
    # =========================================================================
    # STEP 1: SCOUT FINDINGS
    # =========================================================================
    print_header("STEP 1: SCOUT FINDINGS (Competitor Intelligence)")
    
    print(f"📡 Business Being Monitored: {business_profile['name']}")
    print(f"   Your Price: ${business_profile['pricing']['average_price']}")
    print(f"   Positioning: {business_profile.get('positioning', 'N/A')}")
    print()
    
    print(f"🔍 Competitors Discovered: {len(scout_findings['competitors'])}")
    print()
    
    for comp in scout_findings['competitors']:
        print(f"   • {comp['name']}")
        print(f"     Price: ${comp['pricing']['average_price']}")
        
        # Count promotions
        promo_count = len(comp.get('current_promotions', []))
        if promo_count > 0:
            print(f"     Promotions: {promo_count} active")
            for promo in comp['current_promotions'][:2]:
                print(f"       - {promo['title']}")
        
        # Count new products
        new_count = len(comp.get('new_products', []))
        if new_count > 0:
            print(f"     New Products: {new_count}")
        
        print()
    
    print_arrow()
    
    # =========================================================================
    # STEP 2: ANALYST EVALUATION
    # =========================================================================
    print_header("STEP 2: ANALYST EVALUATION (Competitive Impact)")
    
    print("🔬 Running competitive analysis...")
    print()
    
    # Initialize Agent B
    analyst = AgentBAnalyst()
    analysis_json = analyst.analyze(business_profile, scout_findings)
    analysis = json.loads(analysis_json)
    
    # Display impact assessment
    impact_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}.get(analysis['impact_level'].lower(), "⚪")
    urgency_emoji = {"low": "🟢", "medium": "🟡", "high": "🔴"}.get(analysis['recommended_urgency'].lower(), "⚪")
    
    print(f"{impact_emoji} IMPACT LEVEL: {analysis['impact_level'].upper()}")
    print(f"{urgency_emoji} URGENCY: {analysis['recommended_urgency'].upper()}")
    
    # Display threat score with visual indicator
    if analysis.get('threat_score') is not None:
        threat_score = analysis['threat_score']
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
    print()
    
    print("💡 KEY INSIGHTS:")
    for i, insight in enumerate(analysis['key_insights'], 1):
        print(f"   {i}. {insight}")
    print()
    
    print("💰 PRICING POSITION:")
    if analysis.get('price_difference_percent'):
        diff = analysis['price_difference_percent']
        if diff > 0:
            print(f"   You're {diff:.1f}% MORE expensive than average")
        else:
            print(f"   You're {abs(diff):.1f}% LESS expensive than average")
    print()
    
    print("📊 MARKET SUMMARY:")
    print(f"   {analysis['summary'][:200]}...")
    print()
    
    print_arrow()
    
    # =========================================================================
    # STEP 3: STRATEGIST RECOMMENDATIONS
    # =========================================================================
    print_header("STEP 3: STRATEGIST RECOMMENDATIONS (Action Plan)")
    
    print("🎯 Generating strategic action plan...")
    print()
    
    # Initialize Agent C
    strategist = AgentCStrategist()
    strategy_json = strategist.strategize(analysis_json, business_profile)
    strategy = json.loads(strategy_json)
    
    # Display recommendations
    print("⚡ PRIORITY ACTIONS:")
    for i, action in enumerate(strategy['priority_actions'], 1):
        print(f"   {i}. {action}")
    print()
    
    print("💵 PRICING STRATEGY:")
    for i, tactic in enumerate(strategy['pricing_strategy'], 1):
        print(f"   {i}. {tactic}")
    print()
    
    print("📢 MARKETING TACTICS:")
    for i, tactic in enumerate(strategy['marketing_tactics'], 1):
        print(f"   {i}. {tactic}")
    print()
    
    print("🛡️  RISK MITIGATION:")
    for i, action in enumerate(strategy['risk_mitigation'], 1):
        print(f"   {i}. {action}")
    print()
    
    # Timeline
    print("⏱️  ACTION TIMELINE:")
    timeline = strategy.get('timeline', {})
    print(f"   Immediate: {timeline.get('immediate', 'N/A')}")
    print(f"   Short-term: {timeline.get('short_term', 'N/A')}")
    print(f"   Medium-term: {timeline.get('medium_term', 'N/A')}")
    print()
    
    # Success metrics
    print("📈 SUCCESS METRICS TO TRACK:")
    for metric in strategy.get('success_metrics', []):
        print(f"   • {metric}")
    print()
    
    # =========================================================================
    # FINAL SUMMARY
    # =========================================================================
    print()
    print("=" * 80)
    print(" PIPELINE COMPLETE")
    print("=" * 80)
    print()
    print(f"✓ Scout discovered {len(scout_findings['competitors'])} competitors")
    print(f"✓ Analyst assessed {analysis['impact_level'].upper()} impact")
    print(f"✓ Strategist generated {len(strategy['priority_actions'])} priority actions")
    print()
    print("Next Steps:")
    print("  1. Review priority actions with leadership team")
    print("  2. Allocate budget for recommended tactics")
    print("  3. Begin implementation according to timeline")
    print("  4. Monitor success metrics weekly")
    print()
    print("=" * 80)
    print()


if __name__ == "__main__":
    main()
