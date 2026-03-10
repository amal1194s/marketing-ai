# 🎯 RivalSense AI - Complete Command Reference

## 📦 Installation Commands

### First Time Setup
```bash
# Navigate to project
cd d:\marketing-ai

# Install all dependencies (automated)
.\install.ps1

# OR manually:
pip install -r requirements.txt
cd rivalsense-ui
npm install
cd ..
```

---

## ▶️ Running the Application

### Option 1: Automated Start (Recommended)
```bash
.\start.ps1
```
Opens two PowerShell windows:
- Backend API on port 8000
- Frontend on port 3000

### Option 2: Manual Start

**Terminal 1 - Backend:**
```bash
python api_server.py
```

**Terminal 2 - Frontend:**
```bash
cd rivalsense-ui
npm run dev
```

### Option 3: Development Mode with Hot Reload

**Backend:**
```bash
uvicorn api_server:app --reload --host 0.0.0.0 --port 8000
```

**Frontend:**
```bash
cd rivalsense-ui
npm run dev
```

---

## 🧪 Testing Commands

### Test Backend API

**Health Check:**
```bash
curl http://localhost:8000/health
```

**Run War Room:**
```bash
curl -X POST http://localhost:8000/run-war-room -H "Content-Type: application/json" -d "{}"
```

**Test Analyst Only:**
```bash
curl -X POST http://localhost:8000/analyze \
  -H "Content-Type: application/json" \
  -d @test_analyst_payload.json
```

### Test Frontend
```bash
# Check if frontend is running
curl http://localhost:3000

# Build for production
cd rivalsense-ui
npm run build

# Start production server
npm start
```

### Test Python Agents Directly

**Test Analyst Agent:**
```bash
python test_agent_b.py
```

**Test Strategist Agent:**
```bash
python test_agent_c.py
```

**Test Complete Pipeline:**
```bash
python war_room_demo.py
```

---

## 🛠️ Development Commands

### Frontend Development

**Install new package:**
```bash
cd rivalsense-ui
npm install <package-name>
```

**Lint code:**
```bash
npm run lint
```

**Type check:**
```bash
npx tsc --noEmit
```

**Format code:**
```bash
npx prettier --write .
```

### Backend Development

**Install new Python package:**
```bash
pip install <package-name>
pip freeze > requirements.txt
```

**Format Python code:**
```bash
black *.py agents/*.py
```

**Lint Python code:**
```bash
flake8 *.py agents/*.py
```

**Run tests:**
```bash
pytest tests/
```

---

## 🚀 Production Commands

### Build Frontend
```bash
cd rivalsense-ui
npm run build
```

### Run Production Backend
```bash
uvicorn api_server:app --host 0.0.0.0 --port 8000 --workers 4
```

### Docker Commands (if using Docker)
```bash
# Build image
docker build -t rivalsense-ai .

# Run container
docker run -p 8000:8000 -p 3000:3000 rivalsense-ai

# Docker Compose
docker-compose up -d
```

---

## 🔍 Debugging Commands

### Check Ports
```bash
# Windows
netstat -ano | findstr :8000
netstat -ano | findstr :3000

# Kill process
taskkill /PID <PID> /F
```

### View Logs

**Backend Logs:**
```bash
# If running with start.ps1, check the red terminal window
# Or redirect to file:
python api_server.py > backend.log 2>&1
```

**Frontend Logs:**
```bash
# Check the blue terminal window
# Or:
cd rivalsense-ui
npm run dev > frontend.log 2>&1
```

### Clear Cache

**Frontend:**
```bash
cd rivalsense-ui
rm -rf .next
rm -rf node_modules
npm install
```

**Python:**
```bash
rm -rf __pycache__
rm -rf agents/__pycache__
```

---

## 📊 API Endpoints Reference

### Base URL
```
http://localhost:8000
```

### Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/health` | Health check |
| POST | `/run-war-room` | Execute complete pipeline |
| POST | `/analyze` | Run Analyst only |
| POST | `/strategy` | Run Strategist only |

### API Documentation
```
http://localhost:8000/docs
```

---

## 🌐 Frontend Routes

| Route | Description |
|-------|-------------|
| `/` | Landing page |
| `/dashboard` | Main dashboard |
| `/competitors` | Competitor tracking |
| `/analysis` | Market analysis |
| `/strategy` | Strategy recommendations |
| `/war-room` | AI agent pipeline |
| `/settings` | Application settings |

---

## 🐛 Common Issues & Solutions

### "Module not found" Error
```bash
# Backend
pip install -r requirements.txt

# Frontend
cd rivalsense-ui
npm install
```

### Port Already in Use
```bash
# Change backend port
uvicorn api_server:app --port 8001

# Change frontend port
npm run dev -- -p 3001
```

### CORS Error
Ensure backend is running before frontend. Check `.env.local`:
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### TypeScript Errors
```bash
cd rivalsense-ui
rm -rf node_modules
npm install
```

---

## 📝 File Locations

### Configuration Files
- `requirements.txt` - Python dependencies
- `rivalsense-ui/package.json` - Node dependencies
- `rivalsense-ui/.env.local` - Environment variables
- `rivalsense-ui/tsconfig.json` - TypeScript config
- `rivalsense-ui/tailwind.config.ts` - Tailwind CSS config

### Data Files
- `example_business_profile.json` - Sample business data
- `example_competitor_findings.json` - Sample competitor data
- `data/outputs/` - Generated analysis outputs

### Agent Files
- `agent_b_analyst.py` - Analyst Agent (Agent B)
- `agent_c_strategist.py` - Strategist Agent (Agent C)
- `agents/scout_agent/scout_agent.py` - Scout Agent

### API Files
- `api_server.py` - FastAPI backend server
- `rivalsense-ui/lib/api.ts` - Frontend API client

---

## 💡 Pro Tips

1. **Always start backend before frontend** to avoid connection errors
2. **Use `.\start.ps1`** for quickest setup
3. **Keep both terminals open** to monitor logs
4. **Use API docs** at `/docs` for testing
5. **Check health endpoint** first when debugging

---

## 🎯 Quick Commands Cheat Sheet

```bash
# Install everything
.\install.ps1

# Start everything
.\start.ps1

# Test API
curl http://localhost:8000/health

# Run War Room
curl -X POST http://localhost:8000/run-war-room

# Open Frontend
start http://localhost:3000

# View API Docs
start http://localhost:8000/docs
```

---

**Need help? Check SETUP_AND_RUN.md or DEMO_GUIDE.md**
