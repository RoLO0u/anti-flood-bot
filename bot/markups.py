import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot import const

def captcha_inline() -> InlineKeyboardMarkup:
    random_capts = [(caption[0], caption[1]) for caption in list(const.OPTIONS)]
    random.shuffle(random_capts)
    listed_markup = [InlineKeyboardButton(text=capt[0], callback_data=f"spam{capt[1]}") for capt in random_capts]
    listed_markup = [listed_markup[:3], listed_markup[3:6], listed_markup[6:]]
    markup = InlineKeyboardMarkup(row_width=3, inline_keyboard=listed_markup)
    return markup