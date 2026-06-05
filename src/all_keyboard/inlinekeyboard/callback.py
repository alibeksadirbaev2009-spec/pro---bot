from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def good_place() -> InlineKeyboardMarkup:
    k = [
            [
        InlineKeyboardButton(text="The Angel Next Door Spoils Me Rotten", callback_data="1")
    ],
    [
        InlineKeyboardButton(text="Oshi no Ko", callback_data="2")
    ], 
    [
        InlineKeyboardButton(text="Your Name", callback_data="3")
    ],
    [
        InlineKeyboardButton(text="Solo Leviling", callback_data="4")
    ],
    [
        InlineKeyboardButton(text="Tamako Love story", callback_data="5")
    ],
    [
        InlineKeyboardButton(text="Darilng in the FranX", callback_data="6")
    ],
    [
        InlineKeyboardButton(text="Naruto", callback_data="7")
    ],
    [
        InlineKeyboardButton(text="Haikuu", callback_data="8")
    ],
    [
        InlineKeyboardButton(text="Basketball Kuroka", callback_data="9")
    ],
    [
        InlineKeyboardButton(text="Tokyo Revengers", callback_data="10")
    ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=k)
