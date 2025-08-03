# 🐢 Lifelong Learners Bot

A Telegram bot built with Azure Functions that provides educational content about famous philosophers. The bot helps users learn about philosophical thinkers, their works, and famous quotes.

## ✨ Features

- **Philosopher Lookup**: Get detailed information about philosophers using `/philosopher <name>`
- **Educational Content**: Learn about philosophers' lives, works, and famous quotes
- **Easy Commands**: Simple and intuitive command structure
- **Rich Information**: Includes era, school of thought, key works, and famous quotes

## 🤖 Available Commands

- `/start` - Welcome message and instructions
- `/philosopher <name>` - Get information about a specific philosopher
- `/help` - Show all available commands and philosophers

## 📚 Available Philosophers

- **Socrates** - Classical Greek philosopher, founder of Western philosophy
- **Plato** - Student of Socrates, founder of Platonism
- **Aristotle** - Student of Plato, systematic approach to philosophy and science

## 🛠️ Technology Stack

- **Azure Functions** - Serverless computing platform
- **Python** - Programming language
- **python-telegram-bot** - Telegram Bot API wrapper
- **JSON** - Data storage for philosopher information

## 🚀 Quick Start

1. Set up your Telegram bot token in Azure Function App settings
2. Deploy the function to Azure
3. Configure the webhook URL in your Telegram bot
4. Start chatting with your bot!

## 📁 Project Structure

```
turtle_bot/
├── function_app.py      # Main Azure Function
├── philosophers.json    # Philosopher data
├── requirements.txt     # Python dependencies
├── host.json           # Azure Functions configuration
└── README.md           # This file
```

## 🎯 Example Usage

```
User: /start
Bot: Welcome to the Lifelong Learners Bot! 🎓
     Ask me about a philosopher using:
     /philosopher <name>
     Example: /philosopher socrates

User: /philosopher socrates
Bot: 🎓 Socrates
     📅 Era: Ancient Greece (469-399 BCE)
     🏛️ School: Classical Greek Philosophy
     📖 Summary: Socrates was a classical Greek philosopher...
     📚 Key Works: Apology, Crito, Phaedo
     💭 Famous Quotes:
     • "The unexamined life is not worth living."
     • "I know that I know nothing."
```

## 🔧 Configuration

The bot requires the following environment variable:
- `TELEGRAM_BOT_TOKEN` - Your Telegram bot token from BotFather

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Built with ❤️ for lifelong learning**
