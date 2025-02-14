
import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

# Telegram API atslēga no vides mainīgajiem
API_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# Izveido bota un dispatcher objektu
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Logu konfigurācija
logging.basicConfig(level=logging.INFO)

# Komanda /start
@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Sveicināti! Šis ir rezervāciju bots krogam 'Vecais Pēteris'. Rakstiet /reserve lai veiktu rezervāciju.")

# Komanda /reserve (rezervācijas veikšanai)
@dp.message_handler(commands=["reserve"])
async def reserve_table(message: types.Message):
    await message.reply("Lūdzu, ierakstiet savu vārdu, datumu un cilvēku skaitu!")

# Nezināmu ziņojumu apstrāde
@dp.message_handler()
async def echo(message: types.Message):
    await message.reply("Lūdzu, izmantojiet komandu /reserve lai veiktu rezervāciju.")

# Palaist bota darbību
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
