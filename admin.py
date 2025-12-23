from telegram import Update
from telegram.ext import CallbackContext
from database import get_all_users, total_users

ADMINS = [7764057183]

def stats(update: Update, context: CallbackContext):
    if update.effective_user.id in ADMINS:
        update.message.reply_text(f"👤 Total Users: {total_users()}")

def broadcast(update: Update, context: CallbackContext):
    if update.effective_user.id not in ADMINS:
        return

    if not update.message.reply_to_message:
        update.message.reply_text("Reply ke saath /broadcast bhejo.")
        return

    msg = update.message.reply_to_message
    ok, fail = 0, 0

    for uid in get_all_users():
        try:
            context.bot.copy_message(uid, msg.chat_id, msg.message_id)
            ok += 1
        except:
            fail += 1

    update.message.reply_text(f"📢 Done\n✅ {ok} | ❌ {fail}")
