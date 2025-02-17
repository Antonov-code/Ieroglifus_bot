from aiogram.types import Message
from aiogram.filters import Command
from aiogram import Router
from keyboards.keyboards import keyboard_help
from keyboards.inlineKeyboards import keyboard_level

router = Router()

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Тут будут полезные команды', reply_markup=keyboard_level)