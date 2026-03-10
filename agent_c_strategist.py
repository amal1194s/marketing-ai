"""
Agent C: The Strategist
Generates practical, actionable recommendations based on competitive analysis.

Takes business profile, scout findings, and analyst output to create
a clear response strategy with ready-to-use marketing content.
"""

import json
from typing import Dict, List, Any, Optional


class AgentCStrategist:
    """
    Agent C: The Strategist
    
    Converts competitive analysis into practical business actions:
    - Decides best response strategy
    - Provides pricing recommendations
    - Generates campaign ideas and marketing content
    - Outputs dashboard-ready recommendations
    """
    
    def __init__(self):
        self.agent_name = "Agent C: The Strategist"
        self.version = "2.0"
    
    def strategize(
        self,
        business_profile: Dict[str, Any],
        scout_findings: Dict[str, Any],
        analyst_output: Dict[str, Any]
    ) -> str:
        """
        Generate strategic recommendations based on all inputs.
        
        Args:
            business_profile: Business profile dictionary
            scout_findings: Scout agent's competitor findings
            analyst_output: Analyst agent's analysis results
            
        Returns:
            JSON string with strategic recommendations in the required format
        """
        try:
            # Parse inputs if they're JSON strings
            if isinstance(business_profile, str):
                business_profile = json.loads(business_profile)
            if isinstance(scout_findings, str):
                scout_findings = json.loads(scout_findings)
            if isinstance(analyst_output, str):
                analyst_output = json.loads(analyst_output)
            
            # Determine response type and strategy
            response_type = self._determine_response_type(analyst_output, business_profile)
            
            # Generate all components
            strategy = {
                "recommended_action": self._generate_recommended_action(
                    response_type, analyst_output, business_profile
                ),
                "response_type": response_type,
                "price_action": self._generate_price_action(
                    response_type, analyst_output, business_profile
                ),
                "campaign_idea": self._generate_campaign_idea(
                    response_type, analyst_output, business_profile
                ),
                "marketing_post": self._generate_marketing_post(
                    response_type, business_profile, analyst_output
                ),
                "cta": self._generate_cta(response_type, business_profile),
                "execution_steps": self._generate_execution_steps(
                    response_type, analyst_output, business_profile
                ),
                "why_this_strategy": self._generate_strategy_rationale(
                    response_type, analyst_output, business_profile
                )
            }
            
            return json.dumps(strategy, indent=2, ensure_ascii=False)
            
        except Exception as e:
            return self._create_error_response(str(e))
    
    def _determine_response_type(
        self,
        analyst_output: Dict[str, Any],
        business_profile: Dict[str, Any]
    ) -> str:
        """
        Determine the best response strategy type.
        
        Decision logic:
        - hold_position: Pricing competitive, no major threats
        - promotion_response: Competitor promotions are main threat
        - price_adjustment: Significantly more expensive than competitors
        - product_differentiation: Unique strengths, avoid price wars
        """
        # Extract analysis data
        price_diff = analyst_output.get("price_difference_percent", 0)
        threat_score = analyst_output.get("threat_score", 5.0)
        impact_level = analyst_output.get("impact_level", "medium").lower()
        insights = analyst_output.get("key_insights", [])
        response_suggestion = analyst_output.get("response_type")
        
        # Use analyst's suggestion if available
        if response_suggestion:
            return response_suggestion
        
        # Check for promotion threats
        has_promo_threat = any(
            "promotion" in str(insight).lower() or "discount" in str(insight).lower()
            for insight in insights
        )
        
        # Check for differentiation opportunities
        business_strengths = business_profile.get("unique_selling_points", [])
        has_unique_strengths = len(business_strengths) > 0
        
        # Decision tree
        if price_diff > 20 and threat_score >= 7:
            # Much more expensive and high threat
            return "price_adjustment"
        
        elif has_promo_threat and price_diff <= 15:
            # Promotions are the issue, not base pricing
            return "promotion_response"
        
        elif price_diff > 15 and impact_level == "high":
            # Moderately expensive with high impact
            if has_unique_strengths:
                return "product_differentiation"
            else:
                return "price_adjustment"
        
        elif has_unique_strengths and price_diff <= 10:
            # Competitive pricing with unique strengths
            return "product_differentiation"
        
        elif threat_score < 5 and price_diff <= 10:
            # Low threat, competitive pricing
            return "hold_position"
        
        else:
            # Default: moderate threat, respond with promotion
            return "promotion_response"
    
    def _generate_recommended_action(
        self,
        response_type: str,
        analyst_output: Dict[str, Any],
        business_profile: Dict[str, Any]
    ) -> str:
        """Generate one clear summary of recommended action."""
        business_name = business_profile.get("name", "your business")
        
        actions = {
            "hold_position": f"Maintain current strategy for {business_name}. Your pricing is competitive and no immediate action needed. Stay alert and monitor competitors.",
            
            "promotion_response": f"Launch a limited-time promotion for {business_name} to compete with current competitor offers. Keep base prices unchanged.",
            
            "price_adjustment": f"Consider a tactical price adjustment for {business_name}. Competitors are significantly cheaper, and you risk losing price-sensitive customers.",
            
            "product_differentiation": f"Double down on what makes {business_name} unique. Avoid price wars by emphasizing quality, service, or unique features."
        }
        
        return actions.get(response_type, actions["hold_position"])
    
    def _generate_price_action(
        self,
        response_type: str,
        analyst_output: Dict[str, Any],
        business_profile: Dict[str, Any]
    ) -> str:
        """Generate specific pricing recommendation."""
        price_diff = analyst_output.get("price_difference_percent", 0)
        
        if response_type == "hold_position":
            return "Keep current pricing. You're competitive in the market."
        
        elif response_type == "promotion_response":
            return "Keep base prices. Launch a 15-20% limited-time promotion (2-4 weeks) to match competitor offers."
        
        elif response_type == "price_adjustment":
            if price_diff > 25:
                return f"Consider reducing prices by 10-15%. You're currently {abs(price_diff):.0f}% above market average."
            else:
                return f"Consider a 5-10% price reduction or add value bundles. You're {abs(price_diff):.0f}% above competitors."
        
        elif response_type == "product_differentiation":
            return "Maintain premium pricing. Justify it by emphasizing quality, service, and unique benefits."
        
        return "Monitor pricing weekly and adjust if needed."
    
    def _generate_campaign_idea(
        self,
        response_type: str,
        analyst_output: Dict[str, Any],
        business_profile: Dict[str, Any]
    ) -> str:
        """Generate a short campaign name or idea."""
        business_type = business_profile.get("business_type", "business")
        
        campaigns = {
            "hold_position": "Customer Appreciation Week",
            "promotion_response": "Flash Sale Alert",
            "price_adjustment": "New Value Pricing",
            "product_differentiation": "Why Choose Quality"
        }
        
        # Customize for food businesses
        if "pizza" in business_type.lower() or "food" in business_type.lower():
            campaigns["promotion_response"] = "Feast Mode: Limited Time Offer"
            campaigns["product_differentiation"] = "Taste the Difference"
        
        return campaigns.get(response_type, "Limited Time Offer")
    
    def _generate_marketing_post(
        self,
        response_type: str,
        business_profile: Dict[str, Any],
        analyst_output: Dict[str, Any]
    ) -> str:
        """Generate a ready-to-use social media post."""
        business_name = business_profile.get("name", "our business")
        business_type = business_profile.get("business_type", "service")
        
        if response_type == "hold_position":
            return (
                f"🌟 Thank you for choosing {business_name}! "
                f"This week, enjoy our quality {business_type} "
                f"with the same great value you trust. "
                f"Your loyalty means everything to us!"
            )
        
        elif response_type == "promotion_response":
            return (
                f"🔥 FLASH SALE AT {business_name.upper()}! 🔥\n\n"
                f"Get 20% OFF your order this week only! "
                f"Don't miss out on your favorite {business_type}. "
                f"Limited time. Order now!"
            )
        
        elif response_type == "price_adjustment":
            return (
                f"📢 BIG NEWS from {business_name}!\n\n"
                f"We've heard you—we're rolling out NEW VALUE PRICING "
                f"to give you even better deals on {business_type}. "
                f"Same quality, better price. Check it out today!"
            )
        
        elif response_type == "product_differentiation":
            usps = business_profile.get("unique_selling_points", [])
            usp_text = usps[0] if usps else "premium quality"
            return (
                f"✨ Why {business_name}? Because you deserve the best!\n\n"
                f"We don't cut corners. {usp_text.capitalize()}. "
                f"When quality matters, choose {business_name}. "
                f"Experience the difference today!"
            )
        
        return f"Visit {business_name} today for great {business_type}!"
    
    def _generate_cta(
        self,
        response_type: str,
        business_profile: Dict[str, Any]
    ) -> str:
        """Generate a clear call to action."""
        ctas = {
            "hold_position": "Order now and taste the quality!",
            "promotion_response": "Claim your discount before it's gone!",
            "price_adjustment": "Check out our new prices today!",
            "product_differentiation": "Experience premium quality—order now!"
        }
        
        return ctas.get(response_type, "Order now!")
    
    def _generate_execution_steps(
        self,
        response_type: str,
        analyst_output: Dict[str, Any],
        business_profile: Dict[str, Any]
    ) -> List[str]:
        """Generate 3-5 practical execution steps."""
        urgency = analyst_output.get("recommended_urgency", "medium").lower()
        
        steps = {
            "hold_position": [
                "Continue monitoring competitor activity weekly",
                "Focus on customer retention and satisfaction",
                "Collect customer feedback to identify improvement areas"
            ],
            
            "promotion_response": [
                "Design a 15-20% discount offer for your best-selling items",
                "Create social media posts and email campaign announcing the promotion",
                "Set a clear deadline (2-4 weeks) and promote urgency",
                "Track response rate and sales during promotion period"
            ],
            
            "price_adjustment": [
                "Analyze which products/services are most price-sensitive",
                "Test new pricing with a small customer segment first",
                "Update all pricing materials (website, menu, signage)",
                "Communicate the change as 'better value' not 'price cut'",
                "Monitor sales volume and profit margins weekly"
            ],
            
            "product_differentiation": [
                "List all unique strengths and features of your business",
                "Create marketing materials highlighting these differentiators",
                "Train staff to communicate unique value to customers",
                "Share customer testimonials and success stories",
                "Focus ad spend on quality-focused audience segments"
            ]
        }
        
        base_steps = steps.get(response_type, steps["hold_position"])
        
        # Add urgency-based step if needed
        if urgency == "high" and response_type != "hold_position":
            base_steps.insert(0, "Take action within 48 hours—competitors are moving fast")
        
        return base_steps[:5]
    
    def _generate_strategy_rationale(
        self,
        response_type: str,
        analyst_output: Dict[str, Any],
        business_profile: Dict[str, Any]
    ) -> List[str]:
        """Generate 3-4 reasons explaining why this strategy was chosen."""
        price_diff = analyst_output.get("price_difference_percent", 0)
        threat_score = analyst_output.get("threat_score", 5.0)
        impact_level = analyst_output.get("impact_level", "medium")
        insights = analyst_output.get("key_insights", [])
        
        reasons = []
        
        if response_type == "hold_position":
            reasons.append(f"Your pricing is competitive (within {abs(price_diff):.0f}% of market average)")
            reasons.append(f"Threat level is {impact_level} with score of {threat_score:.1f}/10")
            reasons.append("No immediate action needed; maintain monitoring")
        
        elif response_type == "promotion_response":
            reasons.append("Competitors are using promotions as their main tactic")
            if price_diff <= 10:
                reasons.append("Your base pricing is competitive; temporary promotion is lower risk")
            reasons.append("Promotions are quick to implement and test")
            reasons.append("Keeps base prices stable for long-term positioning")
        
        elif response_type == "price_adjustment":
            if price_diff > 20:
                reasons.append(f"You're {abs(price_diff):.0f}% more expensive than competitors")
            reasons.append(f"Threat score is {threat_score:.1f}/10, indicating significant risk")
            reasons.append("Price-sensitive customers may switch to cheaper alternatives")
            if impact_level == "high":
                reasons.append("High impact level requires decisive action")
        
        elif response_type == "product_differentiation":
            usps = business_profile.get("unique_selling_points", [])
            if usps:
                reasons.append(f"You have unique strengths: {', '.join(usps[:2])}")
            reasons.append("Competing on price alone leads to margin erosion")
            reasons.append("Premium positioning protects long-term profitability")
            if price_diff <= 15:
                reasons.append("Price gap is manageable if value is communicated well")
        
        # Add insight-based reasons
        for insight in insights[:2]:
            if insight not in str(reasons):
                reasons.append(insight[:100])  # Truncate if too long
        
        return reasons[:4]
    
    def _create_error_response(self, error: str) -> str:
        """Create error response in the required format."""
        return json.dumps({
            "error": True,
            "message": f"Strategy generation failed: {error}",
            "recommended_action": "Unable to generate strategy due to error",
            "response_type": "hold_position",
            "price_action": "Review input data",
            "campaign_idea": "N/A",
            "marketing_post": "N/A",
            "cta": "N/A",
            "execution_steps": ["Fix data errors", "Retry strategy generation"],
            "why_this_strategy": [f"Error occurred: {error}"]
        }, indent=2)


