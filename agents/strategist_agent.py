"""
ScoutIQ Strategist Agent
Generates marketing strategies based on market analysis insights.
"""

import json
from pathlib import Path
from typing import Any, Dict, List, Union


# File paths
MARKET_ANALYSIS_PATH = Path("data/outputs/market_analysis.json")
MARKETING_STRATEGY_PATH = Path("data/outputs/marketing_strategy.json")


def load_json(path: Union[str, Path]) -> Any:
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(f"File not found: {path}")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data: Any, path: Union[str, Path]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def map_threat_level(impact: str) -> str:
    impact = (impact or "").lower()
    if impact in ("high", "medium", "low"):
        return impact
    return "medium"


def generate_strategy(insights: List[Dict]) -> List[Dict]:
    """Convert analyst insights into actionable marketing strategies."""
    strategies = []
    for item in insights:
        competitor = item.get("competitor", "")
        impact = item.get("impact_level", "")
        event = item.get("event_type", "")
        price_diff = item.get("price_difference")

        threat = map_threat_level(impact)

        # default messages
        strategy_type = "marketing_strategy"
        recommended_action = (
            f"Monitor {competitor}'s activity and adjust plans as needed."
        )
        marketing_message = (
            f"Stay tuned for updates and enjoy our unique offerings!"
        )
        expected_benefit = (
            "Maintains visibility and allows flexible response."
        )

        if event.lower() in ["promotion", "discount"]:
            if price_diff is not None and price_diff < 0:
                strategy_type = "pricing_strategy"
                recommended_action = (
                    f"Adjust pricing or launch a special offer to match or beat {competitor}'s {event}."
                )
                marketing_message = (
                    f"Special deal! Compete with {competitor} and enjoy great value today."
                )
                expected_benefit = (
                    "Improves competitiveness on price-sensitive customers and reduces loss of market share."
                )
            else:
                strategy_type = "promotion_strategy"
                recommended_action = (
                    f"Launch a targeted promotion to counter {competitor}'s {event}."
                )
                marketing_message = (
                    f"Don't miss our exclusive promotion—better than {competitor}'s offer!"
                )
                expected_benefit = (
                    "Draws attention away from competitor promotions and retains customer interest."
                )

        strategies.append(
            {
                "competitor": competitor,
                "threat_level": threat,
                "recommended_action": recommended_action,
                "strategy_type": strategy_type,
                "marketing_message": marketing_message,
                "expected_benefit": expected_benefit,
            }
        )
    return strategies


def main():
    try:
        insights = load_json(MARKET_ANALYSIS_PATH)
    except FileNotFoundError:
        print(f"Input file not found: {MARKET_ANALYSIS_PATH}")
        return
    strategies = generate_strategy(insights)
    save_json(strategies, MARKETING_STRATEGY_PATH)
    print(f"Generated {len(strategies)} strategies and saved to {MARKETING_STRATEGY_PATH}")


if __name__ == "__main__":
    main()
