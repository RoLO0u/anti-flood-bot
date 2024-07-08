from typing import Any
from time import monotonic

from aiogram import Router, F

from aiogram.types import CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage

router = Router()

@router.callback_query(F.data.startswith("spam"))
async def callback_query_handler(callback_query: CallbackQuery, storage: MemoryStorage) -> Any:

    user_id = str(callback_query.from_user.id)

    user_storage = await storage.get_data(user_id)

    if int(callback_query.data[4:]) == user_storage["data"][2]:
        time = monotonic()
        await callback_query.message.answer("<PLACEHOLDER>")
        user_storage["data"] = [time, False, 0]
        await storage.set_data(user_id, user_storage)
        await callback_query.message.delete()