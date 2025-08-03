import azure.functions as func
import logging
import json
import os
from telegram import Bot, Update
from telegram.ext import Application

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the app at the top
app = func.FunctionApp()

@app.route(route="telegram_webhook")
async def telegram_webhook(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP trigger for Telegram webhook
    Handles /start command and other messages
    """
    try:
        # Log that a request was received
        logger.info("Telegram webhook request received")
        
        # Get the request body
        body = req.get_body().decode('utf-8')
        logger.info(f"Request body: {body}")
        
        # Parse the JSON data
        data = json.loads(body)
        
        # Extract message information
        if 'message' in data and 'text' in data['message']:
            message_text = data['message']['text']
            chat_id = data['message']['chat']['id']
            
            logger.info(f"Received message: {message_text} from chat_id: {chat_id}")
            
            # Get bot token from environment variable
            bot_token = os.environ.get("TELEGRAM_BOT_TOKEN")
            if not bot_token:
                logger.error("TELEGRAM_BOT_TOKEN not found in environment variables")
                return func.HttpResponse(
                    body="Bot token not configured",
                    status_code=500,
                    mimetype="text/plain"
                )
            
            # Initialize bot
            bot = Bot(token=bot_token)
            
            # Check if the command is /start
            if message_text == "/start":
                response_text = "Welcome to Lifelong Learners Bot! 🎓"
                logger.info("Sending welcome message")
            else:
                response_text = f"Received: {message_text}"
                logger.info(f"Acknowledging message: {message_text}")
            
            # Send the response
            await bot.send_message(chat_id=chat_id, text=response_text)
            
            return func.HttpResponse(
                body="OK",
                status_code=200,
                mimetype="text/plain"
            )
        else:
            logger.info("No message text found in request")
            return func.HttpResponse(
                body="No message text",
                status_code=200,
                mimetype="text/plain"
            )
            
    except Exception as e:
        logger.error(f"Error in telegram_webhook: {e}")
        return func.HttpResponse(
            body=f"Error: {str(e)}",
            status_code=500,
            mimetype="text/plain"
        ) 