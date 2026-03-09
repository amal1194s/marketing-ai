"""
Unit tests for Scout Agent
Tests the core functionality of competitor signal extraction.
"""

import unittest
import json
from agents.scout_agent import ScoutAgent
from agents.scout_agent.schemas import EventType


class TestScoutAgent(unittest.TestCase):
    """Test cases for Scout Agent"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.agent = ScoutAgent()
    
    def tearDown(self):
        """Clean up after tests"""
        self.agent.clear_history()
    
    def test_process_text_basic(self):
        """Test basic text processing"""
        text = "Dominos launched Buy 1 Get 1 offer on Pizza at ₹299"
        signals = self.agent.process_text(text, "Dominos", "test")
        
        self.assertEqual(len(signals), 1)
        self.assertEqual(signals[0]['competitor'], 'Dominos')
        self.assertIn('event_type', signals[0])
    
    def test_process_structured_data(self):
        """Test structured data processing"""
        data = {
            "competitor": "Pizza Hut",
            "product": "Margherita",
            "event_type": "promotion",
            "price": "199",
            "offer": "30% off",
            "summary": "Pizza Hut offers 30% off on Margherita"
        }
        
        signals = self.agent.process_structured_data(data, "test")
        
        self.assertEqual(len(signals), 1)
        self.assertEqual(signals[0]['competitor'], 'Pizza Hut')
        self.assertEqual(signals[0]['product'], 'Margherita')
        self.assertEqual(signals[0]['price'], '199')
    
    def test_process_batch(self):
        """Test batch processing"""
        batch = [
            {
                "type": "text",
                "data": "McDonald's new burger at ₹99",
                "competitor": "McDonald's",
                "source": "web"
            },
            {
                "type": "structured",
                "data": {
                    "competitor": "KFC",
                    "product": "Chicken Bucket",
                    "event_type": "discount",
                    "price": "399",
                    "offer": "20% off"
                },
                "source": "api"
            }
        ]
        
        signals = self.agent.process_batch(batch)
        
        self.assertEqual(len(signals), 2)
        self.assertTrue(any(s['competitor'] == 'McDonald\'s' for s in signals))
        self.assertTrue(any(s['competitor'] == 'KFC' for s in signals))
    
    def test_event_type_detection(self):
        """Test event type detection"""
        test_cases = [
            ("New product launched", "new_product"),
            ("Special discount offer", "discount"),
            ("Buy 1 Get 1 promotion", "promotion"),
            ("Price reduced from ₹500 to ₹400", "price_change"),
        ]
        
        for text, expected_type in test_cases:
            signals = self.agent.process_text(text, "TestCompany", "test")
            if signals:
                self.assertIn(expected_type, signals[0]['event_type'].lower())
    
    def test_price_extraction(self):
        """Test price extraction from text"""
        text = "Special offer: Pizza at ₹299 only!"
        signals = self.agent.process_text(text, "TestPizza", "test")
        
        if signals:
            self.assertIn('299', signals[0]['price'])
    
    def test_get_signals_by_type(self):
        """Test filtering signals by event type"""
        data1 = {
            "competitor": "A",
            "product": "Product1",
            "event_type": "promotion",
            "price": "100",
            "offer": "Special",
            "summary": "Test"
        }
        
        data2 = {
            "competitor": "B",
            "product": "Product2",
            "event_type": "discount",
            "price": "200",
            "offer": "Sale",
            "summary": "Test"
        }
        
        self.agent.process_structured_data(data1)
        self.agent.process_structured_data(data2)
        
        promo_signals = self.agent.get_signals_by_type("promotion")
        self.assertEqual(len(promo_signals), 1)
        self.assertEqual(promo_signals[0]['competitor'], 'A')
    
    def test_get_signals_by_competitor(self):
        """Test filtering signals by competitor"""
        data1 = {"competitor": "CompanyA", "product": "P1", "event_type": "promotion", 
                "price": "100", "offer": "", "summary": "Test"}
        data2 = {"competitor": "CompanyB", "product": "P2", "event_type": "discount", 
                "price": "200", "offer": "", "summary": "Test"}
        
        self.agent.process_structured_data(data1)
        self.agent.process_structured_data(data2)
        
        signals = self.agent.get_signals_by_competitor("CompanyA")
        self.assertEqual(len(signals), 1)
        self.assertEqual(signals[0]['product'], 'P1')
    
    def test_get_stats(self):
        """Test statistics generation"""
        data = {"competitor": "Test", "product": "P1", "event_type": "promotion", 
               "price": "100", "offer": "", "summary": "Test"}
        
        self.agent.process_structured_data(data)
        stats = self.agent.get_stats()
        
        self.assertEqual(stats['total_signals'], 1)
        self.assertEqual(stats['unique_competitors'], 1)
        self.assertIn('by_event_type', stats)
    
    def test_clear_history(self):
        """Test clearing signal history"""
        data = {"competitor": "Test", "product": "P1", "event_type": "promotion", 
               "price": "100", "offer": "", "summary": "Test"}
        
        self.agent.process_structured_data(data)
        self.assertEqual(len(self.agent.signals_history), 1)
        
        self.agent.clear_history()
        self.assertEqual(len(self.agent.signals_history), 0)


if __name__ == '__main__':
    unittest.main()
