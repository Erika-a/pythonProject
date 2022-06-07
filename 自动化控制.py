import pyautogui,time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

width,height = pyautogui.size()

#移动到指定坐标

# for i in range(10):
#     pyautogui.moveTo(100, 100, duration=0.25)
#     pyautogui.moveTo(200, 100, duration=0.25)
#     pyautogui.moveTo(200, 200, duration=0.25)
#     pyautogui.moveTo(100, 200, duration=0.25)

#从当前鼠标位子移动

# for i in range(5):
#     pyautogui.moveRel(100, 0, duration=0.25)
#     pyautogui.moveRel(0, 100, duration=0.25)

#获取鼠标位置

# po = pyautogui.position()
# print(po)

#点击鼠标

# pyautogui.click(10,10)          #鼠标左键
# pyautogui.mouseDown(10,10)      #鼠标按下
# pyautogui.mouseUp(10,10)        #鼠标放开
# pyautogui.doubleClick(10,10)    #双击左键
# pyautogui.rightClick(10,10)     #点击右键
# pyautogui.middleClick(10,10)    #点击中键

#按住拖动

# time.sleep(5)
# pyautogui.click()
# distance = 200
# while distance > 0:
#     pyautogui.dragRel(distance,0,duration=0.2)
#     distance = distance - 5
#     pyautogui.dragRel(0,distance,duration=0.2)
#     pyautogui.dragRel(-distance,0,duration=0.2)
#     distance = distance - 5
#     pyautogui.dragRel(0,-distance,duration=0.2)

#滚动鼠标

# pyautogui.scroll(200)

#截图

# im = pyautogui.screenshot()
#
#
# print(im.getpixel((50,200)))
#
# t1 = pyautogui.pixelMatchesColor(50,200,(68,68,68))
# t2 = pyautogui.pixelMatchesColor(50,200,(255,135,144))
# print(t1,'\n',t2)

#图像识别

# t = pyautogui.locateOnScreen(r'C:\Users\PC\Desktop\1.jpg')             #找图返回坐标
# r = list(pyautogui.locateAllOnScreen(r'C:\Users\PC\Desktop\1.jpg'))    #找全部图
# y = pyautogui.center(t)                                 #返回图片的中心坐标
# print(t)
# print(r)
# print(y)
# pyautogui.click(y)

#键盘控制

# pyautogui.typewrite('hello,world',0.25)         #键盘按键输入
# pyautogui.keyDown('f1')                         #按下键盘
# pyautogui.keyUp('f1')                           #弹起键盘
# pyautogui.hotkey('ctrl','c')                    #按键组合

'''
moveTo（x，y）将鼠标移动到指定的x、y坐标。
moveRel（xOffset，yOffset）相对于当前位置移动鼠标。
dragTo（x，y）按下左键移动鼠标。
dragRel（xOffset，yOffset）按下左键，相对于当前位置移动鼠标。
click（x，y，button）模拟点击（默认是左键）。
rightClick() 模拟右键点击。
middleClick() 模拟中键点击。
doubleClick() 模拟左键双击。
mouseDown（x，y，button）模拟在x、y处按下指定鼠标按键。
mouseUp（x，y，button）模拟在x、y处释放指定键。
scroll（units）模拟滚动滚轮。正参数表示向上滚动，负参数表示向下滚动。
typewrite（message）键入给定消息字符串中的字符。
typewrite（[key1，key2，key3]）键入给定键字符串。
press（key）按下并释放给定键。
keyDown（key）模拟按下给定键。
keyUp（key）模拟释放给定键。
hotkey（[key1，key2，key3]）模拟按顺序按下给定键字符串，然后以相反的顺序释放。
screenshot() 返回屏幕快照的Image对象（参见第17章关于Image对象的信息）。
'''