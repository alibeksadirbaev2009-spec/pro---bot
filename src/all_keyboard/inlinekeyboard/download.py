from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def download() -> InlineKeyboardMarkup:
    see = [
        [
            InlineKeyboardButton(text='Juklep aliw', callback_data="Ju'klew")
        ], 
        [
            InlineKeyboardButton(text='🔙Artqa', callback_data="back")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=see) 