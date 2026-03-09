"""
Extraction logic for Scout Agent
Contains methods to extract competitor signals from various data sources.
"""

import re
from typing import List, Dict, Any, Optional
from .schemas import CompetitorSignal, EventType


class SignalExtractor:
    """Extracts competitor signals from raw data sources"""
    
    # Keywords for event type detection
    EVENT_KEYWORDS = {
        EventType.PRICE_CHANGE: ['price change', 'price update', 'new price', 'repriced'],
        EventType.NEW_PRODUCT: ['new product', 'launched', 'introducing', 'now available', 'just released'],
        EventType.PROMOTION: ['promotion', 'promo', 'special offer', 'promotional'],
        EventType.DISCOUNT: ['discount', 'off', 'sale', 'save', 'reduced'],
        EventType.MARKETING_CAMPAIGN: ['campaign', 'marketing', 'advertisement', 'announcing'],
        EventType.BUNDLE_OFFER: ['bundle', 'combo', 'package', 'together', 'buy with']
    }
    
    # Price patterns
    PRICE_PATTERNS = [
        r'₹\s*(\d+(?:,\d+)*(?:\.\d+)?)',  # Indian Rupee
        r'\$\s*(\d+(?:,\d+)*(?:\.\d+)?)',  # Dollar
        r'(?:Rs\.?|INR)\s*(\d+(?:,\d+)*(?:\.\d+)?)',  # Rs or INR
        r'(?:price|priced at|for|costs?)\s*[:\-]?\s*₹?\$?\s*(\d+(?:,\d+)*(?:\.\d+)?)',  # Generic price
    ]
    
    # Offer patterns
    OFFER_PATTERNS = [
        r'buy\s+\d+\s+get\s+\d+(?:\s+free)?',
        r'\d+%\s+off',
        r'flat\s+\d+%?\s+off',
        r'up\s+to\s+\d+%\s+off',
        r'limited\s+time\s+offer',
        r'flash\s+sale',
        r'clearance\s+sale'
    ]
    
    def __init__(self):
        self.signals = []
    
    def extract_from_text(self, text: str, competitor: str, source: str = "text") -> List[CompetitorSignal]:
        """
        Extract competitor signals from raw text.
        
        Args:
            text: Raw text content to analyze
            competitor: Name of the competitor
            source: Source of the information
            
        Returns:
            List of extracted CompetitorSignal objects
        """
        signals = []
        text_lower = text.lower()
        
        # Detect event type
        event_type = self._detect_event_type(text_lower)
        
        # Extract price
        price = self._extract_price(text)
        
        # Extract offer
        offer = self._extract_offer(text_lower)
        
        # Extract product name (basic extraction)
        product = self._extract_product(text)
        
        # Generate summary
        summary = self._generate_summary(text)
        
        # Create signal
        signal = CompetitorSignal(
            competitor=competitor,
            product=product,
            event_type=event_type,
            price=price,
            offer=offer,
            source=source,
            summary=summary
        )
        
        if signal.validate():
            signals.append(signal)
        
        return signals
    
    def extract_from_structured_data(self, data: Dict[str, Any], source: str = "api") -> List[CompetitorSignal]:
        """
        Extract competitor signals from structured data (dict/JSON).
        
        Args:
            data: Structured data dictionary
            source: Source of the information
            
        Returns:
            List of extracted CompetitorSignal objects
        """
        signals = []
        
        # Handle list of items
        if isinstance(data, list):
            for item in data:
                signals.extend(self.extract_from_structured_data(item, source))
            return signals
        
        # Extract fields from structured data
        competitor = data.get('competitor', data.get('company', data.get('brand', '')))
        product = data.get('product', data.get('item', data.get('name', '')))
        event_type = data.get('event_type', data.get('type', ''))
        price = str(data.get('price', ''))
        offer = data.get('offer', data.get('promotion', data.get('deal', '')))
        summary = data.get('summary', data.get('description', ''))
        
        # Auto-detect event type if not provided
        if not event_type:
            combined_text = f"{product} {offer} {summary}".lower()
            event_type = self._detect_event_type(combined_text)
        
        # Auto-generate summary if not provided
        if not summary:
            summary = self._generate_summary_from_fields(competitor, product, event_type, price, offer)
        
        signal = CompetitorSignal(
            competitor=competitor,
            product=product,
            event_type=event_type,
            price=price,
            offer=offer,
            source=source,
            summary=summary
        )
        
        if signal.validate():
            signals.append(signal)
        
        return signals
    
    def _detect_event_type(self, text: str) -> str:
        """Detect event type from text using keywords"""
        for event_type, keywords in self.EVENT_KEYWORDS.items():
            for keyword in keywords:
                if keyword in text:
                    return event_type.value
        return EventType.MARKETING_CAMPAIGN.value  # Default
    
    def _extract_price(self, text: str) -> str:
        """Extract price from text"""
        for pattern in self.PRICE_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1) if match.lastindex else match.group(0)
        return ""
    
    def _extract_offer(self, text: str) -> str:
        """Extract offer details from text"""
        for pattern in self.OFFER_PATTERNS:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(0)
        return ""
    
    def _extract_product(self, text: str) -> str:
        """
        Extract product name from text.
        This is a basic implementation that looks for capitalized phrases.
        """
        # Look for capitalized words (likely product names)
        # This is a simplified approach
        words = text.split()
        product_candidates = []
        
        for i, word in enumerate(words):
            if word and word[0].isupper() and len(word) > 2:
                # Get 1-3 words that might be product name
                candidate = ' '.join(words[i:min(i+3, len(words))])
                if len(candidate) < 50:  # Reasonable product name length
                    product_candidates.append(candidate)
        
        return product_candidates[0] if product_candidates else ""
    
    def _generate_summary(self, text: str) -> str:
        """Generate a concise summary from text"""
        # Take first sentence or first 150 characters
        sentences = text.split('.')
        if sentences:
            summary = sentences[0].strip()
            if len(summary) > 150:
                summary = summary[:147] + "..."
            return summary
        return text[:150]
    
    def _generate_summary_from_fields(self, competitor: str, product: str, 
                                     event_type: str, price: str, offer: str) -> str:
        """Generate summary from structured fields"""
        parts = [competitor]
        
        if event_type == EventType.NEW_PRODUCT.value:
            parts.append("launched")
        elif event_type == EventType.PROMOTION.value:
            parts.append("is offering")
        elif event_type == EventType.DISCOUNT.value:
            parts.append("announced discount on")
        elif event_type == EventType.PRICE_CHANGE.value:
            parts.append("changed price for")
        
        if product:
            parts.append(product)
        
        if price:
            parts.append(f"at ₹{price}")
        
        if offer:
            parts.append(f"with {offer}")
        
        return " ".join(parts) + "."
