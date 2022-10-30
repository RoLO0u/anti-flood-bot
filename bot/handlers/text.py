from aiogram import Router, F
from aiogram.types import Message

router = Router()

@router.message(F.text)
async def start(message: Message):
    await message.answer("Not Enough or Too Slow!")