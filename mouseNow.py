import time
import pyautogui
print('Press Ctrl-C to quit')

try:
    while True:
        x,y = pyautogui.position()
        postr = 'X:' + str(x).rjust(4) + 'Y:' + str(y).rjust(4)
        pixelcolor = pyautogui.screenshot().getpixel((x,y))
        postr += ' RGB:(' + str(pixelcolor[0]).rjust(3)
        postr += ',' + str(pixelcolor[1]).rjust(3)
        postr += ',' + str(pixelcolor[2]).rjust(3) + ')'
        time.sleep(1)
        print(postr)

        # print('\b' * len(postr),end='',flush=True)
except KeyboardInterrupt:
    print('\nDone')


