# Install RivalSense AI Dependencies

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host "     🚀 RivalSense AI - Dependency Installer" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Cyan
Write-Host ""

# Check if in correct directory
if (-not (Test-Path "requirements.txt")) {
    Write-Host "❌ Error: requirements.txt not found!" -ForegroundColor Red
    Write-Host "Please run this script from the d:\marketing-ai directory" -ForegroundColor Yellow
    exit 1
}

# Install Python dependencies
Write-Host "📦 Installing Python dependencies..." -ForegroundColor Yellow
Write-Host ""

try {
    pip install -r requirements.txt
    Write-Host ""
    Write-Host "✅ Python dependencies installed!" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to install Python dependencies" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    exit 1
}

Write-Host ""

# Check if rivalsense-ui exists
if (-not (Test-Path "rivalsense-ui")) {
    Write-Host "❌ Error: rivalsense-ui directory not found!" -ForegroundColor Red
    exit 1
}

# Install Frontend dependencies
Write-Host "📦 Installing Frontend dependencies..." -ForegroundColor Yellow
Write-Host ""

try {
    Set-Location rivalsense-ui
    npm install
    Set-Location ..
    Write-Host ""
    Write-Host "✅ Frontend dependencies installed!" -ForegroundColor Green
} catch {
    Write-Host "❌ Failed to install Frontend dependencies" -ForegroundColor Red
    Write-Host "Error: $_" -ForegroundColor Red
    Set-Location ..
    exit 1
}

Write-Host ""
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
Write-Host "     ✅ Installation Complete!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Cyan
Write-Host "  1. Run: .\start.ps1" -ForegroundColor White
Write-Host "  2. Open: http://localhost:3000" -ForegroundColor White
Write-Host "  3. Navigate to War Room and click 'Start Analysis'" -ForegroundColor White
Write-Host ""
Write-Host "Happy analyzing! 🎯" -ForegroundColor Green
Write-Host ""
