from typing import Any
from time import monotonic

from aiogram import Router, F

from aiogram.types import CallbackQuery, Message
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.base import StorageKey

router = Router()

@router.callback_query(F.data.startswith("spam"))
async def callback_query_handler(callback_query: CallbackQuery, storage: MemoryStorage, bot_id: int) -> Any:

    message = callback_query.message
    assert isinstance(message, Message)

    key = StorageKey(
        bot_id=bot_id,
        chat_id=message.chat.id,
        user_id=callback_query.from_user.id
    )
    user_storage = await storage.get_data(key)
    print(user_storage, key)

    assert callback_query and callback_query.data
    if int(callback_query.data[4:]) == user_storage["data"][2]:
        time = monotonic()


        await message.answer("<PLACEHOLDER>")
        user_storage["data"] = [time, False, 0]
        await storage.set_data(key, user_storage)
        await message.delete()