"""
Test Script for ScoutIQ Analyst Agent
Tests various scenarios and edge cases
"""

import json
import sys
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from agents.analyst_agent import (
    classify_impact,
    generate_insight,
    analyze_signal,
    load_json,
    save_json
)


def test_classify_impact():
    """Test impact classification logic"""
    print("=" * 70)
    print("Test 1: Impact Classification")
    print("=" * 70)
    
    test_cases = [
        # (signal, price_diff, user_price, expected)
        (
            {"event_type": "discount", "price": 100, "offer": "50% off"},
            -100,  # much cheaper
            200,
            "high"
        ),
        (
            {"event_type": "promotion", "price": 280, "offer": "Buy 1 Get 1"},
            -70,  # moderately cheaper with BOGO
            350,
            "high"
        ),
        (
            {"event_type": "price_update", "price": 320},
            -30,  # slightly cheaper
            350,
            "medium"
        ),
        (
            {"event_type": "launch", "price": 400},
            50,  # more expensive
            350,
            "medium"
        ),
        (
            {"event_type": "price_update", "price": 500},
            150,  # much more expensive
            350,
            "low"
        ),
    ]
    
    passed = 0
    for signal, price_diff, user_price, expected in test_cases:
        result = classify_impact(signal, price_diff, user_price)
        status = "✓" if result == expected else "✗"
        print(f"{status} Price diff: {price_diff}, Event: {signal['event_type']}, "
              f"Expected: {expected}, Got: {result}")
        if result == expected:
            passed += 1
    
    print(f"\nPassed: {passed}/{len(test_cases)}")
    print()


def test_analyze_signal():
    """Test signal analysis"""
    print("=" * 70)
    print("Test 2: Signal Analysis")
    print("=" * 70)
    
    business = {
        "business_name": "Test Business",
        "price": 350
    }
    
    signal = {
        "competitor": "Test Competitor",
        "event_type": "discount",
        "price": 250,
        "offer": "30% off",
        "product": "Test Product",
        "timestamp": "2026-03-09T10:00:00"
    }
    
    result = analyze_signal(signal, business)
    
    print("Input Signal:")
    print(f"  Competitor: {signal['competitor']}")
    print(f"  Price: ₹{signal['price']}")
    print(f"  Event: {signal['event_type']}")
    print()
    
    print("Analysis Result:")
    print(f"  Price Difference: ₹{result['price_difference']}")
    print(f"  Impact Level: {result['impact_level'].upper()}")
    print(f"  Insight: {result['insight'][:80]}...")
    print()
    
    assert result['price_difference'] == -100
    assert result['impact_level'] in ['high', 'medium', 'low']
    assert result['insight']
    print("✓ Signal analysis working correctly")
    print()


def test_edge_cases():
    """Test edge cases and error handling"""
    print("=" * 70)
    print("Test 3: Edge Cases")
    print("=" * 70)
    
    business = {"business_name": "Test", "price": 350}
    
    # Test 1: Missing price in signal
    signal_no_price = {
        "competitor": "Test",
        "event_type": "promotion",
        # price missing - should default to 0
    }
    result = analyze_signal(signal_no_price, business)
    print(f"✓ Handles missing competitor price: {result['competitor_price']}")
    
    # Test 2: Zero price
    signal_zero = {
        "competitor": "Test",
        "event_type": "free",
        "price": 0
    }
    result = analyze_signal(signal_zero, business)
    print(f"✓ Handles zero price: {result['price_difference']}")
    
    # Test 3: Very high price
    signal_high = {
        "competitor": "Premium",
        "event_type": "launch",
        "price": 10000
    }
    result = analyze_signal(signal_high, business)
    print(f"✓ Handles extreme high price: {result['price_difference']}")
    
    # Test 4: Invalid business price should raise error
    try:
        invalid_business = {"price": 0}
        analyze_signal(signal_no_price, invalid_business)
        print("✗ Should have raised error for invalid business price")
    except ValueError as e:
        print(f"✓ Correctly raises error for invalid business price")
    
    print()


def test_full_pipeline():
    """Test the complete pipeline with sample data"""
    print("=" * 70)
    print("Test 4: Full Pipeline Test")
    print("=" * 70)
    
    # Create test data
    test_signals = [
        {
            "competitor": "Competitor A",
            "product": "Product A",
            "event_type": "discount",
            "price": 250,
            "offer": "20% off",
            "timestamp": "2026-03-09T10:00:00"
        },
        {
            "competitor": "Competitor B",
            "product": "Product B",
            "event_type": "promotion",
            "price": 180,
            "offer": "Buy 1 Get 1",
            "timestamp": "2026-03-09T11:00:00"
        }
    ]
    
    test_business = {
        "business_name": "Test Pizza",
        "product": "Pizza",
        "price": 300
    }
    
    # Analyze all signals
    results = []
    for signal in test_signals:
        result = analyze_signal(signal, test_business)
        results.append(result)
    
    print(f"✓ Analyzed {len(results)} signals")
    print(f"  High impact: {sum(1 for r in results if r['impact_level'] == 'high')}")
    print(f"  Medium impact: {sum(1 for r in results if r['impact_level'] == 'medium')}")
    print(f"  Low impact: {sum(1 for r in results if r['impact_level'] == 'low')}")
    
    # Check output structure
    for result in results:
        assert 'competitor' in result
        assert 'impact_level' in result
        assert 'insight' in result
        assert 'price_difference' in result
    
    print("✓ All results have required fields")
    print()


def main():
    """Run all tests"""
    print()
    print("█" * 70)
    print(" ScoutIQ Analyst Agent - Test Suite")
    print("█" * 70)
    print()
    
    try:
        test_classify_impact()
        test_analyze_signal()
        test_edge_cases()
        test_full_pipeline()
        
        print("=" * 70)
        print("✅ All tests passed successfully!")
        print("=" * 70)
        print()
        
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
