import math
import random
from time import clock


#Π的计算
#蒙特卡洛方法

DARTS = 1200
hits = 0
clock()
for i in range(1,DARTS):
    x,y = random.random(),random.random()
    dist = math.sqrt(x**y + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("pi的值是%s"%pi)
print("程序运行时间是%-5.5ss"%clock())


