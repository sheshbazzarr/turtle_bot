# 🚀 Azure Setup Guide for Students

## Step 1: Azure Account Setup
1. Go to [Azure for Students](https://azure.microsoft.com/en-us/free/students/)
2. Sign up with your student email
3. Verify your student status
4. You get $100 free credit + free services for 12 months!

## Step 2: Install Azure CLI
### Windows:
```bash
# Download and install from:
# https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-windows
```

### macOS:
```bash
brew install azure-cli
```

### Linux:
```bash
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash
```

## Step 3: Install Azure Functions Core Tools
```bash
npm install -g azure-functions-core-tools@4 --unsafe-perm true
```

## Step 4: Login to Azure
```bash
az login
```

## Step 5: Create Azure Resources
```bash
# Create a resource group
az group create --name turtle-bot-rg --location eastus

# Create a storage account
az storage account create --name turtlebotstorage --resource-group turtle-bot-rg --location eastus --sku Standard_LRS

# Create a function app
az functionapp create --resource-group turtle-bot-rg --consumption-plan-location eastus --runtime python --runtime-version 3.9 --functions-version 4 --name turtle-bot-app --storage-account turtlebotstorage --os-type linux
```

## Step 6: Deploy Your Bot
```bash
# Navigate to your project folder
cd turtle_bot

# Deploy to Azure
func azure functionapp publish turtle-bot-app
```

## Step 7: Set Up Telegram Webhook
After deployment, your function URL will be:
```
https://turtle-bot-app.azurewebsites.net/api/telegram_webhook
```

Set this as your webhook in Telegram:
```
https://api.telegram.org/bot8266679942:AAE-iZM3rLysX2qb_-WEtL_MwtVze7oebqY/setWebhook?url=https://turtle-bot-app.azurewebsites.net/api/telegram_webhook
```

## Step 8: Test Your Bot!
1. Open Telegram
2. Find your bot: @your_bot_username
3. Send `/start`
4. You should get: "Welcome to Turtle Bot!"

## 💰 Cost Breakdown (Student Free Tier)
- **Azure Functions**: 1 million executions/month FREE
- **Storage**: 5GB FREE
- **Total Cost**: $0/month for student usage!

## 🆘 Troubleshooting
- If you get errors, check the Azure Function logs
- Make sure your bot token is correct
- Verify the webhook URL is accessible 