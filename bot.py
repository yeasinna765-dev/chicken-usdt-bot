import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN", "YOUR_BOT_TOKEN_FROM_BOTFATHER")
WEB_APP_URL = os.getenv("WEB_APP_URL", "https://your-render-app-url.onrender.com")
ADMIN_ID = 7419171743

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    keyboard = [[InlineKeyboardButton("🐔 Open CHICKEN USDT App", web_app=WebAppInfo(url=WEB_APP_URL))]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    welcome_text = f"Welcome to *CHICKEN USDT* (@Chikenusdtbot), {user.first_name}!\n\nEarn USDT and GRAM by feeding hens and growing your farm."
    if user.id == ADMIN_ID:
        welcome_text += "\n\n👑 *Admin Recognized*: Full admin controls unlocked in WebApp."
        
    await update.message.reply_text(welcome_text, parse_mode="Markdown", reply_markup=reply_markup)

if __name__ == "__main__":
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()
