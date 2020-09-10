from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from loader import dp


@dp.message_handler(Command('start'))
async def handle_start_message(message: Message):
    await message.answer(text="Здарова, бродяга! Ты мне фотку, я тебе мем.")


@dp.message_handler()
async def handle_start_message(message: Message):
    await message.answer(text='Пришли мне фото!')


