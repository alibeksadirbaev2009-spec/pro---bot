from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def anime_izlew() -> InlineKeyboardMarkup:
    btns = [
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
    return InlineKeyboardMarkup(inline_keyboard=btns)

def vip() -> InlineKeyboardMarkup:
    btns =[
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
    return InlineKeyboardMarkup(inline_keyboard= btns)