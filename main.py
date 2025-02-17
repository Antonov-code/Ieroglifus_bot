import asyncio
from configparser import ConfigParser
from aiogram import Bot, Dispatcher #, types
# from aiogram.types import Message
# from aiogram.filters import Command

from handlers.start import router as start_router
from handlers.help import router as help_router


config = ConfigParser()
config.read('config.ini')
BOT_TOKEN = config.get('DEFAULT', 'bot_token')



async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)
    dp.include_router(help_router)
    await dp.start_polling(bot)
    
    
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('bot stopped')