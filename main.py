import os
from PIL import Image
from colors import *
from geometric_shapes import *

IMG_DIR = 'img'
filename = os.path.join(IMG_DIR, 'brasil.png')

WIDTH = 1400
module = WIDTH / 14
LENGTH = int(module * 20)

img = Image.new("RGB", (LENGTH, WIDTH), GREEN)
paint_diagonally(img, YELLOW)
img.save(os.path.join(IMG_DIR, "brasil_step_two.png"))
img.show()