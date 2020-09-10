import os

from aiogram import Bot, Dispatcher, types

from config import TOKEN, FOLDER_PICTURES, DATA_FOLDER

bot = Bot(token=TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)

try:
    os.mkdir(FOLDER_PICTURES)
except Exception:
    pass
