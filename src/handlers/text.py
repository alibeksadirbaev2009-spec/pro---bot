from aiogram import F, Router
from aiogram.types import Message
from aiogram.types import ( 
    Message, 
    KeyboardButton, 
    ReplyKeyboardMarkup, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    WebAppInfo)

router = Router()


# 🔎Anime izlew
@router.message(F.text == "🔎Anime izlew")
async def text(message: Message):
    l = [
        [
            InlineKeyboardButton(text="🔎At boyinsha izlew", callback_data="at")
        ],
        [
            InlineKeyboardButton(text="🔎Kod boyinsha izlew", callback_data="kod")
        ],
        [
            InlineKeyboardButton(text="🔎Ha'mme animeler", callback_data="ha'mme")
        ],
        [
            InlineKeyboardButton(text="🔎En' ko'p ko'rilgen animeler", callback_data="top")
        ]
    ]
    mark = InlineKeyboardMarkup(inline_keyboard=l)
    await message.answer("Quydag'lardan birin tan'lan'", reply_markup=mark)

# 📚Qollanba
@router.message(F.text == "📚Qollanba")
async def text(message: Message):
    await message.answer(f"""📖 Botdan foydalanish qo‘llanmasi

🔎 Anime qidirish
1️⃣ Menyudan 🔎 Anime qidirish tugmasini bosing.
2️⃣ Sizda 3 ta variant bor:

• 📂 Barcha animelar – botdagi barcha animelar ro‘yxatini ko‘rasiz.
• 🔎  Nom orqali izlash – anime nomini yozib qidirishingiz mumkin.
•🔢 Kod orqali izlash – anime kodini yozib qidirishingiz mumkin.

3️⃣ Kerakli animeni topganingizdan keyin bot sizga uni yuboradi.

📩 Admin bilan bog‘lanish
Agar savol yoki muammo bo‘lsa, menyudan 👨‍💻 Admin bilan bog‘lanish tugmasini bosib yozishingiz mumkin.

✅ Botdan foydalanish juda oddiy:
Anime qidirish → Kerakli animeni kodini yoki nomini yuboring→ Tomosha qilish

Bot yaratuvchisi: @a1ibek2""")
    
# 💵Reklama ha'm hamiyliq
@router.message(F.text == "💵Reklama ha'm hamiyliq")
async def text(message: Message):
    k = [
        [
            KeyboardButton(text="❌Biykar etiw")
        ],
        [
            KeyboardButton(text="Kontact jiberiw", request_contact=True)
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=k, resize_keyboard=True)
    await message.answer(f"""
Botqa kontakt nomerinizdi qaldirin adminler o'zi qabar jiberedi!
Iltimas adminlerdi bolar bolmas na'rseler menen waqtin alman'. 
Eger sonday jag'day bolsa BLOK!!!
""", reply_markup=mark)

@router.message(F.text == "❌Biykar etiw")
async def main(message: Message):
    k = [
        [
            KeyboardButton(text="🔎Anime izlew")
        ],
        [
            KeyboardButton(text="📚Qollanba"),
            KeyboardButton(text="💵Reklama ha'm hamiyliq")
        ],
        [
            KeyboardButton(text="💎Vip satip aliw"),
            KeyboardButton(text="👤Profile")
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=k, resize_keyboard=True)
    await message.answer(f"🏠Bas menug'a qayttin'iz:", reply_markup=mark)

# 💎Vip satip aliw
@router.message(F.text == "💎Vip satip aliw")
async def text(message: Message):
    m = [
        [
            InlineKeyboardButton(text="💎1 ayliq - 9,000 sum", callback_data="1ay")
        ],
        [
            InlineKeyboardButton(text="💎3 ayliq - 40,000 sum", callback_data="3ay")
        ],
        [
            InlineKeyboardButton(text="💎6 ayliq - 75,000 sum", callback_data="6ay")
        ]
    ]

    mark = InlineKeyboardMarkup(inline_keyboard=m)
    await message.answer("""
    💎 VIP TARIFLER:
    VIP arqali ma'jbu'riy obunalarsiz paydlanasiz.
    Kerekli tarifti tan'lan':
    """,
    reply_markup=mark)

@router.message(F.text == "🔙Artqa")
async def main(message:Message):
    k = [
        [
            KeyboardButton(text="🔎Anime izlew")
        ],
        [
            KeyboardButton(text="📚Qollanba"),
            KeyboardButton(text="💵Reklama ha'm hamiyliq")
        ],
        [
            KeyboardButton(text="💎Vip satip aliw"),
            KeyboardButton(text="👤Profile")
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=k, resize_keyboard=True)
    await message.answer(f"🏠Bas menug'a qayttin'iz:", reply_markup=mark)

# 👤Profile
@router.message(F.text == "👤Profile")
async def text(message: Message):
    await message.answer(f"Waqtinshaliq jabiq!!!")

# text
@router.message(F.text)
async def text(message:Message):
    await message.answer(f"❌ Botqa {message.text} komandasi tanis emes")