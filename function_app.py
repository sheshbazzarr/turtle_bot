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

# This creates a path to your philosophers.json file that works both locally and in Azure
# It finds the directory where the script is located and joins the filename to it.
PHILOSOPHERS_FILE_PATH = os.path.join(os.path.dirname(__file__), 'philosophers.json')

def load_philosophers_data():
    """Load philosopher data from JSON file"""
    try:
        with open(PHILOSOPHERS_FILE_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logger.error(f"Philosophers file not found at {PHILOSOPHERS_FILE_PATH}")
        return {}
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing philosophers.json: {e}")
        return {}
    except Exception as e:
        logger.error(f"Unexpected error loading philosophers data: {e}")
        return {}

def handle_philosopher_command(philosopher_name, philosophers_data):
    """Handle /philosopher command and return appropriate response"""
    if not philosopher_name:
        return "Please provide a philosopher's name. Example: /philosopher plato"
    
    # Make the name lowercase to match our JSON keys
    philosopher_name = philosopher_name.lower()
    
    # Get the philosophers dictionary from the nested structure
    philosophers = philosophers_data.get('philosophers', {})
    
    # Use .get() to safely retrieve the data. It returns None if the key doesn't exist.
    philosopher_info = philosophers.get(philosopher_name)
    
    if philosopher_info:
        # Format the philosopher information nicely
        response = f"🎓 **{philosopher_info['name']}**\n\n"
        response += f"📅 **Era:** {philosopher_info['era']}\n"
        response += f"🏛️ **School:** {philosopher_info['school']}\n\n"
        response += f"📖 **Summary:** {philosopher_info['summary']}\n\n"
        
        if philosopher_info.get('key_works'):
            response += f"📚 **Key Works:** {', '.join(philosopher_info['key_works'])}\n\n"
        
        if philosopher_info.get('famous_quotes'):
            response += "💭 **Famous Quotes:**\n"
            for quote in philosopher_info['famous_quotes']:
                response += f"• \"{quote}\"\n"
        
        return response
    else:
        return f"Sorry, I don't have information on '{philosopher_name}'. Try another philosopher!"

@app.route(route="telegram_webhook")
async def telegram_webhook(req: func.HttpRequest) -> func.HttpResponse:
    """
    HTTP trigger for Telegram webhook
    Handles /start command, /philosopher command, and other messages
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
            
            # Load philosophers data
            philosophers_data = load_philosophers_data()
            
            # Handle different commands
            if message_text == "/start":
                response_text = "Welcome to the Lifelong Learners Bot! 🎓\n\nAsk me about a philosopher using:\n/philosopher <name>\n\nExample: /philosopher socrates"
                logger.info("Sending welcome message")
            
            elif message_text.lower().startswith('/philosopher'):
                # Split the command to get the name. e.g., ['/philosopher', 'plato']
                parts = message_text.split()
                philosopher_name = parts[1] if len(parts) > 1 else None
                response_text = handle_philosopher_command(philosopher_name, philosophers_data)
                logger.info(f"Handling philosopher command for: {philosopher_name}")
            
            elif message_text.lower().startswith('/help'):
                # Get available philosophers for the help message
                philosophers = philosophers_data.get('philosophers', {})
                available_philosophers = list(philosophers.keys())
                
                response_text = f"""🤖 Lifelong Learners Bot Commands:

/start - Welcome message
/philosopher <name> - Get information about a philosopher
/help - Show this help message

Available philosophers:
{', '.join(available_philosophers).title()}

Examples:
/philosopher socrates
/philosopher plato
/philosopher aristotle"""
                logger.info("Sending help message")
            
            else:
                response_text = f"I received your message: '{message_text}'\n\nUse /help to see available commands."
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
            
    except json.JSONDecodeError as e:
        logger.error(f"Error parsing JSON from request body: {e}")
        return func.HttpResponse(
            body="Invalid JSON in request body",
            status_code=400,
            mimetype="text/plain"
        )
    except Exception as e:
        logger.error(f"Error in telegram_webhook: {e}")
        return func.HttpResponse(
            body=f"Error: {str(e)}",
            status_code=500,
            mimetype="text/plain"
        ) 