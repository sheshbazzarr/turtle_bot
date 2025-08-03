# 🚀 Lifelong Learners Bot Deployment Script
# For existing Azure resources

Write-Host "🤖 Lifelong Learners Bot Deployment" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green

# Get Function App name from user
$functionAppName = Read-Host "Enter your Azure Function App name"

Write-Host "Deploying to: $functionAppName" -ForegroundColor Yellow

# Set environment variables
Write-Host "Setting environment variables..." -ForegroundColor Yellow
az functionapp config appsettings set --name $functionAppName --resource-group $functionAppName-rg --settings "TELEGRAM_BOT_TOKEN=6617767169:AAH48MAgEo6xks6sycjkDkAbXkSHMWNnQ5o"

# Deploy the function
Write-Host "Deploying function..." -ForegroundColor Yellow
func azure functionapp publish $functionAppName

Write-Host "✅ Deployment completed!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Green
Write-Host "Your bot URL: https://$functionAppName.azurewebsites.net/api/telegram_webhook" -ForegroundColor Cyan
Write-Host "Set webhook: https://api.telegram.org/bot6617767169:AAH48MAgEo6xks6sycjkDkAbXkSHMWNnQ5o/setWebhook?url=https://$functionAppName.azurewebsites.net/api/telegram_webhook" -ForegroundColor Cyan
Write-Host "Test your bot in Telegram!" -ForegroundColor Green 