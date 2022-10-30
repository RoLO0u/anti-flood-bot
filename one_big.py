import random
import asyncio
import logging
import os

from aiogram import Dispatcher, types, Bot, F, Router
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import CallbackQuery, Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.filters import Command

from typing import Any, Awaitable, Callable, Dict
from time import monotonic

class AntiFloodMiddleware(BaseMiddleware):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
    
    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data: Dict[str, Any]) -> Any:

        print(data)

        return await handler(event, data)

CAPTS = {"Click Me": "1", "-": "0", "Don't": "0", "NO!!!": "0", \
    "Nine!": "0", "HOHO": "0"}

def inline() -> InlineKeyboardMarkup:
    random_capts = [(key, CAPTS[key]) for key in list(CAPTS.keys())]
    random.shuffle(random_capts)
    random_capts = dict(random_capts)
    listed_markup = [InlineKeyboardButton(text=capt, callback_data=random_capts[capt]) for capt in random_capts]
    listed_markup = [listed_markup[:3], listed_markup[3:]]
    markup = InlineKeyboardMarkup(row_width=3, inline_keyboard=listed_markup)
    return markup

inline_router = Router()

@inline_router.callback_query(F.data == "1")
async def callback_query_handler(callback_query: CallbackQuery) -> Any:

    await callback_query.message.answer("1 pressed")

text_router = Router()

@text_router.message(F.text)
async def start(message: Message):
    await message.answer("Text here!", reply_markup=inline())

commands_router = Router()

@commands_router.message(Command("start"))
async def start(message: Message):
    await message.answer("I here!")

async def run():

    logging.basicConfig(level=logging.INFO)

    bot = Bot(os.getenv("BOT_TOKEN"))

    storage = MemoryStorage()

    dp = Dispatcher(storage=storage)

    dp["dp"] = dp

    dp.message.filter(F.chat.type == "private")

    dp.include_router(commands_router)
    dp.include_router(text_router)
    dp.include_router(inline_router)

    dp.message.middleware(AntiFloodMiddleware())

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

if __name__ == "__main__":
    asyncio.run(run())