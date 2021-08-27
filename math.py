# #Π的计算
# #蒙特卡洛方法
#
# DARTS = 1200
# hits = 0
# clock()
# for i in range(1,DARTS):
#     x,y = random.random(),random.random()
#     dist = math.sqrt(x**y + y**2)
#     if dist <= 1.0:
#         hits = hits + 1
# pi = 4 * (hits/DARTS)
# print("pi的值是%s"%pi)
# print("程序运行时间是%-5.5ss"%clock())
#


mianji = float(input("输入面积："))

sdnq = 180 * mianji
wlss = 100 * mianji
ptsj = 290 * mianji
fdm = 2800
mjc = 18000
zongji = sdnq + wlss + ptsj + fdm + mjc
print("水电暖气四项费用为：",sdnq,"\n网络设施安装费为：",wlss,"\n配套升级费 灯化亮化 充电桩费用为：",ptsj,"\n高级防盗门2800\n面积差18000\n总计:",zongji)

print("懂了")