import json
import logging
from telegram import Bot
import asyncio

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Bot token for Lifelong Learners Bot
BOT_TOKEN = "6617767169:AAH48MAgEo6xks6sycjkDkAbXkSHMWNnQ5o"

async def test_bot_functionality():
    """Test the bot functionality locally"""
    
    # Sample Telegram webhook data (simulating what Telegram would send)
    sample_webhook_data = {
        "message": {
            "text": "/start",
            "chat": {
                "id": 123456789  # This would be the actual chat ID from Telegram
            }
        }
    }
    
    print("🤖 Lifelong Learners Bot Test")
    print("=" * 50)
    
    try:
        # Parse the message (simulating what our Azure Function does)
        if 'message' in sample_webhook_data and 'text' in sample_webhook_data['message']:
            message_text = sample_webhook_data['message']['text']
            chat_id = sample_webhook_data['message']['chat']['id']
            
            print(f"📨 Received message: {message_text}")
            print(f"💬 Chat ID: {chat_id}")
            
            # Initialize bot
            bot = Bot(token=BOT_TOKEN)
            
            # Check if the command is /start
            if message_text == "/start":
                response_text = "Welcome to Lifelong Learners Bot! 🎓"
                print("✅ Sending welcome message")
            else:
                response_text = f"Received: {message_text}"
                print(f"✅ Acknowledging message: {message_text}")
            
            print(f"🤖 Bot would send: '{response_text}'")
            
            # Note: We can't actually send messages without a real chat ID
            # But we can test the bot's info
            try:
                bot_info = await bot.get_me()
                print(f"🤖 Bot name: {bot_info.first_name}")
                print(f"🤖 Bot username: @{bot_info.username}")
                print("✅ Bot token is valid!")
            except Exception as e:
                print(f"❌ Error getting bot info: {e}")
            
        else:
            print("❌ No message text found in request")
            
    except Exception as e:
        print(f"❌ Error: {e}")

def test_different_messages():
    """Test how the bot would respond to different messages"""
    
    test_messages = [
        "/start",
        "Hello there!",
        "What's the weather like?",
        "/help",
        "Tell me a joke"
    ]
    
    print("\n🧪 Testing Different Messages")
    print("=" * 50)
    
    for message in test_messages:
        if message == "/start":
            response = "Welcome to Lifelong Learners Bot! 🎓"
        else:
            response = f"Received: {message}"
        
        print(f"📨 Input: {message}")
        print(f"🤖 Output: {response}")
        print("-" * 30)

if __name__ == "__main__":
    print("🚀 Starting Lifelong Learners Bot Test...")
    
    # Test the main functionality
    asyncio.run(test_bot_functionality())
    
    # Test different messages
    test_different_messages()
    
    print("\n✅ Test completed!")
    print("\n📝 Next steps:")
    print("1. Deploy to your existing Azure Function App")
    print("2. Set up webhook URL in Telegram")
    print("3. Test with real messages in Telegram") 