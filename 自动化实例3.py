import time
import os
from PIL import Image
import cv2 as cv
import pyautogui
im = Image

img = cv.imread('Image/1.jpg')

print(img.shape)
print(type(img),img)

cv.imshow('img',img)

cv.waitKey(0)



