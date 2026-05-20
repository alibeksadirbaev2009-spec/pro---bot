import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import ( 
    Message, 
    KeyboardButton, 
    ReplyKeyboardMarkup, 
    ReplyKeyboardRemove, 
    InlineKeyboardButton, 
    InlineKeyboardMarkup, 
    WebAppInfo
    )
from .config import TOKEN

bot = Bot(TOKEN)
dp = Dispatcher()

# start
@dp.message(CommandStart())
async def start(message: Message):
    u = message.from_user
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
            KeyboardButton(text="👤 Profile")
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=k, resize_keyboard=True)
    await message.answer(f"Sa'lem, {u.first_name}  Anime kodini kiriting...", reply_markup=mark)


@dp.message(F.text == "🔎Anime izlew")
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
# ishin kiritiw kk

@dp.message(F.text == "📚Qollanba")
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

@dp.message(F.text == "💵Reklama ha'm hamiyliq")
async def text(message: Message):
    await message.answer(f"Waqtinshaliq jabiq!!!")


@dp.message(F.text == "💎Vip satip aliw")
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

@dp.message(F.text == "👤 Profile")
async def text(message: Message):
    await message.answer(f"Waqtinshaliq jabiq!!!")


@dp.message(F.text)
async def text(message:Message):
    await message.answer(f"❌ Botqa {message.text} komandasi tanis emes")

# bul bot iske qosilganda info aliw yamasa isletillgen de
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":  
    asyncio.run(main=main())