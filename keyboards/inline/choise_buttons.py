from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

share_image = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton(text="Хотите поделиться мемом со всеми?!", callback_data="share_content")
        ]
    ]
)

yes_or_no = InlineKeyboardMarkup(row_width=2)
yes = InlineKeyboardButton(text="Да", callback_data="Yes")
yes_or_no.insert(yes)
no = InlineKeyboardButton(text="Нет", callback_data="No")
yes_or_no.insert(no)
