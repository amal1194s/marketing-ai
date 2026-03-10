"""
Competitor Discovery Engine
Automatically identifies likely competitors based on business profile
"""

import re
from typing import List, Dict, Any, Optional
from dataclasses import dataclass


@dataclass
class CompetitorCandidate:
    """Structure for discovered competitor"""
    name: str
    category: str
    website_url: Optional[str]
    social_url: Optional[str]
    reason: str
    confidence_score: float  # 0.0 to 1.0
    
    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "category": self.category,
            "website_url": self.website_url,
            "social_url": self.social_url,
            "reason": self.reason,
            "confidence_score": round(self.confidence_score, 2)
        }


# Competitor database organized by category
COMPETITOR_DATABASE = {
    "fitness": [
        {"name": "Planet Fitness", "category": "Budget Gym", "price": "low", "audience": "beginners", "url": "https://planetfitness.com"},
        {"name": "LA Fitness", "category": "Full-Service Gym", "price": "medium", "audience": "general", "url": "https://lafitness.com"},
        {"name": "Gold's Gym", "category": "Bodybuilding Gym", "price": "medium", "audience": "serious lifters", "url": "https://goldsgym.com"},
        {"name": "Equinox", "category": "Luxury Gym", "price": "high", "audience": "professionals", "url": "https://equinox.com"},
        {"name": "CrossFit", "category": "CrossFit Box", "price": "high", "audience": "athletes", "url": "https://crossfit.com"},
        {"name": "Anytime Fitness", "category": "24/7 Gym", "price": "medium", "audience": "convenience seekers", "url": "https://anytimefitness.com"},
    ],
    "salon": [
        {"name": "Supercuts", "category": "Budget Hair Salon", "price": "low", "audience": "budget conscious", "url": "https://supercuts.com"},
        {"name": "Great Clips", "category": "Quick Cut Salon", "price": "low", "audience": "families", "url": "https://greatclips.com"},
        {"name": "Ulta Beauty", "category": "Beauty Salon & Retail", "price": "medium", "audience": "beauty enthusiasts", "url": "https://ulta.com"},
        {"name": "Sephora", "category": "Premium Beauty", "price": "high", "audience": "luxury seekers", "url": "https://sephora.com"},
        {"name": "Salon Republic", "category": "Premium Salon", "price": "high", "audience": "upscale clients", "url": "https://salonrepublic.com"},
        {"name": "Drybar", "category": "Blowout Bar", "price": "medium", "audience": "working women", "url": "https://thedrybar.com"},
    ],
    "pizza": [
        {"name": "Domino's", "category": "Pizza Chain", "price": "low", "audience": "budget families", "url": "https://dominos.com"},
        {"name": "Pizza Hut", "category": "Pizza Chain", "price": "low", "audience": "families", "url": "https://pizzahut.com"},
        {"name": "Papa John's", "category": "Pizza Chain", "price": "medium", "audience": "quality seekers", "url": "https://papajohns.com"},
        {"name": "Little Caesars", "category": "Budget Pizza", "price": "low", "audience": "value hunters", "url": "https://littlecaesars.com"},
        {"name": "MOD Pizza", "category": "Fast Casual Pizza", "price": "medium", "audience": "millennials", "url": "https://modpizza.com"},
        {"name": "Blaze Pizza", "category": "Artisan Fast Pizza", "price": "medium", "audience": "young professionals", "url": "https://blazepizza.com"},
    ],
    "coffee": [
        {"name": "Starbucks", "category": "Coffee Chain", "price": "medium", "audience": "professionals", "url": "https://starbucks.com"},
        {"name": "Dunkin'", "category": "Coffee & Donuts", "price": "low", "audience": "everyone", "url": "https://dunkindonuts.com"},
        {"name": "Peet's Coffee", "category": "Premium Coffee", "price": "medium", "audience": "coffee enthusiasts", "url": "https://peets.com"},
        {"name": "Blue Bottle Coffee", "category": "Artisan Coffee", "price": "high", "audience": "connoisseurs", "url": "https://bluebottlecoffee.com"},
        {"name": "Caribou Coffee", "category": "Coffeehouse Chain", "price": "medium", "audience": "midwest customers", "url": "https://cariboucoffee.com"},
        {"name": "Tim Hortons", "category": "Coffee & Baked Goods", "price": "low", "audience": "canadians", "url": "https://timhortons.com"},
    ],
    "bakery": [
        {"name": "Panera Bread", "category": "Bakery Cafe Chain", "price": "medium", "audience": "lunch crowd", "url": "https://panerabread.com"},
        {"name": "Corner Bakery", "category": "Fast Casual Bakery", "price": "medium", "audience": "urban workers", "url": "https://cornerbakery.com"},
        {"name": "Great Harvest Bread", "category": "Artisan Bakery", "price": "medium", "audience": "health conscious", "url": "https://greatharvest.com"},
        {"name": "Nothing Bundt Cakes", "category": "Specialty Bakery", "price": "medium", "audience": "celebration shoppers", "url": "https://nothingbundtcakes.com"},
        {"name": "Crumbl Cookies", "category": "Cookie Shop", "price": "medium", "audience": "young adults", "url": "https://crumblcookies.com"},
        {"name": "Paris Baguette", "category": "French Bakery", "price": "medium", "audience": "upscale customers", "url": "https://parisbaguette.com"},
    ],
    "consulting": [
        {"name": "McKinsey & Company", "category": "Top-Tier Consulting", "price": "high", "audience": "Fortune 500", "url": "https://mckinsey.com"},
        {"name": "BCG", "category": "Strategy Consulting", "price": "high", "audience": "large enterprises", "url": "https://bcg.com"},
        {"name": "Bain & Company", "category": "Management Consulting", "price": "high", "audience": "PE firms", "url": "https://bain.com"},
        {"name": "Deloitte Consulting", "category": "Big Four Consulting", "price": "high", "audience": "enterprises", "url": "https://deloitte.com"},
        {"name": "Accenture", "category": "Technology Consulting", "price": "high", "audience": "IT transformation", "url": "https://accenture.com"},
        {"name": "PwC Consulting", "category": "Advisory Services", "price": "high", "audience": "public companies", "url": "https://pwc.com"},
    ],
    "retail": [
        {"name": "Target", "category": "Department Store", "price": "medium", "audience": "families", "url": "https://target.com"},
        {"name": "Walmart", "category": "Mass Retailer", "price": "low", "audience": "budget shoppers", "url": "https://walmart.com"},
        {"name": "Nordstrom", "category": "Upscale Department Store", "price": "high", "audience": "affluent shoppers", "url": "https://nordstrom.com"},
        {"name": "Macy's", "category": "Department Store", "price": "medium", "audience": "mainstream", "url": "https://macys.com"},
        {"name": "Kohl's", "category": "Discount Department Store", "price": "low", "audience": "value seekers", "url": "https://kohls.com"},
    ],
    "restaurant": [
        {"name": "Chipotle", "category": "Fast Casual Mexican", "price": "medium", "audience": "young adults", "url": "https://chipotle.com"},
        {"name": "Chili's", "category": "Casual Dining", "price": "medium", "audience": "families", "url": "https://chilis.com"},
        {"name": "Olive Garden", "category": "Italian Chain", "price": "medium", "audience": "families", "url": "https://olivegarden.com"},
        {"name": "Cheesecake Factory", "category": "Upscale Casual", "price": "high", "audience": "diners", "url": "https://thecheesecakefactory.com"},
        {"name": "Applebee's", "category": "Neighborhood Grill", "price": "low", "audience": "locals", "url": "https://applebees.com"},
    ],
}


