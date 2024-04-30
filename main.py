import asyncio
import logging
import os

from aiogram import Dispatcher, Bot, F
from aiogram.fsm.storage.memory import MemoryStorage

from bot import middleware

from bot.handlers import commands, text, inline

from bot.run import Environment
Environment().load_env()

async def run():

    logging.basicConfig(level=logging.WARNING)

    bot = Bot(os.getenv("BOT_TOKEN"))

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    dp["dp"] = dp
    dp["storage"] = storage

    dp.message.filter(F.chat.type == "private")

    # Some routers here
    dp.include_router(commands.router)
    dp.include_router(text.router)
    dp.include_router(inline.router)

    # Middleware here
    dp.message.middleware(middleware.AntiFloodMiddleware())

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(run())