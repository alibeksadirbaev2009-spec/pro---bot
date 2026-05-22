from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import ( 
    Message, 
    KeyboardButton, 
    ReplyKeyboardMarkup)

router = Router()

# start
@router.message(CommandStart())
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
            KeyboardButton(text="👤Profile")
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=k, resize_keyboard=True)
    await message.answer(f"Sa'lem, {u.first_name}  Anime kodini kiriting...", reply_markup=mark)
