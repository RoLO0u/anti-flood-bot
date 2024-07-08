from typing import SupportsFloat
from cv2.typing import MatLike

import cv2, random
import numpy as np

from bot import const

def rotate_image(image: MatLike, angle: SupportsFloat) -> MatLike:
    image_center = tuple(np.array(image.shape[1::-1]) / 2)
    rot_mat = cv2.getRotationMatrix2D(image_center, -angle, 1.0)
    result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
    return result

def create_blank() -> MatLike:
    blank = np.zeros((const.HEIGHT, const.WIDTH, 3), np.uint8)
    blank[:, :, :] = const.WHITE
    return blank

def to_bytes(image: MatLike) -> bytes:
    return cv2.imencode(".jpg", image)[1].tobytes()

def create_captcha() -> tuple[bytes, str, int]:

    captcha = create_blank()
    
    target_path = const.IMAGES_ROUTE + random.choice(const.IMAGES)
    target = cv2.imread(target_path, -1)

    correct_answer, angle = random.choice(const.OPTIONS)

    rotate_offset = random.randint(-const.ROTATE_OFFSET, const.ROTATE_OFFSET)
    target = rotate_image(target, angle + rotate_offset)

    y_offset = random.randint(const.Y_OFFSET, const.HEIGHT - const.Y_OFFSET - target.shape[0])
    x_offset = random.randint(const.X_OFFSET, const.WIDTH - const.X_OFFSET - target.shape[1])

    y1, y2 = y_offset, y_offset + target.shape[0]
    x1, x2 = x_offset, x_offset + target.shape[1]

    alpha_s = target[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s

    for c in range(0, 3):
        captcha[y1:y2, x1:x2, c] = (alpha_s * target[:, :, c] +
           alpha_l * captcha[y1:y2, x1:x2, c])
    
    return to_bytes(captcha), correct_answer, angle