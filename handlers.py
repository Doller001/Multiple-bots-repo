from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackContext
from database import add_user, get_all_users, total_users

ADMINS = [7764057183]   # <-- apna admin id yahin


# -------- JOIN CHANNELS --------
CHANNELS = [
    ("📢 BackUp Channel", "https://t.me/+qF_xX_xJxn1mNTZl"),
    ("📢 Main", "https://t.me/+oO6iPYYsHuU4NmE1"),
    ("📢 Uncensored AI", "https://t.me/+sX2ryGchkr8wMmI1"),
    ("📢 Free Call Bomber", "https://t.me/+98gA5quyErViNjBl"),
    ("📢 CP", "https://t.me/+f3gS_FRIxAxiMTRl"),
    ("📢 Hentai Games", "https://t.me/+C60yPiwJyxpiMmI1"),
]


# -------- TOOLS --------
PAGE_1 = [
    ("🤫 Secrate Bot", "https://yuisaq.website/tg/bot?username=new_undre_sser_bot&ref_id=8193086064"),
    ("🖼 Undress Images", "https://t.me/Undress_imagesss_bot?start=7764057183"),
    ("🎥 Undress Videos", "https://t.me/Undress_videosss_bot?start=7764057183"),
    ("🎵 AI Music Creator", "https://t.me/AiMusicCreatorBot?start=Nzc2NDA1"),
    ("📧 Temp Mail", "https://t.me/OnlineEmailBot"),
]

PAGE_2 = [
    ("📱 Number Info", "https://t.me/get_info_number0_bot?start=EvsgKeW"),
    ("📱 Number Info 2", "https://t.me/divine_lookup_rbot?start=7764057183"),
    ("🔁 TG ➜ Number", "https://t.me/Tg_apna_haibot?start=_ref_PvIqV3_Wtxrsr"),
    ("🚗 Vehicle Info", "https://t.me/rtovehicledetailsbot?start=A7B9B57D"),
]

PAGE_3 = [
    ("🔍 Search Tool", "https://t.me/searchanything11_bot?start=REFA82748"),
    ("💻 Hacking", "https://t.me/KaIi_Linux_BOT?start=10c386b45482476a"),
    ("💻 Hacking 2", "https://t.me/Kali_Hacking_Bot?start=e1b5a0"),
    ("📸 Instagram Hack", "https://gplinks.co/JAEydxk"),
    ("📞 Fake Number", "https://t.me/Kali_Number_BOT?start=7764057183"),
]


# -------- KEYBOARDS --------
def join_buttons():
    kb = [[InlineKeyboardButton(n, url=l)] for n, l in CHANNELS]
    kb.append([InlineKeyboardButton("✅ Joined", callback_data="joined")])
    return InlineKeyboardMarkup(kb)


def page_buttons(page, page_no):
    kb = [[InlineKeyboardButton(n, url=l)] for n, l in page]
    nav = []
    if page_no > 1:
        nav.append(InlineKeyboardButton("◀️ Back", callback_data=f"page_{page_no-1}"))
    if page_no < 3:
        nav.append(InlineKeyboardButton("Next ▶️", callback_data=f"page_{page_no+1}"))
    kb.append(nav)
    return InlineKeyboardMarkup(kb)


# -------- HANDLERS --------
def start(update: Update, context: CallbackContext):
    add_user(update.effective_user.id)
    update.message.reply_text(
        "⚠️ Pehle saare channels join karo:",
        reply_markup=join_buttons()
    )


def callbacks(update: Update, context: CallbackContext):
    q = update.callback_query
    q.answer()

    if q.data == "joined":
        q.message.edit_text("📂 Tools Page 1", reply_markup=page_buttons(PAGE_1, 1))
    elif q.data == "page_2":
        q.message.edit_text("📂 Tools Page 2", reply_markup=page_buttons(PAGE_2, 2))
    elif q.data == "page_3":
        q.message.edit_text("📂 Tools Page 3", reply_markup=page_buttons(PAGE_3, 3))
    elif q.data == "page_1":
        q.message.edit_text("📂 Tools Page 1", reply_markup=page_buttons(PAGE_1, 1))


# -------- ADMIN --------
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
