from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram import Router

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет')