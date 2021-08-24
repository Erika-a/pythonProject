import os
import shutil
from PIL import Image

path = os.path.join("C:\\Users\\PC\\Desktop\\wenjian1\\","0537GXQA01B002AJ301T101.png")
img = Image.open(path)

print(img.format)
print(img.size)








