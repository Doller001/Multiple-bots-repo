from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CallbackContext
from database import add_user

# 🔐 JOIN FIRST CHANNELS
CHANNELS = [
    ("📢 BackUp Channel", "https://t.me/+qF_xX_xJxn1mNTZl"),
    ("🔥 Main", "https://t.me/+oO6iPYYsHuU4NmE1"),
    ("🤖 Uncensored AI", "https://t.me/+sX2ryGchkr8wMmI1"),
    ("📞 Free Call Bomber", "https://t.me/+98gA5quyErViNjBl"),
    ("🔞 CP", "https://t.me/+f3gS_FRIxAxiMTRl"),
    ("🎮 Hentai Games", "https://t.me/+C60yPiwJyxpiMmI1"),
]

PAGE_1 = [
    ("🤫 Secrate Bot", "https://yuisaq.website/tg/bot?username=new_undre_sser_bot&ref_id=8193086064"),
    ("🖼️ Undress Images", "https://t.me/Undress_imagesss_bot?start=7764057183"),
    ("🎥 Undress Videos", "https://t.me/Undress_videosss_bot?start=7764057183"),
    ("🎵 AI Music Creator", "https://t.me/AiMusicCreatorBot?start=Nzc2NDA1"),
    ("📧 Temp Mail", "https://t.me/OnlineEmailBot"),
]

PAGE_2 = [
    ("📱 Number Info", "https://t.me/get_info_number0_bot?start=EvsgKeW"),
    ("📞 Number Info 2", "https://t.me/divine_lookup_rbot?start=7764057183"),
    ("🔁 TG ➜ Number", "https://t.me/Tg_apna_haibot?start=_ref_petGrMcsK_zhtQD2DsP"),
    ("🚗 Vehicle Info", "https://t.me/rtovehicledetailsbot?start=A7B9B57D"),
]

PAGE_3 = [
    ("🔎 Search Tool", "https://t.me/searchanything11_bot?start=REFA82748"),
    ("💻 Hacking Tool", "https://t.me/KaIi_Linux_BOT?start=10c386b45482476a"),
    ("💀 Hacking 2", "https://t.me/Kali_Hacking_Bot?start=e1b5a0"),
    ("📸 Instagram Hack", "https://gplinks.co/JAEydxk"),
    ("📟 Fake Number", "https://t.me/Kali_Number_BOT?start=7764057183"),
]

def join_keyboard():
    kb = [[InlineKeyboardButton(n, url=l)] for n, l in CHANNELS]
    kb.append([InlineKeyboardButton("✅ Joined", callback_data="joined")])
    return InlineKeyboardMarkup(kb)

def page_keyboard(page, no):
    kb = [[InlineKeyboardButton(n, url=l)] for n, l in page]
    nav = []
    if no > 1:
        nav.append(InlineKeyboardButton("⬅ Back", callback_data=f"page_{no-1}"))
    if no < 3:
        nav.append(InlineKeyboardButton("Next ➡", callback_data=f"page_{no+1}"))
    kb.append(nav)
    return InlineKeyboardMarkup(kb)

def start(update: Update, context: CallbackContext):
    add_user(update.effective_user.id)
    update.message.reply_text("⚠ Join all channels first:", reply_markup=join_keyboard())

def callbacks(update: Update, context: CallbackContext):
    q = update.callback_query
    q.answer()

    if q.data == "joined":
        q.message.edit_text("📂 Tools Page 1", reply_markup=page_keyboard(PAGE_1, 1))
    elif q.data == "page_2":
        q.message.edit_text("📂 Tools Page 2", reply_markup=page_keyboard(PAGE_2, 2))
    elif q.data == "page_3":
        q.message.edit_text("📂 Tools Page 3", reply_markup=page_keyboard(PAGE_3, 3))
    elif q.data == "page_1":
        q.message.edit_text("📂 Tools Page 1", reply_markup=page_keyboard(PAGE_1, 1))
