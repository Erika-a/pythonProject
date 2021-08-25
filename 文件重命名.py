import os
import shutil
import time
from os import renames

# os.renames()

path1 = r'C:\Users\PC\Desktop\WindowsNoEditor\AirCityExplorer\Content\Paks'
path2 = r'C:\Users\PC\Desktop\WindowsNoEditor\AirCityExplorer\Content\Paks'
namelist1 = "主要河流,重要景观河道,一般活力河道,重要节点,生态廊道,森林公园,湿地公园,综合公园,文化公园,城市广场"

namelist2 = "ZYHL,ZYHD,YBHD,ZYJD,STLD,SLGY,SDGY,ZHGY,WHGY,CSGC"


path3 = 'C:\\Users\\PC\\Desktop\\WindowsNoEditor\\AirCityExplorer\\Content\\Paks\\'

text1 = namelist1.split(',')
text2 = namelist2.split(',')

print(text1)
print(text2)

alllist = os.listdir(path1)


cout1 = 0
# for i in alllist:
#     if '.txt' in i:
#         old = os.path.join(path3,alllist[cout1])
#         new = os.path.join(path2,text2[cout1]) + '.3dt'
#
#         cout1 = cout1 + 1
#
#         print(old,new)
print(alllist)
for i in alllist:
    for t in text1:
        if t in i:

            p = text1.index(t)

            old = os.path.join(path1,i)
            new = os.path.join(path2,text2[p]) + '.3dt'
            if not os.path.exists(new):
                os.rename(old,new)
                print(old,"------ok------" ,new)
            else:
                print('-----no-----')
        else:
            print("文件未找到")






# for i in range(10):
#     file = open(path1 +'//'+ str(text1[cout1]) +'.txt','w')
#     cout1 = cout1 + 1
#     print(file.name)
#     file.close()

# choese1 = input("输入文件名字：")
#
# newname = names.split(',')[int(choese1)-1]
#
# newpath = os.path.join(path2,newname) + '.3dt'
#
#
# if os.path.exists(path1):
#     os.renames(path1,newpath)
#     print("重命名完成")
# else:
#     print("重命名失败")


# def FileRename():
#
