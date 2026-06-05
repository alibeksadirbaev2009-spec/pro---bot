from aiogram import Bot
from src.config import settings

async def check_sub(bot: Bot, user_id: int) -> bool:
    member = await bot.get_chat_member(chat_id=settings.LINK, user_id=user_id)

    return member.status in ["member", "administrator", "creator"]