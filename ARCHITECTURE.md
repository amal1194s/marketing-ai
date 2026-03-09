# Scout Agent - System Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                     SCOUT AGENT SYSTEM                          │
│                 Competitor Intelligence Monitor                 │
└─────────────────────────────────────────────────────────────────┘

                              ▼

┌─────────────────────────────────────────────────────────────────┐
│                        INPUT SOURCES                            │
├─────────────────────────────────────────────────────────────────┤
│  • Website Content        • API Responses                       │
│  • Product Listings       • Social Media                        │
│  • Promotional Text       • Marketing Materials                 │
│  • Scraped Data          • Structured Feeds                     │
└─────────────────────────────────────────────────────────────────┘

                              ▼

┌─────────────────────────────────────────────────────────────────┐
│                      SCOUT AGENT CORE                           │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌───────────────────────────────────────────────────────┐    │
│  │         ScoutAgent (Main Controller)                  │    │
│  ├───────────────────────────────────────────────────────┤    │
│  │  • process_text()                                     │    │
│  │  • process_structured_data()                          │    │
│  │  • process_file()                                     │    │
│  │  • process_batch()                                    │    │
│  │  • export_signals()                                   │    │
│  │  • get_stats()                                        │    │
│  └───────────────────────────────────────────────────────┘    │
│                          ▼                                      │
│  ┌───────────────────────────────────────────────────────┐    │
│  │         SignalExtractor (Intelligence Engine)         │    │
│  ├───────────────────────────────────────────────────────┤    │
│  │  • Event Type Detection                               │    │
│  │  • Price Extraction                                   │    │
│  │  • Offer Detection                                    │    │
│  │  • Product Extraction                                 │    │
│  │  • Summary Generation                                 │    │
│  └───────────────────────────────────────────────────────┘    │
│                          ▼                                      │
│  ┌───────────────────────────────────────────────────────┐    │
│  │         Data Models (Schemas)                         │    │
│  ├───────────────────────────────────────────────────────┤    │
│  │  • CompetitorSignal                                   │    │
│  │  • EventType (Enum)                                   │    │
│  │  • Validation Rules                                   │    │
│  └───────────────────────────────────────────────────────┘    │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

                              ▼

┌─────────────────────────────────────────────────────────────────┐
│                    EVENT CLASSIFICATION                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │ Price Change │  │ New Product  │  │  Promotion   │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Discount   │  │   Campaign   │  │    Bundle    │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

                              ▼

┌─────────────────────────────────────────────────────────────────┐
│                    STRUCTURED OUTPUT                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  {                                                              │
│    "competitor": "Dominos",                                     │
│    "product": "Farmhouse Pizza",                                │
│    "event_type": "promotion",                                   │
│    "price": "299",                                              │
│    "offer": "Buy 1 Get 1",                                      │
│    "source": "website",                                         │
│    "summary": "Dominos launched BOGO on Pizza at ₹299."        │
│  }                                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

                              ▼

┌─────────────────────────────────────────────────────────────────┐
│                    OUTPUT DESTINATIONS                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   JSON File  │  │   Database   │  │     API      │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │  Dashboard   │  │ Alert System │  │   Reports    │         │
│  └──────────────┘  └──────────────┘  └──────────────┘         │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘

                              ▼

┌─────────────────────────────────────────────────────────────────┐
│                 DOWNSTREAM AGENTS (Future)                      │
├─────────────────────────────────────────────────────────────────┤
│  • Analyzer Agent     → Competitive analysis                    │
│  • Strategy Agent     → Strategic recommendations               │
│  • Alert Agent        → Real-time notifications                 │
│  • Dashboard Agent    → Visualization                           │
└─────────────────────────────────────────────────────────────────┘
```

---

## Data Flow Diagram

```
┌──────────────┐
│  Raw Input   │
│  (Text/JSON) │
└──────┬───────┘
       │
       ▼
┌──────────────────┐
│  SignalExtractor │
│  - Detect Event  │
│  - Extract Price │
│  - Extract Offer │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ CompetitorSignal │
│   (Dataclass)    │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│   Validation     │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│  JSON Output     │
└──────────────────┘
```

---

## Module Dependencies

```
scout_agent.py
    │
    ├─→ extractors.py
    │       │
    │       └─→ schemas.py (EventType, CompetitorSignal)
    │
    └─→ schemas.py