def normalize_category(category: str) -> str:
    """Normalize category string for matching"""
    category_lower = category.lower()
    
    # Category mappings
    mappings = {
        "gym": "fitness",
        "fitness center": "fitness",
        "health club": "fitness",
        "workout": "fitness",
        "hair salon": "salon",
        "beauty salon": "salon",
        "barber": "salon",
        "spa": "salon",
        "nail salon": "salon",
        "pizza shop": "pizza",
        "pizzeria": "pizza",
        "coffee shop": "coffee",
        "cafe": "coffee",
        "coffeehouse": "coffee",
        "bakery": "bakery",
        "pastry shop": "bakery",
        "bread": "bakery",
        "consulting": "consulting",
        "advisory": "consulting",
        "strategy": "consulting",
        "store": "retail",
        "shop": "retail",
        "boutique": "retail",
        "restaurant": "restaurant",
        "dining": "restaurant",
        "eatery": "restaurant",
    }
    
    for key, value in mappings.items():
        if key in category_lower:
            return value
    
    return category_lower


def calculate_price_match_score(user_price: str, competitor_price: str) -> float:
    """Calculate how well prices match (0.0 to 1.0)"""
    price_levels = {"low": 0, "medium": 1, "high": 2}
    
    # Normalize user price
    user_normalized = "medium"  # default
    if any(term in user_price.lower() for term in ["$", "cheap", "budget", "affordable"]):
        user_normalized = "low"
    elif any(term in user_price.lower() for term in ["premium", "luxury", "expensive", "upscale"]):
        user_normalized = "high"
    
    user_level = price_levels.get(user_normalized, 1)
    comp_level = price_levels.get(competitor_price, 1)
    
    diff = abs(user_level - comp_level)
    if diff == 0:
        return 1.0
    elif diff == 1:
        return 0.5
    else:
        return 0.2


