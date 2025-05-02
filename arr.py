import logging
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)
import dadJokes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot Token (Replace with yours)
BOT_TOKEN = "7646364330:AAE_8-t0pvB59bv3jY21y7KcXP6Yy6fE-PU"

# ===== Handlers =====
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when /start is issued."""
    user = update.effective_user
    await update.message.reply_text(
        f"Hi {user.first_name}! I'm your bot.\n\n"
        "Use /help to see available commands."
    )

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when /help is issued."""
    help_text = """
    Available commands:
    /start - Start the bot
    /help - Show this help message
    """
    await update.message.reply_text(help_text)

async def dadJoke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Send a message when /help is issued."""
    joke_text = dadJokes.dad_joke_generator()
    await update.message.reply_text(joke_text)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Echo the user message."""
    await update.message.reply_text(update.message.text)

# ===== Error Handler =====
async def error_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Log errors."""
    logger.error(f"Update {update} caused error: {context.error}")

# ===== Main Function =====
def main():
    # Create the Application
    application = Application.builder().token(BOT_TOKEN).build()

    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help))
    application.add_handler(CommandHandler("dadJoke", dadJoke))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Add error handler
    application.add_error_handler(error_handler)

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()