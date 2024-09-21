import os
from PIL import Image

IMG_DIR = 'img'
filename = os.path.join(IMG_DIR, 'brasil.png')

GREEN = (0, 148, 64)
YELLOW = (255, 203, 0)
BLUE = (48, 38, 129)
WHITE = (255, 255, 255)

WIDTH = 1400
LENGTH = int(WIDTH / 14 * 20)

img = Image.new("RGB", (LENGTH, WIDTH), GREEN)
img.save(os.path.join(IMG_DIR, "brasil_step_one.png"))