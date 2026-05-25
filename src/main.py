# aiogram 3.x
import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from .config import settigns
from .handlers import routers
from .utils.my_commands import my_commands

bot = Bot(settigns.TOKEN)
dp = Dispatcher()


dp.include_routers(routers)




# bul bot iske qosilganda info aliw yamasa isletillgen de
async def main():
    await bot.set_my_commands(my_commands())
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":  
    asyncio.run(main=main())

    # bot file bo'liw knopkiler, tas qag'az qayshi    random