from aiogram import F, Router
from aiogram.types import Message

router = Router()

@router.message(F.contact)
async def get_contact(message: Message):
    await message.answer("Kontact qabil qilindi!")