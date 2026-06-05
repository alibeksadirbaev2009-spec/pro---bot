from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def hamiyliq() -> ReplyKeyboardMarkup:
    btns =[
        [
            KeyboardButton(text="Kontact jiberiw", request_contact=True)
        ],
        [
            KeyboardButton(text="❌Biykar etiw")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=btns, resize_keyboard=True)
