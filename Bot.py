import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("8315107200:AAEp2PJtGdwwXXFeL-62WnWKLhb3NuOc0xs")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN environment variable not set")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🤖 Bot is running on Render!")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started successfully...")
    app.run_polling()  # 🔴 THIS keeps the app alive

if __name__ == "__main__":
    main()
