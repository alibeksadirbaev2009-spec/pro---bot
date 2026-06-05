from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def back() -> ReplyKeyboardMarkup:
    m = [
        [
            KeyboardButton(text="🔙Artqa")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=m, resize_keyboard=True)