from aiogram.types import (
        ReplyKeyboardMarkup,
        KeyboardButton,
    )


keyboard_help = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="/start")],
        [
            KeyboardButton(text="/level"),
            KeyboardButton(text="/statistic")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='выберите пункт меню'
)



