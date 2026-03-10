"""
Quick Test Script for RivalSense AI System
Tests the complete War Room pipeline end-to-end
"""

import requests
import json
import time
from colorama import init, Fore, Style

# Initialize colorama for Windows
init()

def print_header(text):
    """Print formatted header"""
    print()
    print(Fore.CYAN + "=" * 80)
    print(f"  {text}")
    print("=" * 80 + Style.RESET_ALL)
    print()

def print_success(text):
    """Print success message"""
    print(Fore.GREEN + "✅ " + text + Style.RESET_ALL)

def print_error(text):
    """Print error message"""
    print(Fore.RED + "❌ " + text + Style.RESET_ALL)

def print_info(text):
    """Print info message"""
    print(Fore.YELLOW + "ℹ️  " + text + Style.RESET_ALL)

def test_health():
    """Test API health endpoint"""
    print_header("Testing Backend Health")
    
    try:
        response = requests.get("http://localhost:8000/health", timeout=5)
        if response.status_code == 200:
            data = response.json()
            print_success(f"Backend is healthy!")
            print(f"   Service: {data.get('service')}")
            print(f"   Status: {data.get('status')}")
            return True
        else:
            print_error(f"Health check failed with status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print_error("Cannot connect to backend. Is it running on port 8000?")
        print_info("Start backend with: python api_server.py")
        return False
    except Exception as e:
        print_error(f"Health check error: {str(e)}")
        return False

def test_war_room():
    """Test War Room endpoint"""
    print_header("Testing War Room Pipeline")
    
    print_info("Sending request to /run-war-room...")
    
    try:
        start_time = time.time()
        response = requests.post(
            "http://localhost:8000/run-war-room",
            json={},
            timeout=30
        )
        duration = time.time() - start_time
        
        if response.status_code == 200:
            data = response.json()
            
            print_success(f"War Room completed in {duration:.2f} seconds!")
            print()
            
            # Display results
            print(Fore.CYAN + "📊 Results Summary:" + Style.RESET_ALL)
            print()
            
            # Business info
            business = data.get('business', {})
            print(f"Business: {business.get('name', 'Unknown')}")
            print(f"Your Price: ${business.get('pricing', {}).get('average_price', 'N/A')}")
            print()
            
            # Scout results
            scout = data.get('scout', {})
            print(f"🔍 Scout found: {scout.get('competitors_found', 0)} competitors")
            print()
            
            # Analyst results
            analyst = data.get('analyst', {})
            print(f"🔬 Analyst Assessment:")
            print(f"   Impact Level: {analyst.get('impact_level', 'Unknown').upper()}")
            print(f"   Threat Score: {analyst.get('threat_score', 'N/A')}/10")
            print(f"   Urgency: {analyst.get('recommended_urgency', 'Unknown').upper()}")
            print()
            
            # Strategist results
            strategist = data.get('strategist', {})
            print(f"🎯 Strategist Recommendation:")
            print(f"   Strategy: {strategist.get('strategy_title', 'N/A')}")
            print(f"   Actions: {len(strategist.get('action_steps', []))} steps")
            
            if strategist.get('marketing_post'):
                print(f"   Marketing: Ready-to-use content generated!")
            print()
            
            return True
        else:
            print_error(f"War Room failed with status {response.status_code}")
            try:
                error_data = response.json()
                print(f"   Error: {error_data.get('detail', 'Unknown error')}")
            except:
                pass
            return False
            
    except requests.exceptions.Timeout:
        print_error("War Room request timed out (>30 seconds)")
        return False
    except Exception as e:
        print_error(f"War Room error: {str(e)}")
        return False

def test_frontend():
    """Test frontend availability"""
    print_header("Testing Frontend")
    
    try:
        response = requests.get("http://localhost:3000", timeout=5)
        if response.status_code == 200:
            print_success("Frontend is running!")
            print_info("Open http://localhost:3000 in your browser")
            return True
        else:
            print_error(f"Frontend returned status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print_error("Cannot connect to frontend. Is it running on port 3000?")
        print_info("Start frontend with: cd rivalsense-ui && npm run dev")
        return False
    except Exception as e:
        print_error(f"Frontend test error: {str(e)}")
        return False

def main():
    """Run all tests"""
    print()
    print(Fore.CYAN + Style.BRIGHT + "=" * 80)
    print(" " * 20 + "🚀 RivalSense AI - System Test")
    print("=" * 80 + Style.RESET_ALL)
    print()
    
    print("Testing complete system...")
    print()
    
    # Track results
    results = {
        "backend": False,
        "war_room": False,
        "frontend": False
    }
    
    # Run tests
    results["backend"] = test_health()
    
    if results["backend"]:
        results["war_room"] = test_war_room()
    else:
        print_info("Skipping War Room test (backend not available)")
    
    results["frontend"] = test_frontend()
    
    # Summary
    print_header("Test Summary")
    
    passed = sum(results.values())
    total = len(results)
    
    print(f"Tests Passed: {passed}/{total}")
    print()
    
    if results["backend"]:
        print_success("Backend API: WORKING")
    else:
        print_error("Backend API: FAILED")
    
    if results["war_room"]:
        print_success("War Room Pipeline: WORKING")
    else:
        print_error("War Room Pipeline: FAILED")
    
    if results["frontend"]:
        print_success("Frontend: WORKING")
    else:
        print_error("Frontend: FAILED")
    
    print()
    
    if passed == total:
        print(Fore.GREEN + Style.BRIGHT + "🎉 All systems operational! Ready for demo!" + Style.RESET_ALL)
        print()
        print("Next steps:")
        print("  1. Open http://localhost:3000")
        print("  2. Click 'War Room' in sidebar")
        print("  3. Click 'Start Analysis'")
    else:
        print(Fore.YELLOW + "⚠️  Some systems need attention. Check errors above." + Style.RESET_ALL)
        print()
        if not results["backend"]:
            print("Start backend: python api_server.py")
        if not results["frontend"]:
            print("Start frontend: cd rivalsense-ui && npm run dev")
    
    print()

if __name__ == "__main__":
    # Try to import colorama, if not available use plain output
    try:
        from colorama import init, Fore, Style
        init()
    except ImportError:
        print("Note: Install colorama for colored output: pip install colorama")
        # Fallback: disable colors
        class FakeFore:
            CYAN = RED = GREEN = YELLOW = ""
        class FakeStyle:
            RESET_ALL = BRIGHT = ""
        Fore = FakeFore()
        Style = FakeStyle()
    
    main()
