from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command


router = Router()

@router.message(Command("start"))
async def start(message: Message):
    await message.answer("Try To Flood Me!")