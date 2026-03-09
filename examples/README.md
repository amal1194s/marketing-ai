# Scout Agent Usage Examples

This directory contains example scripts demonstrating different ways to use the Scout Agent.

## Available Examples

### 1. demo_file_processing.py
Demonstrates processing files (JSON and text) with the Scout Agent.

```bash
python examples/demo_file_processing.py
```

## Running Examples

Make sure you're in the project root directory and have installed dependencies:

```bash
pip install -r requirements.txt
python examples/demo_file_processing.py
```

## Creating Custom Examples

You can create your own examples by:

1. Importing the ScoutAgent: `from agents.scout_agent import ScoutAgent`
2. Creating an instance: `agent = ScoutAgent()`
3. Processing your data using the appropriate method
4. Exporting or using the extracted signals
