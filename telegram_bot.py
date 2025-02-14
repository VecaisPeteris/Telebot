import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Iegūst API atslēgu no vides mainīgajiem
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Pārbauda, vai API atslēga ir pieejama
if not API_TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN nav atrasts vidē!")

# Izveido bota un dispatcher objektu
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Logu konfigurācija
logging.basicConfig(level=logging.INFO)

# Komanda /start
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Sveicināti! Šis ir rezervāciju bots krogam 'Vecais Pēteris'.\n"
                        "Rakstiet /reserve, lai veiktu rezervāciju.")

# Komanda /reserve (rezervācijas veikšanai)
@dp.message_handler(commands=["reserve"])
async def reserve_table(message: types.Message):
    await message.reply("Lūdzu, ierakstiet savu vārdu, datumu un cilvēku skaitu!\n\n"
                        "Piemēram: 'Jānis, 15. februāris, 4 cilvēki'")

# Nezināmu ziņojumu apstrāde
@dp.message_handler()
async def handle_message(message: types.Message):
    await message.reply("Lūdzu, izmantojiet komandu /reserve, lai veiktu rezervāciju.")

# Palaist bota darbību
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
