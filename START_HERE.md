# RivalSense AI - Quick Start Guide

## 🚀 Three Ways to Start Your Project

### Method 1: Double-Click (Easiest)
Simply double-click: **`START.bat`**

### Method 2: PowerShell Script
```powershell
.\start.ps1
```

### Method 3: Manual (Two Terminals)

**Terminal 1 - Backend:**
```powershell
python api_server.py
```

**Terminal 2 - Frontend:**
```powershell
cd rivalsense-ui
npm run dev
```

---

## 📍 Access Your Application

After starting, open these URLs:

| Service | URL |
|---------|-----|
| **Frontend** | http://localhost:3000 |
| **War Room** | http://localhost:3000/war-room |
| **API Docs** | http://localhost:8000/docs |
| **API Health** | http://localhost:8000/health |

---

## ⚡ Quick Demo Flow

1. **Wait 10 seconds** for services to start
2. **Open** http://localhost:3000
3. **Click** "War Room" in sidebar
4. **Click** "Start Analysis"
5. **Watch** the AI magic happen! 🎉

---

## 🛑 How to Stop

Press **Ctrl+C** in each PowerShell window that opened.

---

## 🐛 Troubleshooting

**"Port already in use"**
```powershell
# Kill processes on port 8000
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Kill processes on port 3000
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

**"Module not found"**
```powershell
# Backend dependencies
pip install -r requirements.txt

# Frontend dependencies
cd rivalsense-ui
npm install
```

---

**That's it! You're ready to demo! 🚀**
