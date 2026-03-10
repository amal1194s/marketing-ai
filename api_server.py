"""
FastAPI Backend Server for RivalSense AI
Market Intelligence API - War Room Pipeline

Endpoints:
- GET  /health          - Health check
- POST /run-war-room    - Execute complete Scout → Analyst → Strategist pipeline
- POST /analyze         - Run Analyst only
- POST /strategy        - Run Strategist only
- POST /profile         - Save business profile
- GET  /profile         - Get business profile
- POST /competitors     - Save competitors
- GET  /competitors     - Get competitors
"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict, List, Any, Optional
import json
import os
from datetime import datetime

# Import our agents
from agent_b_analyst import AgentBAnalyst
from agent_c_strategist import AgentCStrategist

# Import category adapter
try:
    from utils.category_adapter import adapt_analysis_result
    from utils.competitor_discovery import discover_competitors, format_discovery_results
except ImportError:
    # Fallback if utils not in path
    import sys
    sys.path.append(os.path.dirname(__file__))
    from utils.category_adapter import adapt_analysis_result
    from utils.competitor_discovery import discover_competitors, format_discovery_results


# Initialize FastAPI app
app = FastAPI(
    title="RivalSense AI API",
    description="Market Intelligence Backend",
    version="1.0.0"
)

# Configure CORS for Next.js frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Request/Response Models
class WarRoomRequest(BaseModel):
    """Request body for War Room execution"""
    business_profile_path: Optional[str] = "example_business_profile.json"
    scout_findings_path: Optional[str] = "example_competitor_findings.json"


class AnalyzeRequest(BaseModel):
    """Request body for Analyst execution"""
    business_profile: Dict[str, Any]
    scout_findings: Dict[str, Any]


class StrategyRequest(BaseModel):
    """Request body for Strategist execution"""
    business_profile: Dict[str, Any]
    scout_findings: Dict[str, Any]
    analyst_output: Dict[str, Any]


class ProfileRequest(BaseModel):
    """Request body for saving business profile"""
    name: str
    category: str
    city: str
    targetAudience: str
    averagePrice: str
    currentOffers: str
    usp: str


class CompetitorRequest(BaseModel):
    """Request body for saving competitors"""
    competitors: List[Dict[str, Any]]


class DiscoverCompetitorsRequest(BaseModel):
    """Request body for competitor discovery"""
    business_name: str
    business_category: str
    city: str
    target_audience: str
    average_price: str
    max_results: Optional[int] = 10


# Storage paths
PROFILES_DIR = "data/profiles"
os.makedirs(PROFILES_DIR, exist_ok=True)

PROFILE_FILE = os.path.join(PROFILES_DIR, "current_profile.json")
COMPETITORS_FILE = os.path.join(PROFILES_DIR, "current_competitors.json")


# Initialize agents
analyst = AgentBAnalyst()
strategist = AgentCStrategist()


# ============================================================================
# ENDPOINTS
# ============================================================================

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "service": "RivalSense AI API",
        "timestamp": datetime.now().isoformat(),
        "agents": {
            "analyst": "Agent B - Analyst",
            "strategist": "Agent C - Strategist"
        }
    }


@app.post("/profile")
async def save_profile(request: ProfileRequest):
    """Save business profile"""
    try:
        profile_data = {
            "name": request.name,
            "category": request.category,
            "city": request.city,
            "target_audience": request.targetAudience,
            "pricing": {
                "average_price": float(request.averagePrice.replace('$', '').replace(',', '')) if request.averagePrice else 0,
                "range": request.averagePrice
            },
            "location": {
                "city": request.city
            },
            "positioning": request.usp,
            "current_offers": request.currentOffers
        }
        
        with open(PROFILE_FILE, 'w') as f:
            json.dump(profile_data, f, indent=2)
        
        return {
            "success": True,
            "message": "Profile saved successfully",
            "profile": profile_data
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save profile: {str(e)}")


@app.get("/profile")
async def get_profile():
    """Get current business profile"""
    try:
        if not os.path.exists(PROFILE_FILE):
            raise HTTPException(status_code=404, detail="No profile found. Please complete onboarding.")
        
        with open(PROFILE_FILE, 'r') as f:
            profile = json.load(f)
        
        return {
            "success": True,
            "profile": profile
        }
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="Profile not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to load profile: {str(e)}")


@app.post("/competitors")
async def save_competitors(request: CompetitorRequest):
    """Save competitors list"""
    try:
        competitors_data = {
            "competitors": request.competitors,
            "updated_at": datetime.now().isoformat()
        }
        
        with open(COMPETITORS_FILE, 'w') as f:
            json.dump(competitors_data, f, indent=2)
        
        return {
            "success": True,
            "message": "Competitors saved successfully",
            "count": len(request.competitors)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save competitors: {str(e)}")


@app.get("/competitors")
async def get_competitors():
    """Get saved competitors"""
    try:
        if not os.path.exists(COMPETITORS_FILE):
            return {
                "success": True,
                "competitors": [],
                "message": "No competitors saved yet"
            }
        
        with open(COMPETITORS_FILE, 'r') as f:
            data = json.load(f)
        
        return {
            "success": True,
            "competitors": data.get("competitors", []),
            "updated_at": data.get("updated_at")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to load competitors: {str(e)}")


@app.post("/run-war-room")
async def run_war_room(request: WarRoomRequest = None):
    """
    Execute complete War Room pipeline:
    Scout → Analyst → Strategist
    
    Returns complete market intelligence analysis with strategy recommendations
    Uses saved business profile and competitors from onboarding
    """
    try:
        # Load saved business profile
        if not os.path.exists(PROFILE_FILE):
            raise HTTPException(
                status_code=404,
                detail="Business profile not found. Please complete onboarding first."
            )
        
        with open(PROFILE_FILE, 'r') as f:
            business_profile = json.load(f)
        
        # Load saved competitors
        if not os.path.exists(COMPETITORS_FILE):
            raise HTTPException(
                status_code=404,
                detail="Competitors not found. Please discover and select competitors first."
            )
        
        with open(COMPETITORS_FILE, 'r') as f:
            competitors_data = json.load(f)
            saved_competitors = competitors_data.get("competitors", [])
        
        if not saved_competitors:
            raise HTTPException(
                status_code=400,
                detail="No competitors selected. Please discover and select competitors first."
            )
        
        # Step 1: Create Scout Findings from saved competitors
        # In a real system, Scout would actually scrape/monitor these competitors
        # For now, we structure the saved competitor data for the Analyst
        scout_findings = {
            "timestamp": datetime.now().isoformat(),
            "business_name": business_profile.get("name", "Your Business"),
            "competitors_found": len(saved_competitors),
            "competitors": []
        }
        
        # Transform competitor data for analysis
        for comp in saved_competitors:
            scout_competitor = {
                "name": comp.get("name", "Unknown"),
                "website": comp.get("website", ""),
                "location": comp.get("location", business_profile.get("city", "")),
                "category": comp.get("category", business_profile.get("category", "")),
                "pricing": comp.get("pricing", {}),
                "target_audience": comp.get("target_audience", ""),
                "promotions": comp.get("promotions", []),
                "strengths": comp.get("strengths", []),
                "signals": []
            }
            
            # Add pricing signal if available
            if comp.get("pricing"):
                scout_competitor["signals"].append({
                    "type": "pricing_info",
                    "data": comp.get("pricing"),
                    "detected_at": datetime.now().isoformat()
                })
            
            # Add promotion signals
            if comp.get("promotion"):
                scout_competitor["signals"].append({
                    "type": "promotion",
                    "title": comp.get("promotion", ""),
                    "detected_at": datetime.now().isoformat()
                })
            
            scout_findings["competitors"].append(scout_competitor)
        
        # Step 2: Run Analyst (Agent B)
        analyst_json = analyst.analyze(business_profile, scout_findings)
        analyst_output = json.loads(analyst_json)
        
        # Adapt analyst output to business category
        analyst_output = adapt_analysis_result(analyst_output, business_profile)
        
        # Step 3: Run Strategist (Agent C)
        strategy_json = strategist.strategize(
            business_profile,
            scout_findings,
            analyst_output
        )
        strategy_output = json.loads(strategy_json)
        
        # Build comprehensive response
        response = {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "business": {
                "name": business_profile.get("name", "Unknown"),
                "category": business_profile.get("category", ""),
                "pricing": business_profile.get("pricing", {}),
                "positioning": business_profile.get("positioning", "")
            },
            "scout": {
                "competitors_found": len(scout_findings.get("competitors", [])),
                "competitors": scout_findings.get("competitors", [])
            },
            "analyst": analyst_output,
            "strategist": strategy_output,
            "pipeline_status": {
                "scout": "completed",
                "analyst": "completed",
                "strategist": "completed"
            }
        }
        
        return response
        
    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except json.JSONDecodeError as e:
        raise HTTPException(status_code=400, detail=f"Invalid JSON: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Pipeline error: {str(e)}")


@app.post("/analyze")
async def analyze(request: AnalyzeRequest):
    """
    Run Analyst (Agent B) only
    
    Analyzes competitor impact and generates threat assessment
    """
    try:
        # Run analyst
        analyst_json = analyst.analyze(
            request.business_profile,
            request.scout_findings
        )
        analyst_output = json.loads(analyst_json)
        
        # Adapt to business category
        analyst_output = adapt_analysis_result(analyst_output, request.business_profile)
        
        return {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "analysis": analyst_output
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Analysis error: {str(e)}")


@app.post("/strategy")
async def generate_strategy(request: StrategyRequest):
    """
    Run Strategist (Agent C) only
    
    Generates strategic recommendations based on analyst output
    """
    try:
        # Run strategist
        strategy_json = strategist.strategize(
            request.business_profile,
            request.scout_findings,
            request.analyst_output
        )
        strategy_output = json.loads(strategy_json)
        
        return {
            "success": True,
            "timestamp": datetime.now().isoformat(),
            "strategy": strategy_output
        }
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Strategy generation error: {str(e)}")


@app.post("/discover-competitors")
async def discover_competitors_endpoint(request: DiscoverCompetitorsRequest):
    """
    Discover likely competitors based on business profile
    
    Uses category, location, price, and audience to find matching competitors
    """
    try:
        # Run competitor discovery
        competitors = discover_competitors(
            business_name=request.business_name,
            business_category=request.business_category,
            city=request.city,
            target_audience=request.target_audience,
            average_price=request.average_price,
            max_results=request.max_results
        )
        
        # Format results
        result = format_discovery_results(competitors)
        result["timestamp"] = datetime.now().isoformat()
        
        return result
        
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Competitor discovery error: {str(e)}")


# ============================================================================
# STARTUP
# ============================================================================

if __name__ == "__main__":
    import uvicorn
    
    print()
    print("=" * 80)
    print(" " * 25 + "🚀 RivalSense AI API Server")
    print("=" * 80)
    print()
    print("Starting FastAPI server...")
    print()
    print("📡 API Documentation: http://localhost:8000/docs")
    print("🏥 Health Check: http://localhost:8000/health")
    print("⚔️  War Room: POST http://localhost:8000/run-war-room")
    print()
    print("=" * 80)
    print()
    
    uvicorn.run("api_server:app", host="0.0.0.0", port=8000, reload=True)