```

---

## Processing Pipeline

```
INPUT → EXTRACTION → CLASSIFICATION → VALIDATION → OUTPUT

┌────────┐   ┌──────────┐   ┌──────────┐   ┌──────────┐   ┌────────┐
│  Text  │──→│  Parse   │──→│ Classify │──→│ Validate │──→│  JSON  │
│  JSON  │   │  Extract │   │   Type   │   │  Schema  │   │  Dict  │
│  File  │   │  Fields  │   │  Detect  │   │  Fields  │   │  List  │
└────────┘   └──────────┘   └──────────┘   └──────────┘   └────────┘
```

---

## Feature Matrix

| Feature                  | Supported | Notes                        |
|-------------------------|-----------|------------------------------|
| Text Processing         | ✅        | Raw text input               |
| Structured Data         | ✅        | JSON/Dict input              |
| File Processing         | ✅        | .txt, .json, .md             |
| Batch Processing        | ✅        | Multiple items               |
| Event Detection         | ✅        | 6 event types                |
| Price Extraction        | ✅        | ₹, $, Rs patterns            |
| Offer Detection         | ✅        | Regex patterns               |
| Auto-Classification     | ✅        | Keyword-based                |
| Auto-Summary            | ✅        | Generated summaries          |
| Validation              | ✅        | Schema validation            |
| Export                  | ✅        | JSON export                  |
| Filtering               | ✅        | By type/competitor           |
| Statistics              | ✅        | Signal counts                |
| Configuration           | ✅        | YAML config                  |
| Testing                 | ✅        | Unit tests                   |

---

## Integration Points

```
┌─────────────────────────────────────────────────────────────┐
│                      MULTI-AGENT SYSTEM                     │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  [Data Sources] → [Scout Agent] → [Signal Storage]         │
│                                          │                  │
│                                          ├─→ [Analyzer]     │
│                                          ├─→ [Strategy]     │
│                                          ├─→ [Alerts]       │
│                                          └─→ [Dashboard]    │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Extraction Logic Flow

```
┌──────────────────────────────────────────────────────────────┐
│                   TEXT INPUT                                 │
│  "Dominos launched Buy 1 Get 1 on Pizza at ₹299"           │
└────────────────┬─────────────────────────────────────────────┘
                 │
                 ▼
        ┌────────────────────┐
        │  Parse & Tokenize  │
        └────────┬───────────┘
                 │
        ┌────────┴────────┐
        │                 │
        ▼                 ▼
┌──────────────┐   ┌──────────────┐
│ Detect Event │   │ Extract Data │
│   Keywords   │   │   Patterns   │
│              │   │              │
│ "launched"   │   │ Price: ₹299  │
│ "Buy 1..."   │   │ Offer: BOGO  │
└──────┬───────┘   └──────┬───────┘
       │                   │
       └─────────┬─────────┘
                 ▼
        ┌────────────────┐
        │   Classify     │
        │  event_type    │
        │  = promotion   │
        └────────┬───────┘
                 │
                 ▼
        ┌────────────────┐
        │ Build Signal   │
        │   Structure    │
        └────────┬───────┘
                 │
                 ▼
        ┌────────────────┐
        │   Validate     │
        └────────┬───────┘
                 │
                 ▼
        ┌────────────────┐
        │  JSON Output   │
        └────────────────┘
```

---

## Test Coverage Map

```
test_scout_agent.py
    │
    ├─→ test_process_text_basic
    ├─→ test_process_structured_data
    ├─→ test_process_batch
    ├─→ test_event_type_detection
    ├─→ test_price_extraction
    ├─→ test_get_signals_by_type
    ├─→ test_get_signals_by_competitor
    ├─→ test_get_stats
    └─→ test_clear_history
```

---

## Performance Characteristics

| Operation              | Complexity | Speed    |
|-----------------------|------------|----------|
| Text Processing       | O(n)       | Fast     |
| Structured Processing | O(1)       | Instant  |
| Batch Processing      | O(n)       | Fast     |
| Event Detection       | O(k)       | Fast     |
| Filtering             | O(n)       | Fast     |
| Export                | O(n)       | Fast     |

Where:
- n = number of items
- k = number of keywords/patterns

---

**Built:** March 9, 2026  
**Version:** 1.0.0  
**Status:** ✅ Production Ready
