import random

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot.const import CAPTCHA_CAPTIONS

def captcha_inline() -> InlineKeyboardMarkup:
    random_capts = [(key, CAPTCHA_CAPTIONS[key]) for key in list(CAPTCHA_CAPTIONS.keys())]
    random.shuffle(random_capts)
    random_capts = dict(random_capts)
    listed_markup = [InlineKeyboardButton(text=capt, callback_data=random_capts[capt]) for capt in random_capts]
    listed_markup = [listed_markup[:3], listed_markup[3:]]
    markup = InlineKeyboardMarkup(row_width=3, inline_keyboard=listed_markup)
    return markup