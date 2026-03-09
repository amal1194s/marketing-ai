"""
Agent B: The Analyst
Market Intelligence AI System - Competitor Impact Analysis Agent

Analyzes competitor activity and evaluates business impact for small businesses.
"""

import json
import re
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class AnalysisResult:
    """Structure for analysis output"""
    impact_level: str  # low, medium, high
    summary: str
    pricing_gap: str
    market_risk: str
    recommended_urgency: str  # low, medium, high
    key_insights: List[str]
    price_difference_percent: Optional[float] = None  # Percent difference vs competitors
    threat_score: Optional[float] = None  # Overall threat score 1-10
    response_type: Optional[str] = None  # hold_position, promotion_response, price_adjustment, product_differentiation
    competitor_breakdown: Optional[List[Dict]] = None  # Per-competitor threat analysis

    def to_json(self) -> str:
        """Convert analysis to JSON format with validation"""
        try:
            # Validate all fields are strings and list
            result = {
                "impact_level": str(self.impact_level) if self.impact_level else "low",
                "summary": str(self.summary) if self.summary else "No analysis available",
                "pricing_gap": str(self.pricing_gap) if self.pricing_gap else "No pricing data",
                "market_risk": str(self.market_risk) if self.market_risk else "Unknown risk",
                "recommended_urgency": str(self.recommended_urgency) if self.recommended_urgency else "low",
                "key_insights": [str(i) for i in (self.key_insights or [])],
                "price_difference_percent": round(self.price_difference_percent, 2) if self.price_difference_percent is not None else None,
                "threat_score": round(self.threat_score, 1) if self.threat_score is not None else None,
                "threat_score_formula": "Price Gap (0-4) + Offer Competition (0-4) + Audience Overlap (0-2) = 1-10",
                "response_type": str(self.response_type) if self.response_type else None,
                "competitor_breakdown": self.competitor_breakdown if self.competitor_breakdown else []
            }
            # Ensure valid JSON
            return json.dumps(result, indent=2, ensure_ascii=False)
        except Exception as e:
            # Fallback to safe JSON
            return json.dumps({
                "impact_level": "low",
                "summary": "Analysis error occurred",
                "pricing_gap": "Unable to analyze",
                "market_risk": "Unable to assess",
                "recommended_urgency": "low",
                "key_insights": ["Analysis could not be completed"],
                "price_difference_percent": None,
                "threat_score": None,
                "threat_score_formula": "Price Gap (0-4) + Offer Competition (0-4) + Audience Overlap (0-2) = 1-10",
                "response_type": None,
                "competitor_breakdown": []
            }, indent=2)


