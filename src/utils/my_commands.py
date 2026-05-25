from aiogram.types import BotCommand

def my_commands() -> list[BotCommand]:
    com = [
        BotCommand(command="/start", description="Botti iske qosiw")
    ]

    return com 