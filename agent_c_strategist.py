"""
Agent C: The Strategist
Generates actionable recommendations based on competitive analysis
"""

import json
from typing import Dict, List
from datetime import datetime


class AgentCStrategist:
    """
    Agent C: The Strategist
    Takes competitive analysis and generates specific action recommendations
    """
    
    def __init__(self):
        self.agent_name = "Agent C: The Strategist"
        self.version = "1.0"
    
    def strategize(self, analysis_json: str, business_profile: Dict) -> str:
        """
        Generate strategic recommendations based on analysis
        
        Args:
            analysis_json: JSON string from Agent B analysis
            business_profile: Business profile dictionary
            
        Returns:
            JSON string with strategic recommendations
        """
        try:
            analysis = json.loads(analysis_json)
            
            # Generate recommendations
            recommendations = self._generate_recommendations(analysis, business_profile)
            
            # Create response
            strategy = {
                "timestamp": datetime.now().isoformat(),
                "business_name": business_profile.get("name", "Unknown"),
                "priority_actions": recommendations["priority"],
                "pricing_strategy": recommendations["pricing"],
                "marketing_tactics": recommendations["marketing"],
                "risk_mitigation": recommendations["risk"],
                "timeline": self._determine_timeline(analysis),
                "success_metrics": self._define_metrics(analysis, business_profile)
            }
            
            return json.dumps(strategy, indent=2)
            
        except Exception as e:
            return self._create_error_response(str(e))
    
    def _generate_recommendations(self, analysis: Dict, business: Dict) -> Dict:
        """Generate specific action recommendations"""
        impact = analysis.get("impact_level", "medium").lower()
        urgency = analysis.get("recommended_urgency", "medium").lower()
        insights = analysis.get("key_insights", [])
        price_diff = analysis.get("price_difference_percent", 0)
        
        recommendations = {
            "priority": [],
            "pricing": [],
            "marketing": [],
            "risk": []
        }
        
        # PRIORITY ACTIONS based on urgency and insights
        if urgency == "high":
            recommendations["priority"].append("Emergency strategy meeting within 24-48 hours")
            recommendations["priority"].append("Activate rapid response plan")
        
        for insight in insights:
            if "price" in insight.lower() or "pricing" in insight.lower():
                if "undercutting" in insight.lower() or price_diff > 15:
                    recommendations["priority"].append("Review pricing strategy immediately")
                    recommendations["priority"].append("Analyze customer price sensitivity")
            
            if "promotion" in insight.lower() or "aggressive" in insight.lower():
                recommendations["priority"].append("Launch counter-promotion campaign")
                recommendations["priority"].append("Strengthen loyalty program incentives")
            
            if "innovation" in insight.lower() or "product" in insight.lower():
                recommendations["priority"].append("Accelerate product development roadmap")
                recommendations["priority"].append("Highlight unique product features")
        
        # PRICING STRATEGY
        if price_diff > 20:
            recommendations["pricing"].append("Consider 10-15% price adjustment")
            recommendations["pricing"].append("Introduce budget-friendly options")
            recommendations["pricing"].append("Emphasize quality-to-price value")
        elif price_diff > 10:
            recommendations["pricing"].append("Maintain pricing but add value bundles")
            recommendations["pricing"].append("Implement tiered pricing structure")
        elif price_diff < -10:
            recommendations["pricing"].append("Leverage price advantage in marketing")
            recommendations["pricing"].append("Focus on volume and market share growth")
        else:
            recommendations["pricing"].append("Maintain current competitive pricing")
            recommendations["pricing"].append("Monitor market changes weekly")
        
        # MARKETING TACTICS
        has_promo_threat = any("promotion" in i.lower() for i in insights)
        has_audience_overlap = any("audience" in i.lower() for i in insights)
        
        if has_promo_threat:
            recommendations["marketing"].append("Launch limited-time promotional campaign")
            recommendations["marketing"].append("Increase social media engagement 2x")
            recommendations["marketing"].append("Target competitor customers with offers")
        
        if has_audience_overlap:
            recommendations["marketing"].append("Strengthen unique value proposition messaging")
            recommendations["marketing"].append("Emphasize brand differentiators")
        
        recommendations["marketing"].append("Boost customer retention programs")
        recommendations["marketing"].append("Collect customer feedback on competitors")
        
        # RISK MITIGATION
        if impact in ["high", "medium"]:
            recommendations["risk"].append("Daily competitor activity monitoring")
            recommendations["risk"].append("Weekly sales trend analysis")
            recommendations["risk"].append("Customer churn tracking and prevention")
        
        if urgency == "high":
            recommendations["risk"].append("Emergency budget allocation for response")
            recommendations["risk"].append("Staff briefing on competitive situation")
        
        recommendations["risk"].append("Document all market changes")
        recommendations["risk"].append("Prepare contingency plans")
        
        # Limit to top recommendations
        recommendations["priority"] = recommendations["priority"][:4]
        recommendations["pricing"] = recommendations["pricing"][:3]
        recommendations["marketing"] = recommendations["marketing"][:4]
        recommendations["risk"] = recommendations["risk"][:3]
        
        return recommendations
    
    def _determine_timeline(self, analysis: Dict) -> Dict:
        """Determine action timeline"""
        urgency = analysis.get("recommended_urgency", "medium").lower()
        impact = analysis.get("impact_level", "medium").lower()
        
        if urgency == "high":
            return {
                "immediate": "0-48 hours: Emergency response, review pricing, launch counter-campaign",
                "short_term": "1-2 weeks: Implement adjustments, monitor results",
                "medium_term": "1-3 months: Evaluate effectiveness, refine strategy"
            }
        elif urgency == "medium":
            return {
                "immediate": "1 week: Strategy meeting, data gathering",
                "short_term": "2-4 weeks: Implement selected tactics",
                "medium_term": "2-6 months: Monitor and optimize"
            }
        else:
            return {
                "immediate": "2 weeks: Review options",
                "short_term": "1-2 months: Gradual implementation",
                "medium_term": "3-6 months: Long-term positioning"
            }
    
    def _define_metrics(self, analysis: Dict, business: Dict) -> List[str]:
        """Define success metrics"""
        metrics = [
            "Market share percentage",
            "Customer retention rate",
            "Average transaction value",
            "Customer acquisition cost"
        ]
        
        insights = analysis.get("key_insights", [])
        
        if any("price" in i.lower() for i in insights):
            metrics.append("Price perception score")
        
        if any("promotion" in i.lower() for i in insights):
            metrics.append("Promotion response rate")
        
        return metrics[:6]
    
    def _create_error_response(self, error: str) -> str:
        """Create error response"""
        return json.dumps({
            "error": True,
            "message": f"Strategy generation failed: {error}",
            "priority_actions": ["Review analysis input data"],
            "pricing_strategy": [],
            "marketing_tactics": [],
            "risk_mitigation": []
        }, indent=2)


if __name__ == "__main__":
    print("Agent C: The Strategist - Ready")
    print("Use war_room_demo.py to see the full pipeline in action")
