from typing import Dict, Any
from time import monotonic

from aiogram import Router, F

from aiogram.types import CallbackQuery
from aiogram.filters.callback_data import CallbackData
from aiogram.fsm.storage.memory import MemoryStorage

router = Router()

@router.callback_query(F.data == "1")
async def callback_query_handler(callback_query: CallbackQuery, storage: MemoryStorage) -> Any:

    user_id = str(callback_query.from_user.id)
    time = monotonic()

    await callback_query.message.answer("YAY!!!! You Are Sooooooooo Good")
    storage.storage[user_id] = [time, False]
    await callback_query.message.delete()