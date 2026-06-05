from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.all_keyboard.keyboard.start import baslaw

router = Router()


# start
@router.message(CommandStart())
async def start(message: Message):
    u = message.from_user
    btns = baslaw()
    await message.answer(f"Sa'lem, {u.first_name}  Kerekli bo'limdi saylan'... ", reply_markup=btns)