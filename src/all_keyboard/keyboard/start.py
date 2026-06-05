from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

def baslaw() -> ReplyKeyboardMarkup:
    main = [
        [
            KeyboardButton(text="🔎Anime izlew")
        ],
        [
            KeyboardButton(text="📚Qollanba"),
            KeyboardButton(text="💵Reklama ha'm hamiyliq")
        ],
        [
            KeyboardButton(text="💎Vip satip aliw"),
            KeyboardButton(text="👤Profile")
        ]
    ]
    return ReplyKeyboardMarkup(keyboard=main, resize_keyboard=True)