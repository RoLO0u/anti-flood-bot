from time import monotonic
from typing import Any, Awaitable, Callable, Dict

from aiogram.types import Message
from aiogram.dispatcher.middlewares.base import BaseMiddleware

from bot.markups import captcha_inline

class AntiFloodMiddleware(BaseMiddleware):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__()
    
    async def __call__(self, handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]], event: Message, data: Dict[str, Any]) -> Any:

        my_storage = data.get("dp").storage.storage

        user_id = str(event.from_user.id)
        time = monotonic()
        
        if not user_id in my_storage:
            my_storage[user_id] = [time, False]
            # print(1)
        elif my_storage[user_id][1]:
            # print(2)
            return
        elif my_storage[user_id][0] + .5 > time: # new message sent less than in 0.5 sec
            my_storage[user_id] = [time, True]
            await event.answer("You Sooooo Fast!!! Now You Should Make Captcha Below To Continue", reply_markup=captcha_inline())
            # print(3)
            return
        else:
            my_storage[user_id][0] = time

        return await handler(event, data)