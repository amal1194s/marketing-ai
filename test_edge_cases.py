"""
Edge Case Tests for Agent B: The Analyst
Tests robustness and error handling
"""

import json
from agent_b_analyst import AgentBAnalyst


def test_edge_cases():
    """Test Agent B with various edge cases"""
    
    agent = AgentBAnalyst()
    
    print("=" * 70)
    print("AGENT B - EDGE CASE TESTING")
    print("=" * 70)
    print()
    
    # Test 1: Empty inputs
    print("Test 1: Empty inputs")
    print("-" * 70)
    result = agent.analyze({}, {})
    parsed = json.loads(result)
    print(f"✓ Returns valid JSON: {parsed['impact_level']}")
    print(f"  Summary: {parsed['summary'][:60]}...")
    print()
    
    # Test 2: No competitors
    print("Test 2: No competitors in data")
    print("-" * 70)
    result = agent.analyze(
        {"name": "Test Business", "pricing": {"average_price": 10}},
        {"competitors": []}
    )
    parsed = json.loads(result)
    print(f"✓ Returns valid JSON: {parsed['impact_level']}")
    print(f"  Summary: {parsed['summary'][:60]}...")
    print()
    
    # Test 3: Missing pricing data
    print("Test 3: Missing pricing data")
    print("-" * 70)
    result = agent.analyze(
        {"name": "Test Business"},
        {
            "competitors": [
                {"name": "Competitor A", "promotions": ["Sale"]}
            ]
        }
    )
    parsed = json.loads(result)
    print(f"✓ Returns valid JSON: {parsed['impact_level']}")
    print(f"  Insights count: {len(parsed['key_insights'])}")
    print()
    
    # Test 4: Malformed pricing
    print("Test 4: Malformed pricing data")
    print("-" * 70)
    result = agent.analyze(
        {"name": "Test", "pricing": {"average_price": "not a number"}},
        {"competitors": [{"name": "A", "pricing": {"average_price": 5}}]}
    )
    parsed = json.loads(result)
    print(f"✓ Returns valid JSON: {parsed['impact_level']}")
    print()
    
    # Test 5: Only pricing, no offers
    print("Test 5: Only pricing data, no promotions")
    print("-" * 70)
    result = agent.analyze(
        {
            "name": "Test Business",
            "pricing": {"average_price": 8.00, "min_price": 5, "max_price": 12}
        },
        {
            "competitors": [
                {
                    "name": "Cheap Competitor",
                    "pricing": {"average_price": 4.00}
                }
            ]
        }
    )
    parsed = json.loads(result)
    print(f"✓ Returns valid JSON: {parsed['impact_level']}")
    print(f"  Pricing gap analysis: {parsed['pricing_gap'][:80]}...")
    print()
    
    # Test 6: Extreme price differences
    print("Test 6: Extreme price differences (100%+)")
    print("-" * 70)
    result = agent.analyze(
        {"name": "Premium", "pricing": {"average_price": 100}},
        {"competitors": [{"name": "Budget", "pricing": {"average_price": 10}}]}
    )
    parsed = json.loads(result)
    print(f"✓ Impact level: {parsed['impact_level']}")
    print(f"  Urgency: {parsed['recommended_urgency']}")
    print()
    
    # Test 7: Many aggressive promotions
    print("Test 7: Many aggressive promotions")
    print("-" * 70)
    result = agent.analyze(
        {"name": "Business", "pricing": {"average_price": 10}},
        {
            "competitors": [
                {
                    "name": "Aggressive Competitor",
                    "pricing": {"average_price": 9},
                    "promotions": [
                        "50% off everything",
                        "Buy one get one free",
                        "Free shipping on all orders",
                        "40% discount today only"
                    ]
                }
            ]
        }
    )
    parsed = json.loads(result)
    print(f"✓ Impact level: {parsed['impact_level']}")
    print(f"  Urgency: {parsed['recommended_urgency']}")
    print(f"  First insight: {parsed['key_insights'][0][:70]}...")
    print()
    
    # Test 8: Unicode and special characters
    print("Test 8: Unicode and special characters")
    print("-" * 70)
    result = agent.analyze(
        {"name": "Café Résumé & Co.", "pricing": {"average_price": 5.99}},
        {"competitors": [{"name": "Competitor™", "pricing": {"average_price": 6.00}}]}
    )
    parsed = json.loads(result)
    print(f"✓ Returns valid JSON with special chars")
    print()
    
    # Test 9: Very large competitor list
    print("Test 9: Many competitors")
    print("-" * 70)
    competitors = [
        {
            "name": f"Competitor {i}",
            "pricing": {"average_price": 5 + i * 0.5},
            "promotions": [f"Promo {i}"] if i % 2 == 0 else []
        }
        for i in range(20)
    ]
    result = agent.analyze(
        {"name": "Business", "pricing": {"average_price": 10}},
        {"competitors": competitors}
    )
    parsed = json.loads(result)
    print(f"✓ Handles {len(competitors)} competitors")
    print(f"  Impact level: {parsed['impact_level']}")
    print()
    
    # Test 10: None and null values
    print("Test 10: None/null values in data")
    print("-" * 70)
    result = agent.analyze(
        {"name": None, "pricing": None, "target_audience": None},
        {"competitors": [{"name": "Test", "pricing": None, "promotions": None}]}
    )
    parsed = json.loads(result)
    print(f"✓ Handles None values: {parsed['impact_level']}")
    print()
    
    print("=" * 70)
    print("ALL EDGE CASES PASSED ✓")
    print("Agent B is robust and always returns valid JSON")
    print("=" * 70)


if __name__ == "__main__":
    try:
        test_edge_cases()
    except Exception as e:
        print(f"❌ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
