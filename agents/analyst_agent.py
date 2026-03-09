"""
ScoutIQ Analyst Agent
Analyzes competitor signals and generates market insights
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Union
from datetime import datetime


# File paths
COMPETITOR_SIGNALS_PATH = Path("data/outputs/competitor_signals.json")
BUSINESS_PROFILE_PATH = Path("data/inputs/business_profile.json")
MARKET_ANALYSIS_PATH = Path("data/outputs/market_analysis.json")


def load_json(path: Union[str, Path]) -> Any:
    """
    Load JSON data from file with error handling.
    
    Args:
        path: Path to JSON file
        
    Returns:
        Parsed JSON data
        
    Raises:
        FileNotFoundError: If file doesn't exist
        json.JSONDecodeError: If file contains invalid JSON
    """
    path = Path(path)
    
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(
            f"Invalid JSON in {path}: {e.msg}",
            e.doc,
            e.pos
        )


def save_json(data: Any, path: Union[str, Path]) -> None:
    """
    Save data as JSON to file.
    
    Args:
        data: Data to save
        path: Path to output file
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def calculate_opportunity_score(
    signal: Dict[str, Any],
    business_profile: Dict[str, Any]
) -> float:
    """
    Calculate Market Opportunity Score (0-10) representing competitive threat level.
    
    Scoring Logic:
    - Base score: 5
    - Price advantage: up to +3 based on percentage cheaper
    - Event type bonus: promotion/discount = +2, launch = +1
    - Extreme discount: if >30% cheaper, add +3
    - Cap at 10
    
    Args:
        signal: Competitor signal data
        business_profile: User's business profile
        
    Returns:
        Opportunity score (0-10)
    """
    competitor_price = signal.get("price", 0)
    user_price = business_profile.get("price", 0)
    event_type = signal.get("event_type", "").lower()
    
    # Start with base score
    score = 5.0
    
    # Handle missing or invalid prices
    if user_price <= 0 or competitor_price <= 0:
        # No valid price comparison possible
        # Score based only on event type
        if event_type in ["promotion", "discount"]:
            return min(7.0, score + 2)
        elif event_type == "launch":
            return min(6.0, score + 1)
        return score
    
    # Calculate price difference and percentage
    price_difference = competitor_price - user_price
    percent_difference = (price_difference / user_price) * 100
    
    # Add points if competitor is cheaper
    if price_difference < 0:  # Competitor cheaper
        # Add up to +3 points based on how much cheaper
        # Scale: 0-10% = +0.5, 10-20% = +1.5, 20-30% = +2.5, >30% = +3
        abs_percent = abs(percent_difference)
        
        if abs_percent <= 10:
            score += 0.5
        elif abs_percent <= 20:
            score += 1.5
        elif abs_percent <= 30:
            score += 2.5
        else:
            score += 3.0
            
        # Extreme discount bonus: if >30% cheaper, add another +3
        if abs_percent > 30:
            score += 3.0
    
    # Event type bonuses
    if event_type in ["promotion", "discount"]:
        score += 2.0
    elif event_type == "launch":
        score += 1.0
    
    # Cap score at 10
    score = min(10.0, score)
    
    # Floor score at 0
    score = max(0.0, score)
    
    return round(score, 1)


def classify_impact(opportunity_score: float) -> str:
    """
    Map opportunity score to impact level.
    
    Mapping:
    - score >= 8: HIGH
    - score 5-7: MEDIUM
    - score < 5: LOW
    
    Args:
        opportunity_score: Market opportunity score (0-10)
        
    Returns:
        Impact level: "high", "medium", or "low"
    """
    if opportunity_score >= 8:
        return "high"
    elif opportunity_score >= 5:
        return "medium"
    else:
        return "low"


def generate_insight(
    signal: Dict[str, Any],
    business_profile: Dict[str, Any],
    price_difference: float,
    opportunity_score: float
) -> str:
    """
    Generate natural language business insight for the signal.
    
    Args:
        signal: Competitor signal data
        business_profile: User's business profile
        price_difference: Price difference (competitor - user)
        opportunity_score: Market opportunity score (0-10)
        
    Returns:
        Business-focused insight string
    """
    competitor = signal.get("competitor", "Competitor")
    event_type = signal.get("event_type", "activity")
    product = signal.get("product", "product")
    competitor_price = signal.get("price", 0)
    user_price = business_profile.get("price", 0)
    offer = signal.get("offer", "")
    
    # Determine impact level from score
    impact_level = classify_impact(opportunity_score)
    
    # Build insight based on impact level and situation
    if impact_level == "high":
        if price_difference < 0:
            # Competitor cheaper - high threat
            abs_diff = abs(price_difference)
            if event_type in ["promotion", "discount"]:
                return (
                    f"{competitor} {event_type} offers a significantly lower price "
                    f"(₹{competitor_price} vs your ₹{user_price}) and may attract "
                    f"price-sensitive customers. Immediate response recommended."
                )
            else:
                return (
                    f"{competitor} is priced ₹{abs_diff} lower than your {product}, "
                    f"creating strong competitive pressure. Consider value differentiation "
                    f"or price adjustment."
                )
        else:
            # Aggressive promotion even if not cheaper
            return (
                f"{competitor} launched aggressive {event_type} ({offer}) which could "
                f"draw market attention. Monitor customer response and prepare counter-strategy."
            )
    
    elif impact_level == "medium":
        if price_difference < 0:
            abs_diff = abs(price_difference)
            return (
                f"{competitor} is moderately cheaper (₹{abs_diff} difference) with {event_type}. "
                f"Notable competitive activity that warrants monitoring and potential response."
            )
        elif event_type in ["launch", "new_product"]:
            return (
                f"{competitor} {event_type} creates market movement. "
                f"Evaluate if product refresh or promotional response is needed."
            )
        else:
            return (
                f"{competitor} {event_type} activity at similar price point. "
                f"Moderate competitive presence requires awareness and tracking."
            )
    
    else:  # low impact
        if price_difference > 0:
            return (
                f"{competitor} is more expensive (₹{competitor_price} vs your ₹{user_price}). "
                f"Your price advantage is maintained. Focus on quality and retention."
            )
        else:
            return (
                f"{competitor} {event_type} presents minimal immediate threat. "
                f"Standard competitive activity that should be monitored but does not require urgent action."
            )


