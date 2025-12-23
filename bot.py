from flask import Flask
import threading
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from handlers import start, callbacks
from admin import admin_handlers

BOT_TOKEN = "8236683990:AAGuQN5QKhcx7peERy9yUe_sR0qrS7RvEYA"

# 🌐 Flask (Render + UptimeRobot)
app = Flask(__name__)
@app.route("/")
def home():
    return "Bot is running"

def run_flask():
    app.run(host="0.0.0.0", port=10000)

def main():
    threading.Thread(target=run_flask).start()

    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(callbacks))
    admin_handlers(dp)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
