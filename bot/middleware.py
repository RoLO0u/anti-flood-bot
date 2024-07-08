from time import time as timeSeconds
from typing import Any, Awaitable, Callable, Dict, List

from aiogram.types import Message, BufferedInputFile
from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.fsm.storage.memory import MemoryStorage

from bot.markups import captcha_inline
from bot.images import create_captcha

class AntiFloodMiddleware(BaseMiddleware):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
    
    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data: Dict[str, Any]) -> Any:

        my_storage = data.get("storage")
        assert isinstance(my_storage, MemoryStorage)        

        user_id = str(event.from_user.id)
        user_storage: Dict[str, List[float | bool]] = await my_storage.get_data(user_id)

        time = timeSeconds()
        
        if not user_storage or not user_storage.get("data"):
            user_storage["data"] = [time, False, 0]
        elif user_storage["data"][1]:
            return
        elif user_storage["data"][0] + .5 > time: # new message sent less than in 0.5 sec
            image, answer, angle = create_captcha()
            user_storage["data"] = [time, True, angle]
            await my_storage.set_data(user_id, user_storage)
            await event.answer_photo(BufferedInputFile(image, "captcha"), "<PLACEHOLDER>", reply_markup=captcha_inline())
            return        
        else:
            user_storage["data"][0] = time

        await my_storage.set_data(user_id, user_storage)

        return await handler(event, data)