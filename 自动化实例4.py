from PIL import ImageGrab
import numpy
import cv2

if __name__ == '__main__':
    screenshot = ImageGrab.grab()

    screenshot.save("test.png")
    img_array = cv2.imread("test.png")
    print(img_array)

    # 跳过文件保存步骤，直接读取
    img_array2 = numpy.asanyarray(screenshot)
    # Image读取出来的是RGB, cv2是BGR。需要转化一下
    img_array2 = cv2.cvtColor(img_array2, cv2.COLOR_RGB2BGR)
    print(img_array2)