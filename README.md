# Flood captcha bot

Simple telegram bot example written using aiogram with captcha to stop spam.

## Environment

To use this example set `.env` file with:

`BOT_TOKEN` set to token given to the bot by [@BotFather](https://t.me/BotFather)

## Storage

For this example bot uses MemoryStorage which is **not** recommended for use in production

> Learn more [about storages in aiogram](https://docs.aiogram.dev/en/latest/dispatcher/finite_state_machine/storages.html)

## Configuration

In [const.py](bot/const.py) file you can find a few options to configure this bot

* `IMAGES` list of images listed in `IMAGES_ROUTE` folder. Images need to be facing right and should have transparent background.
* `IMAGES_ROUTE` route to the folder with images.
* `WIDTH` & `HEIGHT` width and height of the captcha image
* `BACKGROUND` color of the captcha background
* `X_OFFSET` & `Y_OFFSET` offset in which captcha can't be put
* `ROTATE_OFFSET` random rotation adjustments by `n` degrees
* `DELAY` time after which user is allowed to send next message in seconds
* `OPTIONS` tuple of options user will be given after captcha is triggered. First in a tuple is a caption and second positions is meant for degrees or `None` which will be skipped

## Captcha example

<img src="readmefiles/example.png" alt="example" width=400>

Currently this captcha is being used by [@paces_bot](https://t.me/paces_bot)

## Using

* aiogram 3.13.1
* python 3.11.8 (recommended)