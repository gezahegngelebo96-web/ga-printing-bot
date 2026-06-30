import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    print("❌ TOKEN NOT FOUND - Check Railway Variables")

menu = [
    ["📸 Photo Editing", "🪪 ID Photo"],
    ["🎓 Graduation Design", "🖨 Printing"],
    ["📦 Order Status", "📞 Contact Us"],
]

keyboard = ReplyKeyboardMarkup(menu, resize_keyboard=True)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to GA Printing & Studio 🇪🇹\nChoose service:",
        reply_markup=keyboard
    )

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "📸 Photo Editing":
        await update.message.reply_text("Send your photo 📸")
    elif text == "🪪 ID Photo":
        await update.message.reply_text("Send ID details 🪪")
    elif text == "🎓 Graduation Design":
        await update.message.reply_text("Send graduation info 🎓")
    elif text == "🖨 Printing":
        await update.message.reply_text("Send file for printing 🖨")
    elif text == "📦 Order Status":
        await update.message.reply_text("Enter your order ID 📦")
    elif text == "📞 Contact Us":
        await update.message.reply_text(
            "GA Printing Studio\n📍 Konso-Karat\n📞 +251912702062 / +251916357344 / +251970057813"
        )
    else:
        await update.message.reply_text("Please choose from menu.")

def main():
    print("🚀 BOT STARTING...")

    app = Application.builder().token(TOKEN).build()

    print("✅ APP BUILT SUCCESSFULLY")

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle))

    app.run_polling()

if __name__ == "__main__":
    main()
