"""
Full Pipeline Integration Example
Shows Scout -> Analyst -> Strategist working together
"""

import json
from agent_c_strategist import AgentCStrategist


# Simulate the full pipeline
def run_full_pipeline_simulation():
    """
    Simulates the complete three-agent pipeline:
    1. Scout Agent finds competitor data
    2. Analyst Agent evaluates impact
    3. Strategist Agent recommends action
    """
    
    print("="*70)
    print("MULTI-AGENT MARKET INTELLIGENCE SYSTEM")
    print("Full Pipeline Simulation")
    print("="*70)
    
    # STEP 1: Business Profile (from database/config)
    print("\n📋 STEP 1: Business Profile")
    print("-" * 70)
    business_profile = {
        "name": "Mike's Pizza Palace",
        "business_type": "pizza restaurant",
        "location": "Downtown",
        "unique_selling_points": [
            "Fresh ingredients daily",
            "Family recipes since 1985",
            "Wood-fired oven"
        ],
        "pricing": {
            "large_pizza": 16.99,
            "medium_pizza": 13.99,
            "small_pizza": 10.99
        },
        "target_audience": "families, young professionals"
    }
    print(json.dumps(business_profile, indent=2))
    
    # STEP 2: Scout Agent Output (simulated)
    print("\n🔍 STEP 2: Scout Agent - Competitor Findings")
    print("-" * 70)
    scout_findings = {
        "scan_date": "2026-03-10",
        "competitors_found": 3,
        "competitors": [
            {
                "name": "Domino's Pizza",
                "prices": {"large": 15.99, "medium": 12.99},
                "promotions": ["50% off online orders this week"],
                "location": "2 blocks away"
            },
            {
                "name": "Pizza Hut",
                "prices": {"large": 16.99, "medium": 13.99},
                "promotions": [],
                "location": "Downtown"
            },
            {
                "name": "Papa John's",
                "prices": {"large": 14.99, "medium": 11.99},
                "promotions": ["Buy one get one 25% off"],
                "location": "Main Street"
            }
        ],
        "market_summary": "Competitive market with active promotions"
    }
    print(json.dumps(scout_findings, indent=2))
    
    # STEP 3: Analyst Agent Output (simulated)
    print("\n📊 STEP 3: Analyst Agent - Impact Analysis")
    print("-" * 70)
    analyst_output = {
        "timestamp": "2026-03-10T14:30:00",
        "impact_level": "medium",
        "summary": "Competitors running promotions. Your base pricing is competitive but promotional activity creates temporary pressure.",
        "pricing_gap": "Your pricing is within 6% of market average",
        "market_risk": "Medium risk from aggressive promotions by 2 competitors",
        "recommended_urgency": "medium",
        "key_insights": [
            "Domino's aggressive 50% off promotion poses immediate threat",
            "Your base pricing remains competitive with Pizza Hut",
            "Papa John's targeting price-sensitive customers with BOGO",
            "Your unique selling points provide differentiation opportunity"
        ],
        "price_difference_percent": 6.0,
        "threat_score": 6.5,
        "response_type": "promotion_response",
        "competitor_breakdown": [
            {"name": "Domino's", "threat_level": "high", "reason": "Aggressive promotion"},
            {"name": "Pizza Hut", "threat_level": "low", "reason": "Similar pricing"},
            {"name": "Papa John's", "threat_level": "medium", "reason": "Lower base price"}
        ]
    }
    print(json.dumps(analyst_output, indent=2))
    
    # STEP 4: Strategist Agent - Action Plan
    print("\n🎯 STEP 4: Strategist Agent - Action Plan")
    print("-" * 70)
    
    strategist = AgentCStrategist()
    strategy_json = strategist.strategize(
        business_profile,
        scout_findings,
        analyst_output
    )
    strategy = json.loads(strategy_json)
    
    print(json.dumps(strategy, indent=2))
    
    # STEP 5: Dashboard View (formatted output)
    print("\n" + "="*70)
    print("📱 DASHBOARD VIEW - READY FOR BUSINESS OWNER")
    print("="*70)
    
    print(f"\n🎯 RECOMMENDED ACTION:")
    print(f"   {strategy['recommended_action']}")
    
    print(f"\n💰 PRICING GUIDANCE:")
    print(f"   {strategy['price_action']}")
    
    print(f"\n📢 CAMPAIGN IDEA:")
    print(f"   {strategy['campaign_idea']}")
    
    print(f"\n📱 READY-TO-POST (copy & paste to social media):")
    print("   " + "-"*66)
    for line in strategy['marketing_post'].split('\n'):
        print(f"   {line}")
    print("   " + "-"*66)
    
    print(f"\n✅ CALL TO ACTION:")
    print(f"   {strategy['cta']}")
    
    print(f"\n📋 NEXT STEPS:")
    for i, step in enumerate(strategy['execution_steps'], 1):
        print(f"   {i}. {step}")
    
    print(f"\n💡 WHY THIS STRATEGY:")
    for i, reason in enumerate(strategy['why_this_strategy'], 1):
        print(f"   {i}. {reason}")
    
    print("\n" + "="*70)
    print("✓ Pipeline Complete - Strategy Ready for Implementation")
    print("="*70)
    
    return {
        "business_profile": business_profile,
        "scout_findings": scout_findings,
        "analyst_output": analyst_output,
        "strategy": strategy
    }


def show_pipeline_flow():
    """Show the data flow through the system"""
    print("\n" + "="*70)
    print("PIPELINE ARCHITECTURE")
    print("="*70)
    print("""
    ┌─────────────────────────────────────────────────────────────────┐
    │  INPUT: Business Profile + Competitor Data                     │
    └─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │  AGENT A: SCOUT                                                 │
    │  Finds competitor pricing, promotions, activity                 │
    └─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │  AGENT B: ANALYST                                               │
    │  Analyzes threat level, pricing gap, impact                     │
    └─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │  AGENT C: STRATEGIST ← YOU ARE HERE                             │
    │  Generates action plan, marketing content, recommendations      │
    └─────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
    ┌─────────────────────────────────────────────────────────────────┐
    │  OUTPUT: Dashboard-Ready Business Actions                       │
    │  • Recommended action                                           │
    │  • Pricing guidance                                             │
    │  • Marketing content (ready to post)                            │
    │  • Execution steps                                              │
    │  • Strategy rationale                                           │
    └─────────────────────────────────────────────────────────────────┘
    """)


if __name__ == "__main__":
    # Show architecture
    show_pipeline_flow()
    
    # Run full simulation
    print("\n\n")
    results = run_full_pipeline_simulation()
    
    print("\n\n" + "="*70)
    print("INTEGRATION NOTES")
    print("="*70)
    print("""
Agent C: The Strategist is designed to be:

✓ PRACTICAL - Recommendations are feasible for small businesses
✓ CLEAR - No jargon, business-friendly language
✓ ACTIONABLE - Every output can be implemented immediately
✓ DASHBOARD-READY - JSON format perfect for UI display
✓ COMPLETE - Includes marketing content, not just strategy

Integration Points:
- Accepts JSON or dict inputs
- Returns valid JSON with all required fields
- Handles errors gracefully
- Works with partial data (optional fields)
- Stateless - no database dependencies

Usage in Production:
1. Collect business profile (one-time setup)
2. Run Scout Agent periodically (daily/weekly)
3. Run Analyst Agent on scout findings
4. Run Strategist Agent to generate action plan
5. Display results in dashboard
6. Let business owner execute recommendations
    """)
