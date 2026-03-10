"""
Category Adapter - Makes agent output category-agnostic
Adapts food-specific agent language to any business category
"""

import re
from typing import Dict, Any


# Category-specific terminology mappings
CATEGORY_TERMS = {
    "pizza": {
        "generic_product": "pizzas",
        "generic_offer": "deals",
        "generic_service": "delivery",
        "generic_location": "restaurant",
    },
    "coffee": {
        "generic_product": "drinks",
        "generic_offer": "promotions",
        "generic_service": "cafe experience",
        "generic_location": "cafe",
    },
    "gym": {
        "generic_product": "memberships",
        "generic_offer": "packages",
        "generic_service": "training",
        "generic_location": "facility",
    },
    "salon": {
        "generic_product": "services",
        "generic_offer": "specials",
        "generic_service": "treatments",
        "generic_location": "salon",
    },
    "bakery": {
        "generic_product": "baked goods",
        "generic_offer": "daily specials",
        "generic_service": "custom orders",
        "generic_location": "bakery",
    },
    "consulting": {
        "generic_product": "services",
        "generic_offer": "packages",
        "generic_service": "consulting",
        "generic_location": "firm",
    },
    "retail": {
        "generic_product": "products",
        "generic_offer": "sales",
        "generic_service": "shopping experience",
        "generic_location": "store",
    },
}


def get_category_terms(category: str) -> Dict[str, str]:
    """Get category-specific terminology or default to generic terms"""
    category_lower = category.lower()
    
    # Check for exact or partial matches
    for key in CATEGORY_TERMS:
        if key in category_lower or category_lower in key:
            return CATEGORY_TERMS[key]
    
    # Default generic terms for unknown categories
    return {
        "generic_product": "products",
        "generic_offer": "offers",
        "generic_service": "services",
        "generic_location": "business",
    }


def adapt_text_to_category(text: str, category: str) -> str:
    """
    Replace generic business terms with category-specific language
    
    Args:
        text: Original text from agent
        category: Business category (e.g., "pizza", "gym", "salon")
    
    Returns:
        Adapted text with category-appropriate terminology
    """
    if not text or not category:
        return text
    
    terms = get_category_terms(category)
    adapted = text
    
    # Replace compound terms with possessive handling
    # Pattern: capture possessive suffix separately
    adapted = re.sub(
        r'\b(pizza\s+shop|coffee\s+shop|restaurant)(\'s)?\b',
        lambda m: terms['generic_location'] + (m.group(2) if m.group(2) else ''),
        adapted,
        flags=re.IGNORECASE
    )
    
    # Replace individual food terms
    adapted = re.sub(r'\b(pizza|pizzas)\b', terms['generic_product'], adapted, flags=re.IGNORECASE)
    adapted = re.sub(r'\b(coffee|coffees?|drinks?)\b', terms['generic_product'], adapted, flags=re.IGNORECASE)
    adapted = re.sub(r'\b(menu items?|food items?)\b', terms['generic_product'], adapted, flags=re.IGNORECASE)
    
    # Replace location terms (but not if already replaced above)
    adapted = re.sub(r'\b(restaurants?|cafes?)\b', terms['generic_location'], adapted, flags=re.IGNORECASE)
    
    # Replace service terms
    adapted = re.sub(r'\b(dine-?in|dining)\b', terms['generic_service'], adapted, flags=re.IGNORECASE)
    adapted = re.sub(r'\b(delivery|takeout)\b', terms['generic_service'], adapted, flags=re.IGNORECASE)
    
    return adapted


def adapt_analysis_result(analysis: Dict[str, Any], business_profile: Dict[str, Any]) -> Dict[str, Any]:
    """
    Adapt the entire analysis result to match business category
    
    Args:
        analysis: Analysis result dictionary
        business_profile: Business profile with category information
    
    Returns:
        Adapted analysis result
    """
    category = business_profile.get('category', 'business')
    adapted = analysis.copy()
    
    # Adapt text fields
    text_fields = ['summary', 'pricing_gap', 'market_risk']
    for field in text_fields:
        if field in adapted and adapted[field]:
            adapted[field] = adapt_text_to_category(adapted[field], category)
    
    # Adapt key insights
    if 'key_insights' in adapted and isinstance(adapted['key_insights'], list):
        adapted['key_insights'] = [
            adapt_text_to_category(insight, category)
            for insight in adapted['key_insights']
        ]
    
    # Adapt competitor breakdown
    if 'competitor_breakdown' in adapted and isinstance(adapted['competitor_breakdown'], list):
        for comp in adapted['competitor_breakdown']:
            if isinstance(comp, dict):
                for key in ['threat_analysis', 'key_factors']:
                    if key in comp and comp[key]:
                        if isinstance(comp[key], str):
                            comp[key] = adapt_text_to_category(comp[key], category)
                        elif isinstance(comp[key], list):
                            comp[key] = [
                                adapt_text_to_category(item, category) if isinstance(item, str) else item
                                for item in comp[key]
                            ]
    
    return adapted


def format_category_message(category: str, message_type: str = "pricing") -> str:
    """
    Generate category-appropriate messages
    
    Args:
        category: Business category
        message_type: Type of message (pricing, offer, product, audience)
    
    Returns:
        Formatted message string
    """
    terms = get_category_terms(category)
    
    messages = {
        "pricing": f"Your {category} pricing is competitive for {terms['generic_product']}.",
        "offer": f"Consider promoting {terms['generic_offer']} to attract customers.",
        "product": f"Your {terms['generic_product']} differentiate you from competitors.",
        "audience": f"Your {terms['generic_location']} targets the right customer segment.",
    }
    
    return messages.get(message_type, "Your business positioning is strong.")


def get_category_icon(category: str) -> str:
    """Get emoji icon for category"""
    category_lower = category.lower()
    
    icons = {
        "pizza": "🍕",
        "coffee": "☕",
        "gym": "💪",
        "salon": "💇",
        "bakery": "🥐",
        "consulting": "💼",
        "retail": "🛍️",
        "restaurant": "🍽️",
        "food": "🍴",
        "health": "🏥",
        "fitness": "🏋️",
        "beauty": "💄",
        "tech": "💻",
        "education": "📚",
    }
    
    for key, icon in icons.items():
        if key in category_lower:
            return icon
    
    return "🏢"  # Default business icon


if __name__ == "__main__":
    # Test the adapter
    test_text = "Your pizza shop's pricing is 15% higher than competing restaurants. Consider offering delivery specials."
    
    print("Original (Food):")
    print(test_text)
    print()
    
    print("Adapted to Gym:")
    print(adapt_text_to_category(test_text, "gym"))
    print()
    
    print("Adapted to Salon:")
    print(adapt_text_to_category(test_text, "salon"))
    print()
    
    print("Adapted to Consulting:")
    print(adapt_text_to_category(test_text, "consulting"))
