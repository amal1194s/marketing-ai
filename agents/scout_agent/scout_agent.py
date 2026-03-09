"""
Scout Agent - Main Module
Monitors competitor sources and extracts business intelligence signals.
"""

import json
from typing import List, Dict, Any, Union
from pathlib import Path

from .schemas import CompetitorSignal
from .extractors import SignalExtractor


class ScoutAgent:
    """
    Scout Agent for monitoring competitor intelligence.
    
    Responsibilities:
    - Monitor competitor sources (websites, feeds, data)
    - Extract important business signals
    - Structure information as JSON
    - Detect competitor events (price changes, launches, promotions, etc.)
    
    This agent does NOT analyze or suggest strategies.
    It only collects and structures competitor information.
    """
    
    def __init__(self, config: Dict[str, Any] = None):
        """
        Initialize Scout Agent.
        
        Args:
            config: Optional configuration dictionary
        """
        self.config = config or {}
        self.extractor = SignalExtractor()
        self.signals_history = []
        
    def process_text(self, text: str, competitor: str, source: str = "text") -> List[Dict[str, Any]]:
        """
        Process raw text and extract competitor signals.
        
        Args:
            text: Raw text content from competitor source
            competitor: Name of the competitor
            source: Source identifier (website, scraper, etc.)
            
        Returns:
            List of competitor signals as dictionaries
        """
        signals = self.extractor.extract_from_text(text, competitor, source)
        self.signals_history.extend(signals)
        return [signal.to_dict() for signal in signals]
    
    def process_structured_data(self, data: Union[Dict, List], source: str = "api") -> List[Dict[str, Any]]:
        """
        Process structured data (JSON/dict) and extract competitor signals.
        
        Args:
            data: Structured data (dictionary or list of dictionaries)
            source: Source identifier
            
        Returns:
            List of competitor signals as dictionaries
        """
        signals = self.extractor.extract_from_structured_data(data, source)
        self.signals_history.extend(signals)
        return [signal.to_dict() for signal in signals]
    
    def process_file(self, file_path: str) -> List[Dict[str, Any]]:
        """
        Process a file and extract competitor signals.
        Supports .txt, .json files.
        
        Args:
            file_path: Path to the file
            
        Returns:
            List of competitor signals as dictionaries
        """
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        if path.suffix == '.json':
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return self.process_structured_data(data, source=f"file:{path.name}")
        
        elif path.suffix in ['.txt', '.md']:
            with open(path, 'r', encoding='utf-8') as f:
                text = f.read()
                # Try to extract competitor name from filename or content
                competitor = path.stem.replace('_', ' ').title()
                return self.process_text(text, competitor, source=f"file:{path.name}")
        
        else:
            raise ValueError(f"Unsupported file type: {path.suffix}")
    
    def process_batch(self, items: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Process multiple items in batch.
        
        Args:
            items: List of items, each with 'type', 'data', and optional 'source'
                  Example: [
                      {'type': 'text', 'data': '...', 'competitor': 'X', 'source': 'web'},
                      {'type': 'structured', 'data': {...}, 'source': 'api'}
                  ]
        
        Returns:
            List of all extracted signals
        """
        all_signals = []
        
        for item in items:
            item_type = item.get('type')
            data = item.get('data')
            source = item.get('source', 'batch')
            
            if item_type == 'text':
                competitor = item.get('competitor', 'Unknown')
                signals = self.process_text(data, competitor, source)
                all_signals.extend(signals)
            
            elif item_type == 'structured':
                signals = self.process_structured_data(data, source)
                all_signals.extend(signals)
        
        return all_signals
    
    def export_signals(self, output_path: str, signals: List[Dict[str, Any]] = None):
        """
        Export signals to a JSON file.
        
        Args:
            output_path: Path to output file
            signals: Signals to export (if None, exports all from history)
        """
        signals_to_export = signals or [s.to_dict() for s in self.signals_history]
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(signals_to_export, f, indent=2, ensure_ascii=False)
    
    def get_signals_by_type(self, event_type: str) -> List[Dict[str, Any]]:
        """
        Filter signals by event type.
        
        Args:
            event_type: Event type to filter by
            
        Returns:
            List of signals matching the event type
        """
        return [
            signal.to_dict() 
            for signal in self.signals_history 
            if signal.event_type == event_type
        ]
    
    def get_signals_by_competitor(self, competitor: str) -> List[Dict[str, Any]]:
        """
        Filter signals by competitor name.
        
        Args:
            competitor: Competitor name
            
        Returns:
            List of signals from the specified competitor
        """
        return [
            signal.to_dict() 
            for signal in self.signals_history 
            if signal.competitor.lower() == competitor.lower()
        ]
    
    def clear_history(self):
        """Clear the signals history"""
        self.signals_history.clear()
    
    def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about collected signals.
        
        Returns:
            Dictionary with signal statistics
        """
        total = len(self.signals_history)
        
        if total == 0:
            return {"total_signals": 0}
        
        # Count by event type
        event_counts = {}
        competitor_counts = {}
        
        for signal in self.signals_history:
            event_counts[signal.event_type] = event_counts.get(signal.event_type, 0) + 1
            competitor_counts[signal.competitor] = competitor_counts.get(signal.competitor, 0) + 1
        
        return {
            "total_signals": total,
            "by_event_type": event_counts,
            "by_competitor": competitor_counts,
            "unique_competitors": len(competitor_counts)
        }
