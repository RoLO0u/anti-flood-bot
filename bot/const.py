IMAGES = [
    "backhand-index-pointing-right.png", 
    "palm-down-hand.png",
    "rightwards-hand.png"
]

IMAGES_ROUTE = "bot/img/"

WIDTH, HEIGHT= 800, 400

BACKGROUND = 0xFF # white by default

X_OFFSET, Y_OFFSET = 100, 100

ROTATE_OFFSET = 5 # random degrees

DELAY = .5 # time after which the captcha is triggered

OPTIONS = (
    ("↖", 225), ("⬆️️", 270), ("↗️", 315),
    ("⬅️", 180), ("❌", None), ("➡️", 0),
    ("↙️", 135), ("⬇️", 90), ("↘", 45), 
)