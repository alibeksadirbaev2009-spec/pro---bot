from aiogram import F, Router
from aiogram.types import (
    CallbackQuery, 
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup)


router = Router()

@router.callback_query(F.data == "at")
async def at(call: CallbackQuery):
    await call.message.answer(f"Anime atin kiritin':")
    await call.answer()

@router.callback_query(F.data == "kod")
async def kod(call: CallbackQuery):
    await call.message.answer(f"Anime kodin kiritin':")
    await call.answer()

@router.callback_query(F.data == "ha'mme")
async def all(call: CallbackQuery):
    await call.message.answer(f"Ele-beri iske tu'speydi !!!:")
    await call.answer()


@router.callback_query(F.data == "top")
async def top(call: CallbackQuery):
    
    l = [
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
    mark = InlineKeyboardMarkup(inline_keyboard=l)
    await call.message.answer(f"""
🔝 En' ko'p ko'rilgen animeler (Top 10):
1.The Angel Next Door Spoils Me Rotten  — 👁 5210 ma'rte ko'rilgen
2.Oshi no Ko — 👁 4872 ma'rte ko'rilgen
3.Your Name — 👁 4631 ma'rte ko'rilgen
4.Solo Leviling — 👁 4187 ma'rte ko'rilgen
5.Tamako Love story — 👁 3924 ma'rte ko'rilgen
6.Darilng in the FranX — 👁 3816 ma'rte ko'rilgen
7.Naruto — 👁 3504 ma'rte ko'rilgen
8.Haikuu — 👁 3180 ma'rte ko'rilgen
9.Basketball Kuroka — 👁 2975 ma'rte ko'rilgen
10.Tokyo Revengers — 👁 2843 ma'rte ko'rilgen
""", reply_markup=mark)

    await call.answer()

# @router.callback_query(F.data == "The Angel Next Door Spoils Me Rotten")
# async def first(call: CallbackQuery):




@router.callback_query(F.data == "1ay")
async def one(call: CallbackQuery):
    m =[
        [
            KeyboardButton(text="🔙Artqa")
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=m, resize_keyboard=True)
    await call.message.answer(f"""
💎 1 ayliq VIP

💰 To'lem summasi: 9,000 so'm
⏱️ Mu'ddeti: 30 kun

💳 To'lem kartasi:
4916 9903 2086 1561

📸 To'lemdi a'melge asirig'andan keyin, chek su'wretin jiberin'.
                              
Admin tasdiqlag'annan keyin VIP avtomatik iske qosiladi.
""", reply_markup=mark)
    await call.answer()

@router.callback_query(F.data == "3ay")
async def three(call: CallbackQuery):
    m =[
        [
            KeyboardButton(text="🔙Artqa")
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=m, resize_keyboard=True)
    await call.message.answer(f"""
💎 3 ayliq VIP

💰 To'lem summasi: 40,000 so'm
⏱️ Mu'ddeti: 90 kun

💳 To'lem kartasi:
4916 9903 2086 1561

📸 To'lemdi a'melge asirig'andan keyin, chek su'wretin jiberin'.
                              
Admin tasdiqlag'annan keyin VIP avtomatik iske qosiladi.
""", reply_markup=mark)
    await call.answer()

@router.callback_query(F.data == "6ay")
async def six(call: CallbackQuery):
    m =[
        [
            KeyboardButton(text="🔙Artqa")
        ]
    ]
    mark = ReplyKeyboardMarkup(keyboard=m, resize_keyboard=True)
    await call.message.answer(f"""
💎 6 ayliq VIP

💰 To'lem summasi: 75,000 so'm
⏱️ Mu'ddeti: 180 kun

💳 To'lem kartasi:
4916 9903 2086 1561

📸 To'lemdi a'melge asirig'andan keyin, chek su'wretin jiberin'.
                              
Admin tasdiqlag'annan keyin VIP avtomatik iske qosiladi.
""", reply_markup=mark)
    await call.answer()
