import os

# 创建文件夹

def mkdir(path):
    folder = os.path.exists(path)

    if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
        os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        print("---  创建文件夹...  ---")
        print("---  完成  ---")

    else:
        print("---  文件夹已存在!  ---")


file = "E:\\Zhangjiakou_20200907\\06_MAX\\所有地块20210311\\OSGB\\0818\\3dt"


# os.getcwd()可以查看py文件所在路径；

# 在os.getcwd()后边 加上 [:-4] + 'xxoo\\' 就可以在py文件所在路径下创建 xxoo文件夹

def ljck():
    folder = os.getcwd()[:-4] + 'new_folder\\test\\'
    folder2 = os.getcwd() + '\\new_folder\\test\\'
    # 获取此py文件路径，在此路径选创建在new_folder文件夹中的test文件夹

    if not os.path.exists(folder2):
        os.makedirs(folder2)
        print(folder2 + "\n文件夹创建完成")

# 创建txt文件
#
# 在桌面创建一个名字为new的txt文件

def cj():
    file = open('C:\\Users\\PC\\Desktop\\'+'new'+'.txt','w')
    file.close()

def cj2():
    path1 = input("输入一个路径：")
    flie_name = input("输入文件名字:")
    flie_lie = int(input("选择文件格式：\n1,txt\n2,jpg\n3,bat\n:"))
    print(path1 + "\\" + flie_name + ".txt")
    if flie_lie == 1:
        file = open(path1+ "\\" + flie_name + '.txt','w')
        print(flie_name+'.txt'+"创建完成")
    elif flie_lie == 2:
        file = open(path1+ "\\" + flie_name + '.jpg', 'w')
        print(flie_name + '.jpg' + "创建完成")
    elif flie_lie == 3:
        file = open(path1+ "\\" + flie_name + '.bat', 'w')
        print(flie_name + '.bat' + "创建完成")
    else:
        print("创建失败")

# 在py文件路径下创建test的txt文件

def txt(name,text):
    b = os.getcwd()+'\\' + 'new\\'

    if not os.path.exists(b):
        os.makedirs(b)

    xxoo = b + name + '.txt'

    file = open(xxoo,'w')

    file.write(text)

    file.close()
    print("ok")

# 创建excel

import xlsxwriter

def excel():
    wb = xlsxwriter.Workbook('C:\\Users\\PC\\Desktop\\111.xlsx')
    # 在G盘xxoo文件下创建103的excel
    worksheet = wb.add_worksheet('s001')
    # 103的excel的sheet页名称为s001
    worksheet.write(0,0,123456)
    worksheet.write(2,1,664)
    worksheet.write(1,5,250)
    # 写入信息
    wb.close()

def notdir(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print("{0}\n创建完成".format(path))


def cjwjj():
    # p = input("输入路径自动创建mesh,texture,material:\n")
    p = r'E:\Zhangjiakou_20200907\06_MAX\shapan\AirCityExplorer\Content\SPjiaohu1'
    t = input("输入文件夹名：\n")
    path1 = os.path.join(p,t)
    path2 = os.path.join(p,t + '\\Mesh')
    path3 = os.path.join(p, t + '\\Texture')
    path4 = os.path.join(p, t + '\\Material')
    # if not os.path.exists(path1):
    #     os.makedirs(path1)
    #     print("{0}\n创建完成".format(path1))
    # if not os.path.exists(path2):
    #     os.makedirs(path2)
    #     print("{0}\n创建完成".format(path2))
    # if not os.path.exists(path3):
    #     os.makedirs(path3)
    #     print("{0}\n创建完成".format(path3))
    # if not os.path.exists(path4):
    #     os.makedirs(path4)
    #     print("{0}\n创建完成".format(path4))
    notdir(path1)
    notdir(path2)
    notdir(path3)
    notdir(path4)


if __name__ == '__main__':
    cjwjj()




