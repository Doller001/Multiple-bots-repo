from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from handlers import start, callbacks, stats, broadcast

BOT_TOKEN = "8236683990:AAGoq9LhffBwNHwbYfgwKaefFLHkN7q9-lI"

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(CommandHandler("broadcast", broadcast))
    dp.add_handler(CallbackQueryHandler(callbacks))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
