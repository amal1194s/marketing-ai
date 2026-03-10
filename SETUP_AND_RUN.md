# RivalSense AI - Setup & Run Guide

## 🚀 Quick Start

This guide will help you run the complete RivalSense AI Market Intelligence system.

## 📋 Prerequisites

- **Python 3.8+** (for backend)
- **Node.js 18+** (for frontend)
- **npm or yarn** (for package management)

---

## 🔧 Setup

### 1. Install Python Dependencies

```bash
# Navigate to project root
cd d:\marketing-ai

# Install Python packages
pip install -r requirements.txt
```

### 2. Install Frontend Dependencies

```bash
# Navigate to frontend directory
cd rivalsense-ui

# Install Node.js packages
npm install

# Return to project root
cd ..
```

---

## ▶️ Running the Application

### Option 1: Manual Start (Two Terminals)

**Terminal 1 - Backend API:**
```bash
# From project root (d:\marketing-ai)
python api_server.py
```

✅ Backend will start on: `http://localhost:8000`
📚 API Docs available at: `http://localhost:8000/docs`

**Terminal 2 - Frontend:**
```bash
# From project root
cd rivalsense-ui
npm run dev
```

✅ Frontend will start on: `http://localhost:3000`

### Option 2: PowerShell Script (Recommended)

Create a file `start.ps1` in project root:

```powershell
# Start RivalSense AI System

Write-Host "🚀 Starting RivalSense AI..." -ForegroundColor Cyan
Write-Host ""

# Start Backend
Write-Host "📡 Starting Backend API..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD'; python api_server.py"

Start-Sleep -Seconds 3

# Start Frontend
Write-Host "🎨 Starting Frontend..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "cd '$PWD\rivalsense-ui'; npm run dev"

Write-Host ""
Write-Host "✅ RivalSense AI is starting up!" -ForegroundColor Green
Write-Host ""
Write-Host "Backend:  http://localhost:8000" -ForegroundColor Cyan
Write-Host "Frontend: http://localhost:3000" -ForegroundColor Cyan
Write-Host ""
Write-Host "Press Ctrl+C in each window to stop services" -ForegroundColor Gray
```

Then run:
```bash
.\start.ps1
```

---

## 🎯 Using the War Room

1. **Open Frontend**: Navigate to `http://localhost:3000`

2. **Access War Room**: Click "War Room" in the sidebar or "Run War Room" in the top bar

3. **Run Analysis**: Click "Start Analysis" button

4. **Watch Pipeline**: 
   - 🔍 Scout Agent scans competitors
   - 🔬 Analyst Agent evaluates threats
   - 🎯 Strategist Agent generates recommendations

5. **View Results**: Complete strategy and marketing content displayed on screen

---

## 🔍 Testing the API

### Health Check
```bash
curl http://localhost:8000/health
```

### Run War Room via API
```bash
curl -X POST http://localhost:8000/run-war-room \
  -H "Content-Type: application/json" \
  -d "{}"
```

### Using Python
```python
import requests

# Health check
response = requests.get("http://localhost:8000/health")
print(response.json())

# Run War Room
response = requests.post("http://localhost:8000/run-war-room")
result = response.json()
print(result)
```

---

## 📁 Project Structure

```
d:\marketing-ai\
├── api_server.py              # FastAPI backend
├── agent_b_analyst.py         # Analyst Agent
├── agent_c_strategist.py      # Strategist Agent
├── example_business_profile.json
├── example_competitor_findings.json
├── requirements.txt           # Python dependencies
└── rivalsense-ui/             # Next.js frontend
    ├── app/
    │   ├── war-room/          # War Room page
    │   ├── dashboard/
    │   ├── competitors/
    │   ├── analysis/
    │   └── strategy/
    ├── components/
    │   └── war-room-progress.tsx
    ├── lib/
    │   └── api.ts             # API client
    ├── package.json
    └── .env.local             # Environment variables
```

---

## 🐛 Troubleshooting

### Backend won't start

**Error**: `ModuleNotFoundError: No module named 'fastapi'`

**Fix**:
```bash
pip install fastapi uvicorn pydantic
```

### Frontend won't start

**Error**: `Cannot find module 'next'`

**Fix**:
```bash
cd rivalsense-ui
npm install
```

### CORS Errors in Browser

**Symptom**: War Room shows "Backend API Not Available"

**Fix**: Ensure backend is running on `http://localhost:8000`:
```bash
python api_server.py
```

### Port Already in Use

**Backend (Port 8000)**:
```bash
# Kill existing process
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Or use different port
uvicorn api_server:app --port 8001
```

**Frontend (Port 3000)**:
```bash
# Use different port
cd rivalsense-ui
npm run dev -- -p 3001
```

---

## 🎨 Features

### ✅ Fully Implemented

- ✅ FastAPI backend with War Room pipeline
- ✅ Next.js frontend with responsive UI
- ✅ Real-time War Room progress visualization
- ✅ Complete Analyst (Agent B) integration
- ✅ Complete Strategist (Agent C) integration
- ✅ API health checking
- ✅ Error handling and display
- ✅ Results visualization with insights
- ✅ Marketing content generation
- ✅ Dark mode premium UI

### 🔮 Pages Available

- `/` - Landing page
- `/dashboard` - Main dashboard
- `/competitors` - Competitor tracking
- `/analysis` - Market analysis
- `/strategy` - Strategy recommendations
- `/war-room` - AI agent pipeline execution
- `/settings` - Application settings

---

## 🚦 Quick Status Check

**Is everything running?**

```bash
# Check backend
curl http://localhost:8000/health

# Check frontend
curl http://localhost:3000
```

If both respond, you're good to go! 🎉

---

## 💡 Usage Tips

1. **First Run**: Always start backend before frontend
2. **Development**: Keep both terminals open to see logs
3. **Demo**: Use War Room page for impressive live demonstrations
4. **Results**: Check console logs for detailed agent outputs
5. **Customization**: Edit `example_business_profile.json` for different scenarios

---

## 📞 Support

For issues or questions:
1. Check logs in terminal windows
2. Verify all dependencies are installed
3. Ensure ports 3000 and 8000 are available
4. Review API docs at `http://localhost:8000/docs`

---

**Ready to analyze the market? Let's go! 🚀**
