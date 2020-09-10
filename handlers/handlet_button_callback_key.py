
from aiogram.types import CallbackQuery

from config import CHANNEL_PUBLIC_ID
from keyboards.inline.choise_buttons import yes_or_no
from loader import dp, bot


@dp.callback_query_handler(text_contains='share_content')
async def handle_callback(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text="Мем будет доступен всем пользователям бота. Поделиться?", reply_markup=yes_or_no)


@dp.callback_query_handler(text_contains='Yes')
async def handle_callback_yes(call: CallbackQuery):
    await call.message.delete()
    await bot.send_message(CHANNEL_PUBLIC_ID,  "{0} отправил нам крутой мем!".format(call.message.chat.first_name),
                           reply_to_message_id=call.message.message_id-2)
    await call.message.answer(text="Спасибо, что поделились!! Картинка отправлена в общий чат.")


@dp.callback_query_handler(text_contains='No')
async def handle_callback_yes(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=None)
    await call.message.answer(text="Не поделились :(")