class AgentBAnalyst:
    """
    Agent B: The Analyst
    
    Analyzes competitor intelligence and evaluates business impact.
    Provides strategic insights for small business owners.
    """
    
    def __init__(self):
        self.analysis_factors = [
            "price_differences",
            "new_offers_promotions",
            "product_launches",
            "target_audience_overlap",
            "market_positioning"
        ]
    
    def analyze(self, business_profile: Dict[str, Any], competitor_findings: Dict[str, Any]) -> str:
        """
        Main analysis method that compares business profile with competitor findings.
        
        Args:
            business_profile: Dictionary containing business information
            competitor_findings: Dictionary containing competitor data from Scout Agent
            
        Returns:
            JSON string with analysis results
        """
        try:
            # Validate inputs
            if not business_profile or not competitor_findings:
                return self._create_error_response("Missing required input data")
            
            # Extract key information safely
            business_pricing = business_profile.get("pricing", {}) or {}
            business_products = business_profile.get("products", []) or []
            business_target_audience = business_profile.get("target_audience", {}) or {}
            
            competitors = competitor_findings.get("competitors", []) or []
            
            if not competitors:
                return self._create_no_data_response()
            
            # Perform analysis with error handling
            pricing_analysis = self._analyze_pricing(business_pricing, competitors)
            offers_analysis = self._analyze_offers(competitor_findings, competitors)
            product_analysis = self._analyze_products(business_products, competitors)
            audience_analysis = self._analyze_audience(business_target_audience, competitors)
            positioning_analysis = self._analyze_positioning(business_profile, competitors)
            
            # Determine impact level
            impact_level = self._calculate_impact_level(
                pricing_analysis, offers_analysis, product_analysis, 
                audience_analysis, positioning_analysis
            )
            
            # Generate strategic insights
            key_insights = self._generate_strategic_insights(
                pricing_analysis, offers_analysis, product_analysis,
                audience_analysis, positioning_analysis, competitors
            )
            
            # Calculate threat score (1-10)
            threat_score = self._calculate_threat_score(
                pricing_analysis, offers_analysis, audience_analysis
            )
            
            # Determine recommended response type
            response_type = self._determine_response_type(
                pricing_analysis, offers_analysis, product_analysis, threat_score
            )
            
            # Create per-competitor breakdown
            competitor_breakdown = self._create_competitor_breakdown(
                competitors, business_pricing, business_target_audience
            )
            
            # Create detailed pricing gap explanation
            pricing_gap_text = self._create_pricing_gap_explanation(pricing_analysis)
            
            # Create analysis result
            result = AnalysisResult(
                impact_level=impact_level,
                summary=self._create_summary(impact_level, competitors, pricing_analysis, offers_analysis),
                pricing_gap=pricing_gap_text,
                market_risk=self._assess_market_risk(impact_level, audience_analysis, pricing_analysis, offers_analysis),
                recommended_urgency=self._determine_urgency(impact_level, pricing_analysis, offers_analysis),
                key_insights=key_insights[:3],  # Top 3 most important insights
                price_difference_percent=pricing_analysis.get("difference_percent") if pricing_analysis.get("has_data") else None,
                threat_score=threat_score,
                response_type=response_type,
                competitor_breakdown=competitor_breakdown
            )
            
            return result.to_json()
            
        except Exception as e:
            # Robust error handling - always return valid JSON
            return self._create_error_response(f"Analysis error: {str(e)}")
    
    def _analyze_pricing(self, business_pricing: Dict, competitors: List[Dict]) -> Dict:
        """Analyze price differences between business and competitors - automatically detect gaps"""
        try:
            if not business_pricing or not competitors:
                return {
                    "impact": "low", 
                    "description": "Insufficient pricing data to compare",
                    "has_data": False
                }
            
            business_avg_price = float(business_pricing.get("average_price", 0))
            business_min = float(business_pricing.get("min_price", 0))
            business_max = float(business_pricing.get("max_price", 0))
            
            # Collect all competitor pricing data
            competitor_data = []
            for comp in competitors:
                comp_pricing = comp.get("pricing", {})
                if comp_pricing and comp_pricing.get("average_price"):
                    competitor_data.append({
                        "name": comp.get("name", "Unknown"),
                        "avg": float(comp_pricing.get("average_price", 0)),
                        "min": float(comp_pricing.get("min_price", 0)),
                        "max": float(comp_pricing.get("max_price", 0))
                    })
            
            if not competitor_data or business_avg_price == 0:
                return {
                    "impact": "low", 
                    "description": "Unable to compare pricing effectively",
                    "has_data": False
                }
            
            # Calculate competitor statistics
            competitor_prices = [c["avg"] for c in competitor_data]
            avg_competitor_price = sum(competitor_prices) / len(competitor_prices)
            min_competitor_price = min(competitor_prices)
            max_competitor_price = max(competitor_prices)
            
            # Find cheapest and most expensive competitor
            cheapest_comp = min(competitor_data, key=lambda x: x["avg"])
            most_expensive_comp = max(competitor_data, key=lambda x: x["avg"])
            
            # Calculate price differences
            price_diff_percent = ((business_avg_price - avg_competitor_price) / avg_competitor_price) * 100
            vs_cheapest_percent = ((business_avg_price - cheapest_comp["avg"]) / cheapest_comp["avg"]) * 100
            vs_most_expensive_percent = ((business_avg_price - most_expensive_comp["avg"]) / most_expensive_comp["avg"]) * 100
            
            # Determine pricing position
            if business_avg_price < min_competitor_price:
                position = "lowest"
            elif business_avg_price > max_competitor_price:
                position = "highest"
            elif business_avg_price < avg_competitor_price:
                position = "below_average"
            elif business_avg_price > avg_competitor_price:
                position = "above_average"
            else:
                position = "at_average"
            
            # Determine impact strategically
            impact = "low"
            strategic_notes = []
            
            if price_diff_percent > 25:
                impact = "high"
                strategic_notes.append("significant premium pricing risk")
            elif price_diff_percent > 15:
                impact = "medium"
                strategic_notes.append("moderate pricing disadvantage")
            elif price_diff_percent > 5:
                impact = "low"
                strategic_notes.append("slight premium positioning")
            elif price_diff_percent < -15:
                impact = "low"
                strategic_notes.append("strong value positioning")
            elif price_diff_percent < -5:
                impact = "low"
                strategic_notes.append("competitive pricing advantage")
            
            # Create strategic description
            description = f"Your average price (${business_avg_price:.2f}) is {abs(price_diff_percent):.1f}% "
            description += "higher than" if price_diff_percent > 0 else "lower than"
            description += f" market average (${avg_competitor_price:.2f}). "
            
            if position == "highest":
                description += f"You're the most expensive option - {abs(vs_cheapest_percent):.1f}% above {cheapest_comp['name']}."
            elif position == "lowest":
                description += f"You're the most affordable - {abs(vs_cheapest_percent):.1f}% below competitors."
            elif abs(price_diff_percent) > 15:
                description += f"Significant gap vs {cheapest_comp['name']} (${cheapest_comp['avg']:.2f})."
            
            return {
                "impact": impact,
                "description": description,
                "has_data": True,
                "business_price": business_avg_price,
                "competitor_avg": avg_competitor_price,
                "min_competitor": min_competitor_price,
                "max_competitor": max_competitor_price,
                "difference_percent": price_diff_percent,
                "vs_cheapest_percent": vs_cheapest_percent,
                "cheapest_competitor": cheapest_comp["name"],
                "most_expensive_competitor": most_expensive_comp["name"],
                "position": position,
                "strategic_notes": strategic_notes,
                "competitor_count": len(competitor_data)
            }
            
        except Exception as e:
            return {
                "impact": "low", 
                "description": "Error analyzing pricing",
                "has_data": False
            }
    
    def _analyze_offers(self, competitor_findings: Dict, competitors: List[Dict]) -> Dict:
        """Analyze and automatically detect competitor offers and promotions"""
        try:
            active_promotions = []
            offer_details = []
            
            for comp in competitors:
                comp_name = comp.get("name", "Unknown")
                promotions = comp.get("promotions", []) or []
                new_offers = comp.get("new_offers", []) or []
                
                for promo in promotions:
                    active_promotions.append(promo)
                    offer_details.append({
                        "competitor": comp_name,
                        "offer": str(promo),
                        "type": self._classify_offer_type(str(promo))
                    })
                
                for offer in new_offers:
                    active_promotions.append(offer)
                    offer_details.append({
                        "competitor": comp_name,
                        "offer": str(offer),
                        "type": self._classify_offer_type(str(offer)),
                        "is_new": True
                    })
            
            if not active_promotions:
                return {
                    "impact": "low", 
                    "count": 0, 
                    "aggressive": False,
                    "has_offers": False
                }
            
            # Detect aggressive promotions automatically
            aggressive_indicators = [
                r'\b(30|40|50|60|70|80|90)%\s*(off|discount)',  # High discounts
                r'\bbogo\b',  # Buy one get one
                r'\bbuy\s+one\s+get\s+one\b',
                r'\bfree\b',  # Free offers
                r'\b2\s*for\s*1\b',  # 2 for 1
                r'\bhalf\s*price\b',  # Half price
                r'\b0\s*%\b'  # Zero percent / free
            ]
            
            aggressive_offers = []
            for detail in offer_details:
                offer_text = detail["offer"].lower()
                if any(re.search(pattern, offer_text, re.IGNORECASE) for pattern in aggressive_indicators):
                    aggressive_offers.append(detail)
            
            is_aggressive = len(aggressive_offers) > 0
            
            # Categorize offer types
            offer_types = {}
            for detail in offer_details:
                offer_type = detail["type"]
                offer_types[offer_type] = offer_types.get(offer_type, 0) + 1
            
            # Determine impact
            if is_aggressive and len(active_promotions) >= 3:
                impact = "high"
            elif is_aggressive or len(active_promotions) >= 4:
                impact = "medium"
            elif len(active_promotions) >= 2:
                impact = "low"
            else:
                impact = "low"
            
            return {
                "impact": impact,
                "count": len(active_promotions),
                "aggressive": is_aggressive,
                "aggressive_count": len(aggressive_offers),
                "has_offers": True,
                "promotions": active_promotions,
                "offer_details": offer_details,
                "offer_types": offer_types,
                "competitors_with_offers": len(set(d["competitor"] for d in offer_details))
            }
            
        except Exception as e:
            return {
                "impact": "low", 
                "count": 0, 
                "aggressive": False,
                "has_offers": False
            }
    
    def _classify_offer_type(self, offer_text: str) -> str:
        """Automatically classify offer type based on text"""
        offer_lower = offer_text.lower()
        
        # Classification rules
        if any(word in offer_lower for word in ["loyalty", "reward", "points", "member"]):
            return "loyalty"
        elif any(word in offer_lower for word in ["bogo", "buy one get one", "2 for 1"]):
            return "bogo"
        elif any(word in offer_lower for word in ["bundle", "combo", "package"]):
            return "bundle"
        elif any(word in offer_lower for word in ["free", "complimentary"]):
            return "free"
        elif any(word in offer_lower for word in ["subscription", "monthly", "unlimited"]):
            return "subscription"
        elif any(word in offer_lower for word in ["%", "discount", "off", "save"]):
            return "discount"
        elif any(word in offer_lower for word in ["student", "senior", "military"]):
            return "segment_discount"
        else:
            return "other"
    
    def _analyze_products(self, business_products: List, competitors: List[Dict]) -> Dict:
        """Analyze product launches and bundles from competitors"""
        new_products_count = 0
        bundle_count = 0
        
        for comp in competitors:
            new_products = comp.get("new_products", [])
            bundles = comp.get("bundles", [])
            new_products_count += len(new_products)
            bundle_count += len(bundles)
        
        total_new = new_products_count + bundle_count
        
        if total_new > 5:
            impact = "high"
        elif total_new > 2:
            impact = "medium"
        else:
            impact = "low"
        
        return {
            "impact": impact,
            "new_products": new_products_count,
            "bundles": bundle_count,
            "innovation_level": "high" if total_new > 5 else "medium" if total_new > 2 else "low"
        }
    
    def _analyze_audience(self, business_audience: Dict, competitors: List[Dict]) -> Dict:
        """Analyze target audience overlap"""
        if not business_audience:
            return {"impact": "medium", "overlap": "unknown"}
        
        business_demographics = set(business_audience.get("demographics", []))
        business_interests = set(business_audience.get("interests", []))
        
        overlap_scores = []
        
        for comp in competitors:
            comp_audience = comp.get("target_audience", {})
            comp_demographics = set(comp_audience.get("demographics", []))
            comp_interests = set(comp_audience.get("interests", []))
            
            if comp_demographics or comp_interests:
                demo_overlap = len(business_demographics & comp_demographics) / max(len(business_demographics), 1)
                interest_overlap = len(business_interests & comp_interests) / max(len(business_interests), 1)
                overlap_scores.append((demo_overlap + interest_overlap) / 2)
        
        if not overlap_scores:
            return {"impact": "medium", "overlap": "unknown"}
        
        avg_overlap = sum(overlap_scores) / len(overlap_scores)
        
        if avg_overlap > 0.7:
            impact = "high"
            overlap = "very high"
        elif avg_overlap > 0.4:
            impact = "medium"
            overlap = "moderate"
        else:
            impact = "low"
            overlap = "low"
        
        return {"impact": impact, "overlap": overlap, "overlap_score": avg_overlap}
    
    def _analyze_positioning(self, business_profile: Dict, competitors: List[Dict]) -> Dict:
        """Analyze market positioning differences"""
        business_positioning = business_profile.get("positioning", "")
        
        competitor_positions = [
            comp.get("positioning", "") for comp in competitors if comp.get("positioning")
        ]
        
        if not business_positioning:
            return {"impact": "low", "differentiation": "unclear"}
        
        # Simple differentiation check
        similar_positioning = sum(
            1 for pos in competitor_positions 
            if any(word in pos.lower() for word in business_positioning.lower().split() if len(word) > 4)
        )
        
        if similar_positioning > len(competitor_positions) * 0.6:
            impact = "medium"
            differentiation = "weak"
        else:
            impact = "low"
            differentiation = "strong"
        
        return {
            "impact": impact,
            "differentiation": differentiation,
            "similar_competitors": similar_positioning
        }
    
    def _calculate_impact_level(self, pricing: Dict, offers: Dict, products: Dict, 
                                 audience: Dict, positioning: Dict) -> str:
        """Calculate overall impact level"""
        impact_scores = {
            "high": 3,
            "medium": 2,
            "low": 1
        }
        
        total_score = (
            impact_scores.get(pricing.get("impact", "low"), 1) * 2 +  # Pricing weighted more
            impact_scores.get(offers.get("impact", "low"), 1) * 1.5 +  # Offers weighted more
            impact_scores.get(products.get("impact", "low"), 1) +
            impact_scores.get(audience.get("impact", "low"), 1) +
            impact_scores.get(positioning.get("impact", "low"), 1)
        )
        
        max_score = 3 * 2 + 3 * 1.5 + 3 * 3  # Maximum possible score
        normalized_score = total_score / max_score
        
        if normalized_score > 0.65:
            return "high"
        elif normalized_score > 0.40:
            return "medium"
        else:
            return "low"
    
    def _generate_strategic_insights(self, pricing: Dict, offers: Dict, products: Dict,
                                    audience: Dict, positioning: Dict, competitors: List[Dict]) -> List[str]:
        """Generate ultra-concise key insights"""
        insights = []
        priority_scores = []
        
        try:
            # PRICING INSIGHTS - Ultra concise
            if pricing.get("has_data"):
                price_diff = pricing.get("difference_percent", 0)
                
                if price_diff > 20:
                    insights.append("Price undercutting detected")
                    priority_scores.append(10)
                elif price_diff > 10:
                    insights.append("Higher pricing than competitors")
                    priority_scores.append(8)
                elif price_diff < -15:
                    insights.append("Strong price advantage")
                    priority_scores.append(5)
                elif abs(price_diff) > 5:
                    if price_diff > 0:
                        insights.append("Above market pricing")
                        priority_scores.append(7)
                    else:
                        insights.append("Below market pricing")
                        priority_scores.append(4)
            
            # OFFERS INSIGHTS - Ultra concise
            if offers.get("has_offers"):
                offer_count = offers.get("count", 0)
                aggressive = offers.get("aggressive", False)
                
                if aggressive:
                    insights.append("Aggressive promotions active")
                    priority_scores.append(11)
                elif offer_count >= 3:
                    insights.append("Multiple competitor promotions")
                    priority_scores.append(7)
                elif offer_count >= 1:
                    insights.append("Promotional overlap")
                    priority_scores.append(6)
            
            # AUDIENCE INSIGHTS - Ultra concise
            overlap = audience.get("overlap", "unknown")
            if overlap == "very high":
                insights.append("Same target audience")
                priority_scores.append(9)
            elif overlap == "moderate":
                insights.append("Moderate audience overlap")
                priority_scores.append(6)
            elif overlap == "low":
                insights.append("Different target audience")
                priority_scores.append(3)
            
            # PRODUCT INSIGHTS - Ultra concise
            new_products = products.get("new_products", 0)
            bundles = products.get("bundles", 0)
            
            if new_products >= 5 or bundles >= 3:
                insights.append("High product innovation")
                priority_scores.append(8)
            elif new_products >= 2 or bundles >= 1:
                insights.append("New product launches")
                priority_scores.append(6)
            
            # POSITIONING INSIGHTS - Ultra concise
            if positioning.get("differentiation") == "weak":
                insights.append("Similar positioning")
                priority_scores.append(7)
            elif positioning.get("differentiation") == "strong":
                insights.append("Strong differentiation")
                priority_scores.append(2)
            
            # COMPETITIVE DENSITY
            comp_count = len(competitors)
            if comp_count >= 5 and not any("compet" in i.lower() for i in insights):
                insights.append("Crowded market")
                priority_scores.append(6)
            
            # FALLBACK - Stable market
            if not insights:
                insights.append("No immediate threats")
                priority_scores.append(1)
            
            # Sort insights by priority and return top 3
            sorted_insights = [insight for _, insight in sorted(zip(priority_scores, insights), reverse=True)]
            return sorted_insights
            
        except Exception as e:
            return ["Analysis incomplete"]
    
    def _create_pricing_gap_explanation(self, pricing_analysis: Dict) -> str:
        """Create detailed, strategic pricing gap explanation"""
        try:
            if not pricing_analysis.get("has_data"):
                return "No competitor pricing data available for comparison"
            
            business_price = pricing_analysis.get("business_price", 0)
            competitor_avg = pricing_analysis.get("competitor_avg", 0)
            diff_percent = pricing_analysis.get("difference_percent", 0)
            position = pricing_analysis.get("position", "")
            cheapest = pricing_analysis.get("cheapest_competitor", "")
            most_expensive = pricing_analysis.get("most_expensive_competitor", "")
            min_comp = pricing_analysis.get("min_competitor", 0)
            max_comp = pricing_analysis.get("max_competitor", 0)
            
            explanation = f"Your pricing: ${business_price:.2f} average. "
            explanation += f"Market range: ${min_comp:.2f} - ${max_comp:.2f}. "
            
            if abs(diff_percent) < 5:
                explanation += f"You're competitively priced at market average (${competitor_avg:.2f}). "
                explanation += "Maintain current pricing and focus on value differentiation."
            elif diff_percent > 0:
                explanation += f"You're {abs(diff_percent):.1f}% above market average (${competitor_avg:.2f}). "
                if position == "highest":
                    explanation += f"{cheapest} is cheapest at ${min_comp:.2f}. "
                    explanation += "Premium positioning requires exceptional quality/service to justify cost."
                else:
                    explanation += f"Price-sensitive customers may prefer {cheapest} (${min_comp:.2f}). "
                    explanation += "Emphasize quality, service, or unique benefits to justify premium."
            else:
                explanation += f"You're {abs(diff_percent):.1f}% below market average (${competitor_avg:.2f}). "
                if position == "lowest":
                    explanation += "Strong value positioning. Use this advantage in marketing. "
                    explanation += "Consider if you have room for strategic price increases."
                else:
                    explanation += "Competitive pricing advantage. Attract price-conscious customers while maintaining margins."
            
            return explanation
            
        except Exception as e:
            return "Unable to generate detailed pricing analysis"
    
    def _create_summary(self, impact_level: str, competitors: List[Dict], 
                       pricing_analysis: Dict, offers_analysis: Dict) -> str:
        """"Create strategic executive summary"""
        try:
            comp_count = len(competitors)
            comp_names = [c.get("name", "Unknown") for c in competitors[:3]]
            
            summary = f"{impact_level.capitalize()} competitive pressure from {comp_count} competitor(s)"
            if comp_count <= 3:
                summary += f" ({', '.join(comp_names)})"
            summary += ". "
            
            # Add most critical factor
            if offers_analysis.get("aggressive"):
                summary += f"{offers_analysis.get('aggressive_count', 0)} aggressive promotions active - immediate response needed. "
            elif pricing_analysis.get("impact") == "high":
                summary += f"Significant pricing gap detected ({abs(pricing_analysis.get('difference_percent', 0)):.0f}%). "
            elif pricing_analysis.get("has_data"):
                summary += f"Pricing position: {pricing_analysis.get('position', 'competitive').replace('_', ' ')}. "
            
            # Add recommendation
            if impact_level == "high":
                summary += "Strategic action required within 48 hours."
            elif impact_level == "medium":
                summary += "Monitor closely and prepare response."
            else:
                summary += "Maintain current strategy."
                
            return summary
            
        except Exception as e:
            comp_count = len(competitors) if competitors else 0
            return f"{impact_level.capitalize()} competitive activity from {comp_count} competitor(s)"
    
    def _assess_market_risk(self, impact_level: str, audience_analysis: Dict, 
                           pricing_analysis: Dict, offers_analysis: Dict) -> str:
        """Assess strategic risk of losing customers with specific scenarios"""
        try:
            risk_factors = []
            risk_level = "Low"
            
            # Analyze each risk factor
            if impact_level == "high":
                risk_factors.append("high competitive pressure")
            
            if audience_analysis.get("overlap") == "very high":
                risk_factors.append(f"direct competition for same customers ({audience_analysis.get('overlap_score', 0)*100:.0f}% overlap)")
            
            if pricing_analysis.get("impact") == "high":
                price_diff = pricing_analysis.get("difference_percent", 0)
                risk_factors.append(f"unfavorable pricing ({abs(price_diff):.0f}% above market)")
            
            if offers_analysis.get("aggressive"):
                aggressive_count = offers_analysis.get("aggressive_count", 0)
                risk_factors.append(f"{aggressive_count} aggressive competitor promotions")
            
            # Determine risk level and create strategic assessment
            if len(risk_factors) >= 3 or (offers_analysis.get("aggressive") and pricing_analysis.get("impact") == "high"):
                risk_level = "HIGH"
                assessment = f"HIGH RISK: {', '.join(risk_factors)}. "
                assessment += "Customers are highly likely to switch for better deals. "
                assessment += "ACTION: Launch retention campaign immediately. "
                assessment += "Contact high-value customers directly. Consider price matching or value-adds."
                
            elif len(risk_factors) >= 2:
                risk_level = "MODERATE"
                assessment = f"Moderate risk: {', '.join(risk_factors)}. "
                assessment += "Some customer attrition expected, especially price-sensitive segments. "
                assessment += "ACTION: Monitor sales data daily. Prepare promotional response. "
                assessment += "Strengthen customer relationships through engagement."
                
            elif len(risk_factors) == 1:
                risk_level = "LOW-MODERATE"
                assessment = f"Low-moderate risk: {risk_factors[0]}. "
                assessment += "Minimal immediate threat but require monitoring. "
                assessment += "ACTION: Stay alert to market changes. "
                assessment += "Focus on service quality and customer satisfaction."
                
            else:
                risk_level = "LOW"
                assessment = "Low risk: Your competitive position is stable. "
                assessment += "No immediate threats to customer retention detected. "
                assessment += "ACTION: Maintain current standards. "
                assessment += "Continue monitoring competitors monthly. Focus on customer experience and loyalty."
            
            return assessment
            
        except Exception as e:
            return "Unable to assess market risk. Monitor competitors regularly."
    
    def _determine_urgency(self, impact_level: str, pricing_analysis: Dict, offers_analysis: Dict) -> str:
        """Determine recommended urgency level with strategic reasoning"""
        try:
            # Critical urgency triggers
            if offers_analysis.get("aggressive") and offers_analysis.get("aggressive_count", 0) >= 2:
                return "high"  # Multiple aggressive offers = immediate threat
            
            if impact_level == "high" and pricing_analysis.get("difference_percent", 0) > 25:
                return "high"  # Extreme pricing disadvantage
            
            # High urgency triggers  
            if impact_level == "high":
                return "high"
            
            if offers_analysis.get("aggressive"):
                return "high"  # Any aggressive promotion needs fast response
            
            # Medium urgency triggers
            if impact_level == "medium":
                return "medium"
            
            if pricing_analysis.get("impact") == "medium" or offers_analysis.get("count", 0) >= 3:
                return "medium"
            
            # Default to low
            return "low"
            
        except Exception as e:
            return "medium"  # Safe default
    
    def _calculate_threat_score(self, pricing_analysis: Dict, offers_analysis: Dict, 
                               audience_analysis: Dict) -> float:
        """
        Calculate overall threat score from 1-10 based on:
        - Price gap (0-4 points)
        - Offer competition (0-4 points)
        - Target audience overlap (0-2 points)
        """
        try:
            score = 0.0
            
            # PRICE GAP SCORING (0-4 points)
            if pricing_analysis.get("has_data"):
                price_diff = abs(pricing_analysis.get("difference_percent", 0))
                
                if price_diff > 30:
                    score += 4.0  # Extreme price gap
                elif price_diff > 20:
                    score += 3.5  # Major price gap
                elif price_diff > 15:
                    score += 3.0  # Significant gap
                elif price_diff > 10:
                    score += 2.5  # Moderate gap
                elif price_diff > 5:
                    score += 2.0  # Small gap
                elif price_diff > 2:
                    score += 1.0  # Minimal gap
                # else: 0 points for no significant gap
            
            # OFFER COMPETITION SCORING (0-4 points)
            if offers_analysis.get("has_offers"):
                offer_count = offers_analysis.get("count", 0)
                aggressive_count = offers_analysis.get("aggressive_count", 0)
                
                if aggressive_count >= 3:
                    score += 4.0  # Multiple aggressive offers
                elif aggressive_count >= 2:
                    score += 3.5  # Two aggressive offers
                elif aggressive_count >= 1:
                    score += 3.0  # One aggressive offer
                elif offer_count >= 5:
                    score += 2.5  # Many non-aggressive offers
                elif offer_count >= 3:
                    score += 2.0  # Several offers
                elif offer_count >= 1:
                    score += 1.0  # Few offers
                # else: 0 points for no offers
            
            # TARGET AUDIENCE OVERLAP SCORING (0-2 points)
            overlap = audience_analysis.get("overlap", "unknown").lower()
            
            if overlap == "very high":
                score += 2.0  # Same target audience = high threat
            elif overlap == "high":
                score += 1.5  # High overlap
            elif overlap == "moderate":
                score += 1.0  # Moderate overlap
            elif overlap == "low":
                score += 0.5  # Low overlap
            # else: 0 points for no overlap or unknown
            
            # Normalize to 1-10 scale
            # Max possible: 4 + 4 + 2 = 10
            # Min possible: 0
            # Add 1 to shift range from 0-10 to 1-10
            final_score = min(10.0, max(1.0, score + 1.0))
            
            return final_score
            
        except Exception as e:
            return 5.0  # Neutral threat if calculation fails
    
    def _determine_response_type(self, pricing_analysis: Dict, offers_analysis: Dict,
                                 product_analysis: Dict, threat_score: float) -> str:
        """
        Determine recommended response type based on competitive situation.
        Returns one of: hold_position, promotion_response, price_adjustment, product_differentiation
        """
        try:
            # Check for aggressive promotional competition
            aggressive_offers = offers_analysis.get("aggressive", False)
            offer_count = offers_analysis.get("count", 0)
            
            # Check pricing situation
            price_diff = pricing_analysis.get("difference_percent", 0)
            has_price_data = pricing_analysis.get("has_data", False)
            
            # Check product competition
            new_products = product_analysis.get("new_products", 0)
            
            # Decision logic (prioritized)
            
            # 1. PROMOTION RESPONSE - if facing aggressive promotions
            if aggressive_offers or offer_count >= 3:
                return "promotion_response"
            
            # 2. PRICE ADJUSTMENT - if significantly overpriced
            if has_price_data and price_diff > 15:
                return "price_adjustment"
            
            # 3. PRODUCT DIFFERENTIATION - if many new products or high innovation
            if new_products >= 3 or threat_score >= 7.0:
                return "product_differentiation"
            
            # 4. HOLD POSITION - stable situation
            if threat_score < 4.0:
                return "hold_position"
            
            # Default: Product differentiation for medium threats
            return "product_differentiation"
            
        except Exception as e:
            return "hold_position"  # Safe default
    
    def _create_competitor_breakdown(self, competitors: List[Dict], 
                                     business_pricing: Dict, 
                                     business_target_audience: Dict) -> List[Dict]:
        """
        Create per-competitor threat analysis with clear reasons.
        Returns list of competitor breakdown dicts.
        """
        try:
            breakdown = []
            business_avg_price = float(business_pricing.get("average_price", 0))
            
            for comp in competitors:
                comp_name = comp.get("name", "Unknown Competitor")
                comp_pricing = comp.get("pricing", {})
                comp_avg_price = float(comp_pricing.get("average_price", 0)) if comp_pricing else 0
                
                # Calculate price comparison
                price_threat = "none"
                price_reason = ""
                if business_avg_price > 0 and comp_avg_price > 0:
                    price_diff_pct = ((business_avg_price - comp_avg_price) / comp_avg_price) * 100
                    if price_diff_pct > 20:
                        price_threat = "high"
                        price_reason = f"You're {price_diff_pct:.0f}% more expensive"
                    elif price_diff_pct > 10:
                        price_threat = "medium"
                        price_reason = f"You're {price_diff_pct:.0f}% more expensive"
                    elif price_diff_pct < -15:
                        price_threat = "low"
                        price_reason = f"You're {abs(price_diff_pct):.0f}% cheaper"
                    else:
                        price_threat = "low"
                        price_reason = "Similar pricing"
                
                # Analyze promotions
                promotions = comp.get("current_promotions", [])
                promo_count = len(promotions)
                promo_threat = "none"
                promo_reason = ""
                
                if promo_count == 0:
                    promo_threat = "none"
                    promo_reason = "No active promotions"
                else:
                    # Check for aggressive promotions
                    aggressive_promos = []
                    for promo in promotions:
                        promo_text = str(promo.get("title", "")) + " " + str(promo.get("description", ""))
                        if any(keyword in promo_text.lower() for keyword in ["30%", "40%", "50%", "60%", "70%", "80%", "90%", "bogo", "buy one get one", "free"]):
                            aggressive_promos.append(promo.get("title", "promotion"))
                    
                    if len(aggressive_promos) >= 2:
                        promo_threat = "high"
                        promo_reason = f"{len(aggressive_promos)} aggressive promotions"
                    elif len(aggressive_promos) >= 1:
                        promo_threat = "medium"
                        promo_reason = f"1 aggressive promotion"
                    elif promo_count >= 3:
                        promo_threat = "medium"
                        promo_reason = f"{promo_count} active promotions"
                    else:
                        promo_threat = "low"
                        promo_reason = f"{promo_count} promotion(s)"
                
                # Analyze audience overlap (simplified)
                comp_audience = comp.get("target_audience", {})
                overlap_threat = "unknown"
                overlap_reason = "Unable to determine"
                
                if comp_audience and business_target_audience:
                    # Simple heuristic based on demographics
                    business_demos = business_target_audience.get("demographics", [])
                    comp_demos = comp_audience.get("demographics", [])
                    
                    if business_demos and comp_demos:
                        # Calculate overlap
                        business_set = set([str(d).lower() for d in business_demos])
                        comp_set = set([str(d).lower() for d in comp_demos])
                        overlap_count = len(business_set & comp_set)
                        
                        if overlap_count >= 2:
                            overlap_threat = "high"
                            overlap_reason = "Same target audience"
                        elif overlap_count == 1:
                            overlap_threat = "medium"
                            overlap_reason = "Some audience overlap"
                        else:
                            overlap_threat = "low"
                            overlap_reason = "Different audience"
                
                # Determine overall threat level for this competitor
                threat_levels = {"high": 3, "medium": 2, "low": 1, "none": 0, "unknown": 1}
                overall_score = (
                    threat_levels.get(price_threat, 0) +
                    threat_levels.get(promo_threat, 0) +
                    threat_levels.get(overlap_threat, 0)
                )
                
                if overall_score >= 7:
                    overall_threat = "high"
                elif overall_score >= 4:
                    overall_threat = "medium"
                else:
                    overall_threat = "low"
                
                # Create reasons list
                reasons = []
                if price_reason:
                    reasons.append(price_reason)
                if promo_reason and promo_threat != "none":
                    reasons.append(promo_reason)
                if overlap_reason and overlap_threat != "unknown":
                    reasons.append(overlap_reason)
                
                breakdown.append({
                    "competitor_name": comp_name,
                    "threat_level": overall_threat,
                    "reasons": reasons if reasons else ["Standard competitive presence"]
                })
            
            return breakdown
            
        except Exception as e:
            return []  # Return empty list on error
    
    def _create_error_response(self, error_message: str) -> str:
        """Create robust error response in valid JSON format"""
        try:
            safe_message = str(error_message)[:200] if error_message else "Unknown error"
            return json.dumps({
                "impact_level": "low",
                "summary": f"Analysis incomplete: {safe_message}",
                "pricing_gap": "Unable to analyze pricing - insufficient data",
                "market_risk": "Cannot assess risk without complete data. Manual review recommended.",
                "recommended_urgency": "low",
                "key_insights": [
                    "Analysis could not be completed due to data issues",
                    "Verify input data format matches requirements",
                    "Contact support if problem persists"
                ],
                "price_difference_percent": None,
                "threat_score": None,
                "threat_score_formula": "Price Gap (0-4) + Offer Competition (0-4) + Audience Overlap (0-2) = 1-10",
                "response_type": None,
                "competitor_breakdown": []
            }, indent=2, ensure_ascii=False)
        except:
            # Ultimate fallback - guaranteed valid JSON
            return '{"impact_level":"low","summary":"Analysis error","pricing_gap":"N/A","market_risk":"Unable to assess","recommended_urgency":"low","key_insights":["Error occurred during analysis"],"price_difference_percent":null,"threat_score":null,"threat_score_formula":"Price Gap (0-4) + Offer Competition (0-4) + Audience Overlap (0-2) = 1-10","response_type":null,"competitor_breakdown":[]}'
    
    def _create_no_data_response(self) -> str:
        """Create response when no competitor data is available"""
        try:
            return json.dumps({
                "impact_level": "low",
                "summary": "No competitor data available for analysis. Unable to assess competitive threats.",
                "pricing_gap": "No competitor pricing data available for comparison. Market research needed.",
                "market_risk": "Cannot assess without competitor information. Recommendation: Conduct market research to identify competitors and gather intelligence.",
                "recommended_urgency": "low",
                "key_insights": [
                    "Zero competitors detected in data feed",
                    "Recommend activating Scout Agent to collect competitor intelligence",
                    "Focus on customer satisfaction and retention until competitor data available"
                ],
                "price_difference_percent": None,
                "threat_score": None,
                "threat_score_formula": "Price Gap (0-4) + Offer Competition (0-4) + Audience Overlap (0-2) = 1-10",
                "response_type": "hold_position",
                "competitor_breakdown": []
            }, indent=2, ensure_ascii=False)
        except:
            return '{"impact_level":"low","summary":"No competitor data","pricing_gap":"N/A","market_risk":"Unknown","recommended_urgency":"low","key_insights":["No data available"],"price_difference_percent":null,"threat_score":null,"threat_score_formula":"Price Gap (0-4) + Offer Competition (0-4) + Audience Overlap (0-2) = 1-10","response_type":"hold_position","competitor_breakdown":[]}'


# Example usage
def main():
    """Example usage of Agent B"""
    agent = AgentBAnalyst()
    
    # Example business profile
    business_profile = {
        "name": "Local Coffee Shop",
        "pricing": {
            "average_price": 5.50,
            "min_price": 3.00,
            "max_price": 8.00
        },
        "products": ["Coffee", "Pastries", "Sandwiches"],
        "target_audience": {
            "demographics": ["young professionals", "students"],
            "interests": ["coffee culture", "local business"]
        },
        "positioning": "Premium locally-sourced coffee experience"
    }
    
    # Example competitor findings (from Scout Agent)
    competitor_findings = {
        "competitors": [
            {
                "name": "Chain Coffee Co",
                "pricing": {
                    "average_price": 4.50
                },
                "promotions": ["Buy one get one 50% off", "Loyalty rewards"],
                "new_products": ["Seasonal lattes", "Breakfast bundle"],
                "target_audience": {
                    "demographics": ["young professionals", "families"],
                    "interests": ["convenience", "coffee"]
                },
                "positioning": "Fast, affordable coffee for everyone"
            }
        ]
    }
    
    # Perform analysis
    result = agent.analyze(business_profile, competitor_findings)
    print(result)


if __name__ == "__main__":
    main()
