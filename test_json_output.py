"""
Quick test to verify JSON output includes all new fields
"""

import json
from agent_b_analyst import AgentBAnalyst

# Initialize agent
agent = AgentBAnalyst()

# Load test data
with open('example_business_profile.json', 'r') as f:
    business = json.load(f)

with open('example_competitor_findings.json', 'r') as f:
    competitors = json.load(f)

# Run analysis
result_json = agent.analyze(business, competitors)
result = json.loads(result_json)

# Verify all fields present
print("=" * 70)
print(" JSON OUTPUT VALIDATION")
print("=" * 70)
print()

required_fields = [
    "impact_level",
    "summary",
    "pricing_gap",
    "market_risk",
    "recommended_urgency",
    "key_insights",
    "price_difference_percent",
    "threat_score",
    "threat_score_formula",
    "response_type",
    "competitor_breakdown"
]

print("✓ Checking required fields:")
all_present = True
for field in required_fields:
    present = field in result
    status = "✓" if present else "✗"
    print(f"  {status} {field}")
    if not present:
        all_present = False

print()
if all_present:
    print("✅ All required fields present!")
else:
    print("❌ Some fields missing!")

print()
print("=" * 70)
print(" SAMPLE JSON OUTPUT")
print("=" * 70)
print()
print(json.dumps(result, indent=2))