if __name__ == "__main__":
    # Test example
    print("=" * 70)
    print("Agent C: The Strategist - Test Example")
    print("=" * 70)
    
    # Sample inputs
    business_profile = {
        "name": "Mike's Pizza Palace",
        "business_type": "pizza restaurant",
        "unique_selling_points": ["Fresh ingredients", "Family recipes"],
        "pricing": {"large_pizza": 16.99}
    }
    
    scout_findings = {
        "competitors": [
            {"name": "Domino's", "price": 15.99, "promotion": "50% off"}
        ]
    }
    
    analyst_output = {
        "impact_level": "medium",
        "price_difference_percent": 8.0,
        "threat_score": 6.5,
        "recommended_urgency": "medium",
        "key_insights": ["Competitors running aggressive promotions"]
    }
    
    # Generate strategy
    strategist = AgentCStrategist()
    result = strategist.strategize(business_profile, scout_findings, analyst_output)
    
    # Display result
    strategy = json.loads(result)
    print("\n✅ STRATEGY GENERATED:\n")
    print(f"Action: {strategy['recommended_action']}\n")
    print(f"Type: {strategy['response_type']}\n")
    print(f"Marketing Post:\n{strategy['marketing_post']}\n")
    print(f"CTA: {strategy['cta']}\n")
    print("\nFull JSON output:")
    print(result)
    print("\n" + "=" * 70)
    print("✓ Agent C ready for use!")
    print("=" * 70)
