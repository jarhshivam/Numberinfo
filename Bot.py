import requests
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Hi! Use /num 9876543210")

async def num(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("❗ Usage: /num 9876543210")
        return

    number = context.args[0]

    url = f"https://api-rootxindia.vercel.app/?type=num&key=demo_reddit&query={number}"

    try:
        res = requests.get(url)
        data = res.json()

        msg = f"📱 Number: {number}\n\n"

        if isinstance(data, dict):
            for k, v in data.items():
                msg += f"{k}: {v}\n"
        else:
            msg += str(data)

        await update.message.reply_text(msg)

    except:
        await update.message.reply_text("⚠️ Error fetching data")

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("num", num))

    print("Bot running...")
    app.run_polling()

if __name__ == "__main__":
    main()
