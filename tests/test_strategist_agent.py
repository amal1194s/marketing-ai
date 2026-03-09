"""
Unit tests for Strategist Agent
"""

import json
import os
import sys
import tempfile
import unittest

# allow importing from repository root
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents import strategist_agent


class TestStrategistAgent(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.mkdtemp()
        self.input_path = os.path.join(self.tempdir, "market_analysis.json")
        self.output_path = os.path.join(self.tempdir, "marketing_strategy.json")

        self.example = [
            {
                "competitor": "Dominos",
                "event_type": "promotion",
                "competitor_price": 299,
                "user_price": 350,
                "price_difference": -51,
                "impact_level": "high",
            },
            {
                "competitor": "LocalShop",
                "event_type": "other",
                "impact_level": "low",
            },
        ]
        with open(self.input_path, "w", encoding="utf-8") as f:
            json.dump(self.example, f)

    def tearDown(self):
        import shutil
        shutil.rmtree(self.tempdir)

    def test_generate_strategy(self):
        insights = strategist_agent.load_json(self.input_path)
        strategies = strategist_agent.generate_strategy(insights)
        self.assertEqual(len(strategies), 2)
        # first should be pricing strategy because price_diff negative
        self.assertEqual(strategies[0]['strategy_type'], 'pricing_strategy')
        # second is generic marketing_strategy
        self.assertEqual(strategies[1]['strategy_type'], 'marketing_strategy')

    def test_save_and_load(self):
        strat = strategist_agent.generate_strategy(self.example)
        strategist_agent.save_json(strat, self.output_path)
        with open(self.output_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        self.assertEqual(data, strat)


if __name__ == '__main__':
    unittest.main()
