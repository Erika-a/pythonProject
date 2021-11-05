import pyautogui
from PIL import Image
import time


pg = pyautogui


def zhaotu(im):
    t = pg.locateOnScreen(im)
    x,y = pg.center(t)
    return x,y

def shili1():
    pg.click(zhaotu('Image/1.png'))
    time.sleep(2)
    pg.click(zhaotu('Image/2.png'))
    time.sleep(1)
    pg.typewrite('bilanhangxianwiki',0.1)
    time.sleep(0.5)
    pg.click(zhaotu('Image/3.png'))
    time.sleep(1.5)
    pg.click(zhaotu('Image/4.png'))
    time.sleep(1.5)
    pg.click(zhaotu('Image/5.png'))
    imt = 'Image/6.png'
    while True:
        try:
            time.sleep(1)
            t = pg.locateOnScreen('Image/6.png')
            x,y = pg.center(t)
            if x > 1 or y > 1:
                pg.screenshot('Image/save.png')
                break
            else:
                pass

        except:
            print("图片没找到，滚动继续")
            pg.scroll(-100)

def chik(img):
    time.sleep(1)
    img1 = zhaotu(f'Image/{img}.png')
    print(img1)
    pg.click(img1)

def chik2(img):
    time.sleep(1)
    while True:
        try:
            img1 = zhaotu(f'{img}.jpg')
            print(img1)
            pg.click(img1)
            break
        except:
            print("meizhaodao")
            pass


if __name__ == '__main__':
    chik(1)