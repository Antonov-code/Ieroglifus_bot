from aiogram.types import (
        InlineKeyboardMarkup,
        InlineKeyboardButton
    )


from aiogram.types import (
        ReplyKeyboardMarkup,
        KeyboardButton,
        InlineKeyboardMarkup,
        InlineKeyboardButton
    )


keyboard_level = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="HSK-1", callback_data="hsk1")],
    [InlineKeyboardButton(text="HSK-2", callback_data="hsk2")],
    [InlineKeyboardButton(text="HSK-3", callback_data="hsk3")]
])