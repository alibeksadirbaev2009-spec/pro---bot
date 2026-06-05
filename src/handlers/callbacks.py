from aiogram import F, Router
from aiogram.types import (
    CallbackQuery, 
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup)
from src.all_keyboard.inlinekeyboard.callback import good_place
from src.all_keyboard.keyboard.back import back
from src.all_keyboard.inlinekeyboard.text import anime_izlew
from aiogram import Bot
from src.check_sub import check_sub
from src.config import settings


router = Router()


# name
@router.callback_query(F.data == "at")
async def at(call: CallbackQuery):
    await call.message.answer(f"Anime atin kiritin':")
    await call.answer()


# code
@router.callback_query(F.data == "kod")
async def kod(call: CallbackQuery):
    await call.message.answer(f"Anime kodin kiritin':")
    await call.answer()


# all
@router.callback_query(F.data == "ha'mme")
async def all(call: CallbackQuery):
    await call.message.answer(f"Ele-beri iske tu'speydi !!!:")
    await call.answer()

# top
@router.callback_query(F.data == "top")
async def top(call: CallbackQuery):
    btns = good_place()
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
""", reply_markup=btns)

    await call.answer()



# @router.callback_query(F.data == "The Angel Next Door Spoils Me Rotten")
# async def first(call: CallbackQuery):



# one month
@router.callback_query(F.data == "1ay")
async def one(call: CallbackQuery):
    btns = back()
    await call.message.answer(f"""
💎 1 ayliq VIP

💰 To'lem summasi: 9,000 so'm
⏱️ Mu'ddeti: 30 kun

💳 To'lem kartasi:
4916 9903 2086 1561

📸 To'lemdi a'melge asirig'andan keyin, chek su'wretin jiberin'.
                              
Admin tasdiqlag'annan keyin VIP avtomatik iske qosiladi.
""", reply_markup=btns)
    await call.answer()


# 3 months
@router.callback_query(F.data == "3ay")
async def three(call: CallbackQuery):
    btns = back()
    await call.message.answer(f"""
💎 3 ayliq VIP

💰 To'lem summasi: 40,000 so'm
⏱️ Mu'ddeti: 90 kun

💳 To'lem kartasi:
4916 9903 2086 1561

📸 To'lemdi a'melge asirig'andan keyin, chek su'wretin jiberin'.
                              
Admin tasdiqlag'annan keyin VIP avtomatik iske qosiladi.
""", reply_markup=btns)
    await call.answer()


# 6 months
@router.callback_query(F.data == "6ay")
async def six(call: CallbackQuery):
    btns = back()
    await call.message.answer(f"""
💎 6 ayliq VIP

💰 To'lem summasi: 75,000 so'm
⏱️ Mu'ddeti: 180 kun

💳 To'lem kartasi:
4916 9903 2086 1561

📸 To'lemdi a'melge asirig'andan keyin, chek su'wretin jiberin'.
                              
Admin tasdiqlag'annan keyin VIP avtomatik iske qosiladi.
""", reply_markup=btns)
    await call.answer()


# Artqa qaytiw anime an arqali izlewden
@router.callback_query(F.data == "back")
async def artqa(call: CallbackQuery):
    btns = anime_izlew()
    await call.message.answer(f"Artqa qayttin'iz!", reply_markup=btns)


# Ju'klew
@router.callback_query(F.data == "Ju'klew")
async def get_anime(call: CallbackQuery, bot: Bot):
    is_sub = await check_sub(bot, call.from_user.id)

    if not is_sub:
        await call.message.answer("❗Aldin kanalg'a abuna boling: " + settings.LINK)
        await call.answer()
        return

    await call.message.answer("Usi kanaldan tabasiz: https://t.me/many_cool_animies")

    await call.answer()
