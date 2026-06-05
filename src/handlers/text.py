from aiogram import F, Router
from aiogram.types import Message
from src.all_keyboard.inlinekeyboard.text import anime_izlew, vip
from src.all_keyboard.keyboard.text import hamiyliq
from src.all_keyboard.keyboard.start import baslaw
from src.all_keyboard.inlinekeyboard.download import download
router = Router()


# 🔎Anime izlew
@router.message(F.text == "🔎Anime izlew")
async def text(message: Message):
    btns = anime_izlew()
    await message.answer("Quydag'lardan birin tan'lan'", reply_markup=btns)


# 📚Qollanba
@router.message(F.text == "📚Qollanba")
async def text(message: Message):
    await message.answer(f"""📖 Botdan foydalanish qo‘llanmasi

🔎 Anime qidirish
1️⃣ Menyudan 🔎 Anime qidirish tugmasini bosing.
2️⃣ Sizda 3 ta variant bor:

• 📂 Barcha animelar – botdagi barcha animelar ro‘yxatini ko‘rasiz.
• 🔎  Nom orqali izlash – anime nomini yozib qidirishingiz mumkin.
•🔢 Kod orqali izlash – anime kodini yozib qidirishingiz mumkin.

3️⃣ Kerakli animeni topganingizdan keyin bot sizga uni yuboradi.

📩 Admin bilan bog‘lanish
Agar savol yoki muammo bo‘lsa, menyudan 👨‍💻 Admin bilan bog‘lanish tugmasini bosib yozishingiz mumkin.

✅ Botdan foydalanish juda oddiy:
Anime qidirish → Kerakli animeni kodini yoki nomini yuboring→ Tomosha qilish

Bot yaratuvchisi: @a1ibek2""")


# 💵Reklama ha'm hamiyliq
@router.message(F.text == "💵Reklama ha'm hamiyliq")
async def text(message: Message):
    btns = hamiyliq()
    await message.answer(f"""
Botqa kontakt nomerinizdi qaldirin adminler o'zi qabar jiberedi!
Iltimas adminlerdi bolar bolmas na'rseler menen waqtin alman'. 
Eger sonday jag'day bolsa BLOK!!!
""", reply_markup=btns)


# 🏠main
@router.message(F.text == "❌Biykar etiw")
async def main(message: Message):
    btns = baslaw()
    await message.answer(f"🏠Bas menug'a qayttin'iz:", reply_markup=btns)


# 💎Vip satip aliw
@router.message(F.text == "💎Vip satip aliw")
async def text(message: Message):
    btns = vip()
    await message.answer("💎 VIP TARIFLER:\nVIP arqali ma'jbu'riy obunalarsiz paydlanasiz.\nKerekli tarifti tan'lan':",
    reply_markup=btns)


# 🔙back
@router.message(F.text == "🔙Artqa")
async def main(message:Message):
    btn = baslaw()
    await message.answer(f"🏠Bas menug'a qayttin'iz:", reply_markup=btn)


# 👤Profile
@router.message(F.text == "👤Profile")
async def text(message: Message):
    await message.answer(f"Waqtinshaliq jabiq!!!")


# anime - 1
@router.message(F.text == "Yolg'izlikda daraja ko'tarish")
async def text(message: Message):
    btns = download()
    await message.answer(f"""
🟦 1-fasl
📅 Chiqqan: 2024-yil (yanvar–mart)
🎬 Qism: 12 ta episode
📖 Hikoya: Jin-Woo zaif hunterdan “system” olishi va kuchayishni boshlashi
🟨 2-fasl
📅 Chiqqan: 2025-yil
🎬 Qism: 13 ta episode
📖 Hikoya: Jin-Woo yanada kuchli bo‘lib, katta janglar boshlanadi
📌 Umumiy
🧩 Hozircha: 2 fasl
🎯 Har fasl: ~12–13 qism
⚔️ Janr: Action, Fantasy, Level-up system
""", reply_markup=btns)
# text
@router.message(F.text)
async def text(message:Message):
    await message.answer(f"❌ Botqa {message.text} komandasi tanis emes")