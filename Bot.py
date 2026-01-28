import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get bot token from Render Environment Variables
TOKEN = os.getenv("8315107200:AAEp2PJtGdwwXXFeL-62WnWKLhb3NuOc0xs")

if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is not set")

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot is running successfully!")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("Bot started...")
    app.run_polling()  # keeps the bot running forever

if __name__ == "__main__":
    main()
