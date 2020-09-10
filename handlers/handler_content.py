from aiogram.types import Message

from loader import dp, bot

from config import FOLDER_PICTURES

from keyboards.inline.choise_buttons import share_image

from services.datetime import date_time_now
from services.text_on_the_pictures import TransformImage


@dp.message_handler(content_types=['photo'])
async def handle_start_message(message: Message):
    path_to_image = FOLDER_PICTURES + date_time_now() + str(message.from_user.id) + '.jpg'
    await message.photo[-1].download(path_to_image)
    transform_Image = TransformImage(path_to_image)
    await bot.send_photo(message.from_user.id, open(transform_Image.transform_image(), 'rb'))
    await message.answer(text="Сделайте выбор!", reply_markup=share_image)
