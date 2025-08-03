# 🚀 Turtle Bot Azure Deployment Script
# Run this script to deploy your bot to Azure Functions

Write-Host "🤖 Turtle Bot Azure Deployment" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green

# Check if Azure CLI is installed
Write-Host "Checking Azure CLI..." -ForegroundColor Yellow
try {
    az --version | Out-Null
    Write-Host "✅ Azure CLI is installed" -ForegroundColor Green
} catch {
    Write-Host "❌ Azure CLI not found. Please install it first:" -ForegroundColor Red
    Write-Host "https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows" -ForegroundColor Cyan
    exit 1
}

# Check if Azure Functions Core Tools is installed
Write-Host "Checking Azure Functions Core Tools..." -ForegroundColor Yellow
try {
    func --version | Out-Null
    Write-Host "✅ Azure Functions Core Tools is installed" -ForegroundColor Green
} catch {
    Write-Host "❌ Azure Functions Core Tools not found. Installing..." -ForegroundColor Red
    npm install -g azure-functions-core-tools@4 --unsafe-perm true
}

# Login to Azure
Write-Host "Logging into Azure..." -ForegroundColor Yellow
az login

# Create resource group
Write-Host "Creating resource group..." -ForegroundColor Yellow
az group create --name turtle-bot-rg --location eastus

# Create storage account
Write-Host "Creating storage account..." -ForegroundColor Yellow
az storage account create --name turtlebotstorage --resource-group turtle-bot-rg --location eastus --sku Standard_LRS

# Create function app
Write-Host "Creating function app..." -ForegroundColor Yellow
az functionapp create --resource-group turtle-bot-rg --consumption-plan-location eastus --runtime python --runtime-version 3.9 --functions-version 4 --name turtle-bot-app --storage-account turtlebotstorage --os-type linux

# Set environment variables
Write-Host "Setting environment variables..." -ForegroundColor Yellow
az functionapp config appsettings set --name turtle-bot-app --resource-group turtle-bot-rg --settings "TELEGRAM_BOT_TOKEN=8266679942:AAE-iZM3rLysX2qb_-WEtL_MwtVze7oebqY"

# Deploy the function
Write-Host "Deploying function..." -ForegroundColor Yellow
func azure functionapp publish turtle-bot-app

Write-Host "✅ Deployment completed!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host "Your bot URL: https://turtle-bot-app.azurewebsites.net/api/telegram_webhook" -ForegroundColor Cyan
Write-Host "Set webhook: https://api.telegram.org/bot8266679942:AAE-iZM3rLysX2qb_-WEtL_MwtVze7oebqY/setWebhook?url=https://turtle-bot-app.azurewebsites.net/api/telegram_webhook" -ForegroundColor Cyan
Write-Host "Test your bot in Telegram!" -ForegroundColor Green 