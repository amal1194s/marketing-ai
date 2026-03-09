"""
Scout Agent Module
A multi-agent market intelligence system component for monitoring competitor sources.
"""

from .scout_agent import ScoutAgent
from .schemas import CompetitorSignal, EventType

__all__ = ['ScoutAgent', 'CompetitorSignal', 'EventType']
__version__ = '1.0.0'