def analyze_signal(
    signal: Dict[str, Any],
    business_profile: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Analyze a single competitor signal against business profile.
    
    Args:
        signal: Competitor signal data
        business_profile: User's business profile
        
    Returns:
        Analysis result dictionary with opportunity_score
    """
    # Extract prices
    competitor_price = signal.get("price", 0)
    user_price = business_profile.get("price", 0)
    
    # Validate prices
    if user_price <= 0:
        raise ValueError("Business profile must have a valid price > 0")
    
    if competitor_price < 0:
        competitor_price = 0
    
    # Calculate difference
    price_difference = competitor_price - user_price
    
    # Calculate opportunity score
    opportunity_score = calculate_opportunity_score(signal, business_profile)
    
    # Classify impact based on score
    impact_level = classify_impact(opportunity_score)
    
    # Generate insight
    insight = generate_insight(signal, business_profile, price_difference, opportunity_score)
    
    # Build analysis result
    return {
        "competitor": signal.get("competitor", "Unknown"),
        "event_type": signal.get("event_type", "unknown"),
        "competitor_price": competitor_price,
        "user_price": user_price,
        "price_difference": price_difference,
        "opportunity_score": opportunity_score,
        "impact_level": impact_level,
        "insight": insight,
        "timestamp": signal.get("timestamp", datetime.now().isoformat()),
        "offer": signal.get("offer", ""),
        "product": signal.get("product", "")
    }


def run_analyst_agent() -> List[Dict[str, Any]]:
    """
    Main analyst agent execution.
    
    Reads competitor signals and business profile,
    analyzes each signal, and generates market insights.
    
    Returns:
        List of analysis results
        
    Raises:
        FileNotFoundError: If input files are missing
        ValueError: If data is invalid
    """
    print("=" * 70)
    print("ScoutIQ Analyst Agent - Market Analysis")
    print("=" * 70)
    print()
    
    # Load input data
    print("📁 Loading input files...")
    try:
        competitor_signals = load_json(COMPETITOR_SIGNALS_PATH)
        business_profile = load_json(BUSINESS_PROFILE_PATH)
    except FileNotFoundError as e:
        print(f"❌ Error: {e}")
        print("\nMake sure the following files exist:")
        print(f"  - {COMPETITOR_SIGNALS_PATH}")
        print(f"  - {BUSINESS_PROFILE_PATH}")
        raise
    except json.JSONDecodeError as e:
        print(f"❌ Error: {e}")
        raise
    
    # Validate inputs
    if not isinstance(competitor_signals, list):
        raise ValueError("competitor_signals.json must contain a list of signals")
    
    if not isinstance(business_profile, dict):
        raise ValueError("business_profile.json must contain an object")
    
    print(f"✓ Loaded {len(competitor_signals)} competitor signal(s)")
    print(f"✓ Business: {business_profile.get('business_name', 'Unknown')}")
    print()
    
    # Handle empty signals
    if not competitor_signals:
        print("⚠️  No competitor signals to analyze")
        analysis_results = []
    else:
        # Analyze each signal
        print("🔬 Analyzing competitor signals...")
        analysis_results = []
        
        for i, signal in enumerate(competitor_signals, 1):
            try:
                result = analyze_signal(signal, business_profile)
                analysis_results.append(result)
                
                # Print summary
                competitor = result['competitor']
                score = result['opportunity_score']
                impact = result['impact_level'].upper()
                impact_emoji = {"HIGH": "🔴", "MEDIUM": "🟡", "LOW": "🟢"}.get(impact, "⚪")
                
                print(f"  {i}. {impact_emoji} {competitor} - Score: {score}/10 ({impact} Impact)")
                
            except Exception as e:
                print(f"  ⚠️  Skipping signal {i}: {e}")
                continue
        
        print()
        print(f"✓ Analyzed {len(analysis_results)} signal(s)")
    
    # Save results
    print(f"💾 Saving analysis to {MARKET_ANALYSIS_PATH}...")
    save_json(analysis_results, MARKET_ANALYSIS_PATH)
    
    print()
    print("=" * 70)
    print("✅ Market analysis generated successfully")
    print("=" * 70)
    print(f"\nOutput saved to: {MARKET_ANALYSIS_PATH}")
    print(f"Total insights: {len(analysis_results)}")
    
    if analysis_results:
        high_impact = sum(1 for r in analysis_results if r['impact_level'] == 'high')
        medium_impact = sum(1 for r in analysis_results if r['impact_level'] == 'medium')
        low_impact = sum(1 for r in analysis_results if r['impact_level'] == 'low')
        
        print(f"\nImpact Summary:")
        print(f"  🔴 High: {high_impact}")
        print(f"  🟡 Medium: {medium_impact}")
        print(f"  🟢 Low: {low_impact}")
    
    print()
    
    return analysis_results


def main():
    """Entry point for the analyst agent."""
    try:
        run_analyst_agent()
    except Exception as e:
        print(f"\n❌ Error: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    exit(main())
