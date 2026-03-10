# Start everything
.\start.ps1

# Or manually:
# Terminal 1: python api_server.py
# Terminal 2: cd rivalsense-ui && npm run dev

# Open browser
start http://localhost:3000/war-room"""
Main entry point for Scout Agent
Demonstrates competitor signal extraction and monitoring
"""

import json
from pathlib import Path
from agents.scout_agent import ScoutAgent


def main():
    """Main execution function for Scout Agent"""
    
    print("=" * 80)
    print("SCOUT AGENT - COMPETITOR INTELLIGENCE MONITORING")
    print("=" * 80)
    print()
    
    # Initialize Scout Agent
    scout = ScoutAgent()
    
    # Process competitor data from various sources
    print("Extracting competitor signals from multiple sources...")
    print("-" * 80)
    
    # Competitor data batch
    competitor_batch = [
        {
            "type": "structured",
            "data": {
                "competitor": "Dominos",
                "product": "Farmhouse Pizza",
                "event_type": "promotion",
                "price": "299",
                "offer": "Buy 1 Get 1",
                "summary": "Dominos launched Buy 1 Get 1 offer on Farmhouse Pizza"
            },
            "source": "website"
        },
        {
            "type": "structured",
            "data": {
                "competitor": "Pizza Hut",
                "product": "Margherita Pizza",
                "event_type": "discount",
                "price": "199",
                "offer": "30% off",
                "summary": "Pizza Hut offering 30% discount on Margherita Pizza"
            },
            "source": "api"
        },
        {
            "type": "structured",
            "data": {
                "competitor": "Subway",
                "product": "Veggie Sub",
                "event_type": "bundle_offer",
                "price": "180",
                "offer": "Sub + Drink + Chips combo",
                "summary": "Subway introduces value combo with sub, drink and chips"
            },
            "source": "website"
        },
        {
            "type": "text",
            "data": "KFC announced new Zinger Burger meal at ₹250 with special promotional pricing for limited time.",
            "competitor": "KFC",
            "source": "social_media"
        }
    ]
    
    # Process all signals
    signals = scout.process_batch(competitor_batch)
    
    print(f"✓ Extracted {len(signals)} competitor signals")
    print()
    
    # Show all signals
    print("Competitor Signals:")
    print("-" * 80)
    for i, signal in enumerate(signals, 1):
        print(f"\n{i}. {signal['competitor']} - {signal['product']}")
        print(f"   Event Type: {signal['event_type'].upper()}")
        print(f"   Price: ₹{signal['price']}")
        print(f"   Offer: {signal['offer']}")
        print(f"   Source: {signal['source']}")
        print(f"   Summary: {signal['summary']}")
    
    print()
    print("-" * 80)
    
    # Export signals
    output_dir = Path("data/outputs")
    output_dir.mkdir(parents=True, exist_ok=True)
    signals_file = output_dir / "competitor_signals.json"
    
    scout.export_signals(str(signals_file))
    print(f"\n✓ Competitor signals saved to: {signals_file}")
    print()
    
    # Scout statistics
    scout_stats = scout.get_stats()
    print("Scout Agent Statistics:")
    print("-" * 80)
    print(f"  Total Signals Extracted: {scout_stats['total_signals']}")
    print(f"  Unique Competitors: {scout_stats['unique_competitors']}")
    print(f"  Signal Sources: {', '.join(scout_stats['sources'])}")
    print()
    
    # Show signals by event type
    print("Signals by Event Type:")
    for event_type, count in scout_stats['event_types'].items():
        print(f"  • {event_type.replace('_', ' ').title()}: {count}")
    print()
    
    # Show signals by competitor
    print("Signals by Competitor:")
    for competitor in scout_stats['competitors']:
        competitor_signals = scout.get_signals_by_competitor(competitor)
        print(f"  • {competitor}: {len(competitor_signals)} signal(s)")
    
    print()
    print("=" * 80)
    print("Scout Agent execution completed successfully!")
    print("=" * 80)


if __name__ == "__main__":
    main()
