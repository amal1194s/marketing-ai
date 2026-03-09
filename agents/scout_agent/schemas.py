"""
Data schemas for Scout Agent
Defines the structure of competitor signals and event types.
"""

from enum import Enum
from typing import Optional
from dataclasses import dataclass, asdict
import json


class EventType(Enum):
    """Types of competitor events that can be detected"""
    PRICE_CHANGE = "price_change"
    NEW_PRODUCT = "new_product"
    PROMOTION = "promotion"
    DISCOUNT = "discount"
    MARKETING_CAMPAIGN = "marketing_campaign"
    BUNDLE_OFFER = "bundle_offer"


@dataclass
class CompetitorSignal:
    """
    Structured representation of a competitor intelligence signal.
    
    Attributes:
        competitor: Name of the competitor business
        product: Product or service mentioned
        event_type: Type of event detected
        price: Detected price if available
        offer: Promotion or discount details
        source: Where the information was detected
        summary: Short 1-sentence description of the event
    """
    competitor: str
    product: str
    event_type: str
    price: str
    offer: str
    source: str
    summary: str
    
    def to_dict(self) -> dict:
        """Convert signal to dictionary"""
        return asdict(self)
    
    def to_json(self) -> str:
        """Convert signal to JSON string"""
        return json.dumps(self.to_dict(), indent=2)
    
    @classmethod
    def from_dict(cls, data: dict) -> 'CompetitorSignal':
        """Create signal from dictionary"""
        return cls(**data)
    
    def validate(self) -> bool:
        """Validate that the signal has required fields"""
        if not self.competitor:
            return False
        if self.event_type not in [e.value for e in EventType]:
            return False
        return True