def calculate_audience_match_score(user_audience: str, competitor_audience: str) -> float:
    """Calculate audience overlap (0.0 to 1.0)"""
    user_lower = user_audience.lower()
    comp_lower = competitor_audience.lower()
    
    # High overlap keywords
    high_overlap = ["everyone", "general", "families", "professionals", "young adults"]
    
    if comp_lower in high_overlap:
        return 0.7
    
    # Check for word matches
    user_words = set(user_lower.split())
    comp_words = set(comp_lower.split())
    
    if user_words & comp_words:
        return 0.9
    
    return 0.5


def discover_competitors(
    business_name: str,
    business_category: str,
    city: str,
    target_audience: str,
    average_price: str,
    max_results: int = 10
) -> List[CompetitorCandidate]:
    """
    Discover likely competitors based on business profile
    
    Args:
        business_name: User's business name
        business_category: Type of business
        city: Location
        target_audience: Target customer segment
        average_price: Price range
        max_results: Maximum competitors to return
    
    Returns:
        List of CompetitorCandidate objects
    """
    
    normalized_category = normalize_category(business_category)
    competitors = []
    
    # Get competitors from database for this category
    category_competitors = COMPETITOR_DATABASE.get(normalized_category, [])
    
    if not category_competitors:
        # Fallback: try to find similar categories
        for cat_key, cat_competitors in COMPETITOR_DATABASE.items():
            if cat_key in normalized_category or normalized_category in cat_key:
                category_competitors = cat_competitors
                break
    
    for comp in category_competitors:
        # Calculate confidence score based on multiple factors
        scores = []
        reasons = []
        
        # Price match
        price_score = calculate_price_match_score(average_price, comp["price"])
        scores.append(price_score * 0.4)  # 40% weight
        if price_score > 0.7:
            reasons.append(f"Similar price point ({comp['price']})")
        
        # Audience match
        audience_score = calculate_audience_match_score(target_audience, comp["audience"])
        scores.append(audience_score * 0.3)  # 30% weight
        if audience_score > 0.7:
            reasons.append(f"Targets {comp['audience']}")
        
        # Category match (always high since we filtered by category)
        scores.append(0.3)  # 30% weight
        reasons.append(f"Same industry ({comp['category']})")
        
        # Calculate final confidence
        confidence = sum(scores)
        
        # Create reason string
        reason_text = " • ".join(reasons) if reasons else "Similar business type"
        
        # Add location context
        reason_text += f" • Operating in {city} area"
        
        candidate = CompetitorCandidate(
            name=comp["name"],
            category=comp["category"],
            website_url=comp.get("url"),
            social_url=None,  # Can be enhanced with real data
            reason=reason_text,
            confidence_score=confidence
        )
        
        competitors.append(candidate)
    
    # Sort by confidence score
    competitors.sort(key=lambda x: x.confidence_score, reverse=True)
    
    # Return top N
    return competitors[:max_results]


def format_discovery_results(candidates: List[CompetitorCandidate]) -> Dict[str, Any]:
    """Format competitors for API response"""
    return {
        "success": True,
        "discovered_count": len(candidates),
        "competitors": [c.to_dict() for c in candidates],
        "message": f"Discovered {len(candidates)} potential competitors"
    }


if __name__ == "__main__":
    # Test the discovery system
    print("Testing Competitor Discovery Engine\n")
    
    test_cases = [
        {
            "business_name": "FitZone Gym",
            "business_category": "Fitness Center",
            "city": "Austin",
            "target_audience": "Young professionals",
            "average_price": "$50/month"
        },
        {
            "business_name": "Luxe Hair Studio",
            "business_category": "Hair Salon",
            "city": "Miami",
            "target_audience": "Women seeking premium care",
            "average_price": "$120 per visit"
        },
        {
            "business_name": "Joe's Pizza",
            "business_category": "Pizza Restaurant",
            "city": "New York",
            "target_audience": "Families and tourists",
            "average_price": "$15 per pizza"
        }
    ]
    
    for test in test_cases:
        print(f"Business: {test['business_name']}")
        print(f"Category: {test['business_category']}")
        print(f"Discovering competitors...\n")
        
        competitors = discover_competitors(
            test["business_name"],
            test["business_category"],
            test["city"],
            test["target_audience"],
            test["average_price"],
            max_results=5
        )
        
        for i, comp in enumerate(competitors, 1):
            print(f"{i}. {comp.name} ({comp.category})")
            print(f"   Confidence: {comp.confidence_score:.0%}")
            print(f"   Reason: {comp.reason}")
            print(f"   Website: {comp.website_url}")
            print()
        
        print("-" * 60)
        print()
