# PowerShell script to update tools and setup lab environment

Set-Location $env:USERPROFILE

Write-Host "Step 1: Updating azd and VS Code" -ForegroundColor Cyan
winget upgrade microsoft.azd microsoft.visualstudiocode

Write-Host "Step 2: Updating VS Code extensions" -ForegroundColor Cyan
code --update-extensions

Write-Host "Step 3: Starting Docker Desktop" -ForegroundColor Cyan
docker desktop start

Write-Host "Step 4: Cloning lab repository" -ForegroundColor Cyan
git clone https://github.com/microsoft/build25-LAB309.git

Write-Host "Step 5: Opening project in VS Code" -ForegroundColor Cyan
code build25-LAB309

Write-Host "Step 6: Opening lab instructions" -ForegroundColor Cyan
Start-Process "https://aka.ms/build25-lab309-repo"

Write-Host "Setup complete! You may now close this window." -ForegroundColor Green

Exit
