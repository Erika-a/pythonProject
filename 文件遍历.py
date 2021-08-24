import os
import shutil

#当文件夹内只有文件时–listdir()
#当目标文件夹中只有文件时，我们使用os模块的listdir()方法即可：该方法可以返回目标路径下的文件和文件夹的名字列表，参数就是目标路径。


def getfiles():
    path1 = r'E:\\Zhangjiakou_20200907\\06_MAX\\所有地块20210311\\OSGB\\0823\\3dt'
    path2 = r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\A_QX_BEI_06_01'
    filename = os.listdir(path1)
    filename2 = os.listdir(path2)
    print(filename)
    print(filename2)

# 当文件中既有文件又有文件夹时–os.walk()
# 当目标文件中既有文件又有文件夹时，我们使用listdir()方法就只能获得第一层子文件或文件夹了，而子文件夹中的内容便获取不到了。

def getfiles2():
    path1 = r'E:\\Zhangjiakou_20200907\\06_MAX\\所有地块20210311\\OSGB\\0823\\3dt\\'
    path2 = r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\A_QX_BEI_06_01'
    for filepath,dirname,filenames in os.walk(path1):
        for filename in filenames:
            print(filename)
            print(os.path.join(filepath,filename))



# 扩充—获得目标路径下的所有文件的绝对路径
# 如果你足够细心的话，就会发现我们的filepath和filenames打印的结果图是一一
# 对应的关系：文件1.txt和文件2.txt的路径就是E:\test2；文件11.txt和文件12.txt的路径就是E:\test2\目录1；
# 以此类推。那么我们把这两个返回值拼在一起，不就是各个文件的绝对路径了么？



#遍历文件移动
def sl1():
    path1 = r'E:\\Zhangjiakou_20200907\\06_MAX\\所有地块20210311\\OSGB\\0823\\3dt\\'
    path2 = r'E:\\Zhangjiakou_20200907\\06_MAX\\所有地块20210311\\OSGB\\0823\\3dt\\'
    for filepath,dirname,filenames in os.walk(path1):
        for filename in filenames:
            if '.3dt' in filename:
                old = os.path.join(filepath,filename)
                new = path2
                alllist = os.listdir(path2)
                if filename not in alllist:
                    shutil.move(old, new)
                    print(filename, "移动成功")
                if filename in alllist:
                    print(filename,"文件已存在")










def sl2():
    path1 = r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\高铁新城中间建筑'
    path2 = r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0823\高铁新城中间建筑\images'
    alllist = os.listdir(path1)
    for i in alllist:
        if '.tif' in i:
            old = os.path.join(path1,i)
            new = os.path.join(path2,i)
            shutil.copyfile(old,new)
            print(i,"复制完成")


def sl3():
    path1 = r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0803\ZJK_QX_2050\images'
    path2 = r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0803\ZJK_QX_2050\images'
    # if oldfilename == newfilename:
    #     shutil.copyfile(oldfilename,newfilename)
    alllist = os.listdir(path1)
    filelist1 = []
    for filepath,dirname,filenames in os.walk(path2):
        for filename in filenames:
            for i in alllist:

                if '.tif' in i:
                    nu = filelist1.append(i)
            print(nu)
    # for filepath,dirname,filenames in os.walk(path1):
    #     for filename in filenames:
    #         if '.tif' in filename:
    #             print(os.path.join(filepath,filename))
    #
    print()

#单文件夹遍历多文件夹复制
def sl4():
    path1 = r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\蓝色区域透明图\B_QX_BEI_05_08'
    path2 = r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0824'
    alllist = os.listdir(path1)

    for filepath,dirname,filenames in os.walk(path2):
        for filename in filenames:
            for i in alllist:
                if '.tif' in i and filename == i:
                    old = os.path.join(path1,i)
                    new = os.path.join(filepath,filename)
                    shutil.copyfile(old,new)
                    print(old,"--ok--",new)
    print("\n文件复制完成\n")
    # for i in alllist:
    #     for j in alllist2:
    #         if i == j:
    #             print(i,"=",j)

#多文件夹遍历多文件夹
def sl5():
    path1 = input(r"旧路径：")
    path2 = input(r"新路径：")
    if not os.path.exists(path1):
        print(path1,"\n路径不存在")
        exit()
    if not  os.path.exists(path2):
        print(path2,"\n路径不存在")
        exit()

    for oldpath,olddir,oldnames in os.walk(path1):
        for oldname in oldnames:
            for newpath,newdir,newnames in os.walk(path2):
                for newname in newnames:
                    if ".tif" in oldname and oldname == newname :
                        old = os.path.join(oldpath,oldname)
                        new = os.path.join(newpath,newname)
                        shutil.copyfile(old,new)
                        print(old,"----ok----",new)

    print("\n文件复制完成\n")

sl5()