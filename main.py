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

    logging.basicConfig(level=logging.INFO)

    BOT_TOKEN = os.getenv("BOT_TOKEN")
    assert BOT_TOKEN

    bot = Bot(BOT_TOKEN)

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    dp["dp"] = dp
    dp["storage"] = storage
    dp["bot"] = bot
    dp["bot_id"] = bot.id

    dp.message.filter(F.chat.type == "private")

    dp.include_router(commands.router)
    dp.include_router(text.router)
    dp.include_router(inline.router)

    dp.message.middleware(middleware.AntiFloodMiddleware())

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(run())