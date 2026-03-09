"""
Test suite for upgraded Analyst Agent with Opportunity Score
Tests the calculate_opportunity_score and classify_impact functions
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from agents.analyst_agent import (
    calculate_opportunity_score,
    classify_impact,
    analyze_signal
)


def test_opportunity_score_scenarios():
    """Test various opportunity score calculations"""
    
    print("=" * 70)
    print("Testing Opportunity Score Calculations")
    print("=" * 70)
    print()
    
    business = {
        "business_name": "Tony's Pizza",
        "product": "Veg Pizza",
        "price": 350,
        "location": "Coimbatore"
    }
    
    test_cases = [
        {
            "name": "Aggressive Promotion - 15% Cheaper",
            "signal": {
                "competitor": "Dominos",
                "product": "Farmhouse Pizza",
                "event_type": "promotion",
                "price": 299,
                "offer": "Buy 1 Get 1"
            },
            "expected_score_range": (8, 9),
            "expected_impact": "high"
        },
        {
            "name": "Deep Discount - 43% Cheaper",
            "signal": {
                "competitor": "Pizza Hut",
                "product": "Margherita",
                "event_type": "discount",
                "price": 199,
                "offer": "30% off"
            },
            "expected_score_range": (9, 10),
            "expected_impact": "high"
        },
        {
            "name": "Premium Launch - More Expensive",
            "signal": {
                "competitor": "Papa John's",
                "product": "Supreme Pizza",
                "event_type": "launch",
                "price": 399,
                "offer": "New product"
            },
            "expected_score_range": (5, 7),
            "expected_impact": "medium"
        },
        {
            "name": "Moderate Price Drop - 29% Cheaper",
            "signal": {
                "competitor": "Local Pizza Co",
                "product": "Cheese Pizza",
                "event_type": "price_update",
                "price": 249,
                "offer": ""
            },
            "expected_score_range": (7, 8),
            "expected_impact": "medium"
        },
        {
            "name": "Standard Pricing - More Expensive",
            "signal": {
                "competitor": "Premium Pizza",
                "product": "Deluxe",
                "event_type": "standard",
                "price": 450,
                "offer": ""
            },
            "expected_score_range": (4, 6),
            "expected_impact": "medium"
        },
        {
            "name": "Minimal Threat - Much More Expensive",
            "signal": {
                "competitor": "Luxury Pizza",
                "product": "Gold Pizza",
                "event_type": "standard",
                "price": 550,
                "offer": ""
            },
            "expected_score_range": (4, 6),
            "expected_impact": "medium"
        },
        {
            "name": "Missing Price - Promotion Event",
            "signal": {
                "competitor": "Mystery Competitor",
                "product": "Unknown",
                "event_type": "promotion",
                "price": 0,
                "offer": "Special deal"
            },
            "expected_score_range": (6, 8),
            "expected_impact": "medium"
        },
        {
            "name": "Slightly Cheaper - 5% Discount",
            "signal": {
                "competitor": "Nearby Pizza",
                "product": "Basic Pizza",
                "event_type": "discount",
                "price": 333,
                "offer": "5% off"
            },
            "expected_score_range": (7, 8),
            "expected_impact": "medium"
        }
    ]
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(test_cases, 1):
        print(f"Test {i}: {test['name']}")
        print("-" * 70)
        
        signal = test['signal']
        expected_range = test['expected_score_range']
        expected_impact = test['expected_impact']
        
        # Calculate score
        score = calculate_opportunity_score(signal, business)
        impact = classify_impact(score)
        
        # Calculate price difference
        price_diff = signal['price'] - business['price']
        percent_diff = (price_diff / business['price']) * 100 if business['price'] > 0 else 0
        
        # Display results
        print(f"  Competitor: {signal['competitor']}")
        print(f"  Price: ₹{signal['price']} (User: ₹{business['price']})")
        print(f"  Difference: ₹{price_diff} ({percent_diff:.1f}%)")
        print(f"  Event Type: {signal['event_type']}")
        print(f"  Calculated Score: {score}/10")
        print(f"  Impact Level: {impact.upper()}")
        
        # Validate
        score_valid = expected_range[0] <= score <= expected_range[1]
        impact_valid = impact == expected_impact
        
        if score_valid and impact_valid:
            print(f"  ✓ PASS")
            passed += 1
        else:
            print(f"  ✗ FAIL")
            if not score_valid:
                print(f"    Expected score in range {expected_range}, got {score}")
            if not impact_valid:
                print(f"    Expected impact '{expected_impact}', got '{impact}'")
            failed += 1
        
        print()
    
    print("=" * 70)
    print(f"Test Results: {passed} passed, {failed} failed")
    print("=" * 70)
    print()
    
    return failed == 0


def test_full_analysis():
    """Test full signal analysis with opportunity score"""
    
    print("=" * 70)
    print("Testing Full Analysis Pipeline")
    print("=" * 70)
    print()
    
    business = {
        "business_name": "Tony's Pizza",
        "product": "Veg Pizza",
        "price": 350,
        "location": "Coimbatore"
    }
    
    signal = {
        "competitor": "Dominos",
        "product": "Farmhouse Pizza",
        "event_type": "promotion",
        "price": 299,
        "offer": "Buy 1 Get 1",
        "timestamp": "2026-03-09T10:30:00"
    }
    
    print(f"Analyzing: {signal['competitor']} - {signal['event_type']}")
    print()
    
    result = analyze_signal(signal, business)
    
    # Display full result
    print("Analysis Result:")
    print("-" * 70)
    print(f"Competitor:         {result['competitor']}")
    print(f"Event Type:         {result['event_type']}")
    print(f"Competitor Price:   ₹{result['competitor_price']}")
    print(f"User Price:         ₹{result['user_price']}")
    print(f"Price Difference:   ₹{result['price_difference']}")
    print(f"Opportunity Score:  {result['opportunity_score']}/10")
    print(f"Impact Level:       {result['impact_level'].upper()}")
    print()
    print("Insight:")
    print(f"  {result['insight']}")
    print()
    
    # Validate required fields
    required_fields = [
        'competitor', 'event_type', 'competitor_price', 'user_price',
        'price_difference', 'opportunity_score', 'impact_level', 'insight'
    ]
    
    all_present = all(field in result for field in required_fields)
    
    if all_present:
        print("✓ All required fields present")
        return True
    else:
        missing = [f for f in required_fields if f not in result]
        print(f"✗ Missing fields: {missing}")
        return False


def test_edge_cases():
    """Test edge cases and error handling"""
    
    print("=" * 70)
    print("Testing Edge Cases")
    print("=" * 70)
    print()
    
    business = {
        "business_name": "Test Business",
        "product": "Test Product",
        "price": 350
    }
    
    edge_cases = [
        {
            "name": "Zero Competitor Price",
            "signal": {"competitor": "Test", "price": 0, "event_type": "standard", "offer": ""},
            "should_succeed": True
        },
        {
            "name": "Negative Prices Handled",
            "signal": {"competitor": "Test", "price": -100, "event_type": "discount", "offer": ""},
            "should_succeed": True  # Should be converted to 0
        },
        {
            "name": "Missing Event Type",
            "signal": {"competitor": "Test", "price": 300, "offer": ""},
            "should_succeed": True
        },
        {
            "name": "Missing Offer Field",
            "signal": {"competitor": "Test", "price": 300, "event_type": "promotion"},
            "should_succeed": True
        }
    ]
    
    passed = 0
    failed = 0
    
    for i, test in enumerate(edge_cases, 1):
        print(f"Edge Case {i}: {test['name']}")
        
        try:
            score = calculate_opportunity_score(test['signal'], business)
            impact = classify_impact(score)
            print(f"  Score: {score}/10, Impact: {impact}")
            
            if test['should_succeed']:
                print(f"  ✓ PASS - Handled correctly")
                passed += 1
            else:
                print(f"  ✗ FAIL - Should have raised error")
                failed += 1
        except Exception as e:
            if not test['should_succeed']:
                print(f"  ✓ PASS - Correctly raised error: {e}")
                passed += 1
            else:
                print(f"  ✗ FAIL - Unexpected error: {e}")
                failed += 1
        
        print()
    
    print("=" * 70)
    print(f"Edge Case Results: {passed} passed, {failed} failed")
    print("=" * 70)
    print()
    
    return failed == 0


def test_score_to_impact_mapping():
    """Test the score to impact level mapping"""
    
    print("=" * 70)
    print("Testing Score to Impact Mapping")
    print("=" * 70)
    print()
    
    test_cases = [
        (10.0, "high", "Maximum score"),
        (9.5, "high", "Very high score"),
        (8.0, "high", "High threshold"),
        (7.9, "medium", "Just below high"),
        (7.0, "medium", "Mid-range score"),
        (5.0, "medium", "Medium threshold"),
        (4.9, "low", "Just below medium"),
        (3.0, "low", "Low score"),
        (0.0, "low", "Minimum score")
    ]
    
    passed = 0
    failed = 0
    
    for score, expected_impact, description in test_cases:
        impact = classify_impact(score)
        
        if impact == expected_impact:
            print(f"  ✓ Score {score}/10 → {impact.upper()} ({description})")
            passed += 1
        else:
            print(f"  ✗ Score {score}/10 → Expected {expected_impact}, got {impact}")
            failed += 1
    
    print()
    print("=" * 70)
    print(f"Mapping Results: {passed} passed, {failed} failed")
    print("=" * 70)
    print()
    
    return failed == 0


def main():
    """Run all tests"""
    print("\n")
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 15 + "OPPORTUNITY SCORE TEST SUITE" + " " * 25 + "║")
    print("╚" + "═" * 68 + "╝")
    print()
    
    tests = [
        ("Opportunity Score Scenarios", test_opportunity_score_scenarios),
        ("Full Analysis Pipeline", test_full_analysis),
        ("Edge Cases", test_edge_cases),
        ("Score to Impact Mapping", test_score_to_impact_mapping)
    ]
    
    results = []
    
    for test_name, test_func in tests:
        try:
            result = test_func()
            results.append((test_name, result))
        except Exception as e:
            print(f"✗ Test suite '{test_name}' crashed: {e}")
            results.append((test_name, False))
    
    # Final summary
    print()
    print("╔" + "═" * 68 + "╗")
    print("║" + " " * 25 + "FINAL SUMMARY" + " " * 30 + "║")
    print("╚" + "═" * 68 + "╝")
    print()
    
    for test_name, result in results:
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{status:10} - {test_name}")
    
    all_passed = all(result for _, result in results)
    
    print()
    if all_passed:
        print("🎉 ALL TESTS PASSED! Opportunity Score feature working correctly.")
    else:
        print("❌ SOME TESTS FAILED. Please review the results above.")
    print()
    
    return 0 if all_passed else 1


if __name__ == "__main__":
    exit(main())
