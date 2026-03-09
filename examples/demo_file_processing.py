"""
Example usage of Scout Agent with sample data files
"""

from pathlib import Path
from agents.scout_agent import ScoutAgent
import json


def demo_file_processing():
    """Demonstrate processing files"""
    
    print("=" * 60)
    print("DEMO: File Processing with Scout Agent")
    print("=" * 60)
    print()
    
    agent = ScoutAgent()
    
    # Process JSON file
    print("1. Processing JSON file with structured data...")
    print("-" * 60)
    json_file = "data/inputs/sample_competitor_data.json"
    signals = agent.process_file(json_file)
    print(f"Extracted {len(signals)} signals from JSON file")
    print(json.dumps(signals[:2], indent=2))  # Show first 2
    print()
    
    # Process text file
    print("2. Processing text file...")
    print("-" * 60)
    txt_file = "data/inputs/dominos_promo.txt"
    signals = agent.process_file(txt_file)
    print(f"Extracted {len(signals)} signals from text file")
    print(json.dumps(signals, indent=2))
    print()
    
    # Show statistics
    print("3. Agent Statistics")
    print("-" * 60)
    stats = agent.get_stats()
    print(json.dumps(stats, indent=2))
    print()
    
    # Export all signals
    output_dir = Path("data/outputs")
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / "demo_signals.json"
    
    agent.export_signals(str(output_file))
    print(f"✓ All signals exported to: {output_file}")
    print()
    
    print("=" * 60)


if __name__ == "__main__":
    demo_file_processing()
