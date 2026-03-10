# Start RivalSense AI System

Write-Host "🚀 Starting RivalSense AI..." -ForegroundColor Cyan
Write-Host ""

# Check if in correct directory
if (-not (Test-Path "api_server.py")) {
    Write-Host "❌ Error: api_server.py not found!" -ForegroundColor Red
    Write-Host "Please run this script from the d:\marketing-ai directory" -ForegroundColor Yellow
    exit 1
}

if (-not (Test-Path "rivalsense-ui")) {
    Write-Host "❌ Error: rivalsense-ui directory not found!" -ForegroundColor Red
    exit 1
}

# Check Python
Write-Host "Checking Python..." -ForegroundColor Yellow
try {
    $pythonVersion = python --version 2>&1
    Write-Host "✅ $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Python not found! Please install Python 3.8+" -ForegroundColor Red
    exit 1
}

# Check Node
Write-Host "Checking Node.js..." -ForegroundColor Yellow
try {
    $nodeVersion = node --version 2>&1
    Write-Host "✅ Node.js $nodeVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Node.js not found! Please install Node.js 18+" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Starting services..." -ForegroundColor Cyan
Write-Host ""

# Start Backend
Write-Host "📡 Starting Backend API on port 8000..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Write-Host '🔴 Backend API Server' -ForegroundColor Red; Write-Host ''; cd '$PWD'; python api_server.py"

Start-Sleep -Seconds 3

# Start Frontend
Write-Host "🎨 Starting Frontend on port 3000..." -ForegroundColor Yellow
Start-Process powershell -ArgumentList "-NoExit", "-Command", "Write-Host '🔵 Frontend Dev Server' -ForegroundColor Blue; Write-Host ''; cd '$PWD\rivalsense-ui'; npm run dev"

Write-Host ""
Write-Host "✅ RivalSense AI is starting up!" -ForegroundColor Green
Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host ""
Write-Host "  Backend API:  " -NoNewline -ForegroundColor Cyan
Write-Host "http://localhost:8000" -ForegroundColor White
Write-Host "  API Docs:     " -NoNewline -ForegroundColor Cyan
Write-Host "http://localhost:8000/docs" -ForegroundColor White
Write-Host ""
Write-Host "  Frontend:     " -NoNewline -ForegroundColor Cyan
Write-Host "http://localhost:3000" -ForegroundColor White
Write-Host "  War Room:     " -NoNewline -ForegroundColor Cyan
Write-Host "http://localhost:3000/war-room" -ForegroundColor White
Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host ""
Write-Host "⚡ Pro Tip: Wait 10 seconds for services to fully start" -ForegroundColor Yellow
Write-Host "⚡ Press Ctrl+C in each window to stop" -ForegroundColor Yellow
Write-Host ""
Write-Host "Happy analyzing! 🎯" -ForegroundColor Green
Write-Host ""
