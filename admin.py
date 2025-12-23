from telegram.ext import CommandHandler
from database import total_users, get_all_users

ADMINS = [7764057183]

def stats(update, context):
    if update.effective_user.id in ADMINS:
        update.message.reply_text(f"👤 Total Users: {total_users()}")

def broadcast(update, context):
    if update.effective_user.id not in ADMINS:
        return

    if not update.message.reply_to_message:
        update.message.reply_text("Reply ke saath /broadcast use karo")
        return

    msg = update.message.reply_to_message
    ok = fail = 0

    for uid in get_all_users():
        try:
            context.bot.copy_message(uid, msg.chat_id, msg.message_id)
            ok += 1
        except:
            fail += 1

    update.message.reply_text(f"📢 Broadcast Done\n✅ {ok} | ❌ {fail}")

def admin_handlers(dp):
    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(CommandHandler("broadcast", broadcast))
