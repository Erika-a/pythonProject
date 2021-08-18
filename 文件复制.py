import os
import sys
import getpass
import shutil
import cv2


def cjwj():
    floder = 'C:\\Users\\PC\\Desktop\\wenjian1\\'

    if not os.path.exists(floder):
        os.makedirs(floder)
        print("创建文件夹")
    else:
        print("文件夹已存在")
    for i in range(10):
        file = open(floder + 'wenjian' + str(i+1) +  '.txt','w')
        file.close()

def cjwj2():
    floder = 'C:\\Users\\PC\\Desktop\\wenjian2\\'

    if not os.path.exists(floder):
        os.makedirs(floder)
        print("ok")
    else:
        print('no')


# 文件复制

def wjfz():
    oldseg_path = "C:\\Users\\PC\\Desktop\\wenjian1\\"
    newseg_path = "C:\\Users\\PC\\Desktop\\wenjian2\\"

    for i in range(10):
        no = str(1+i)
        segname = 'wenjian'+no+'.txt'
        old_segname = os.path.join(oldseg_path,segname)
        newseg_name = os.path.join(newseg_path,segname)
        # shutil.copyfile(old_segname, newseg_name)
        shutil.move(old_segname, newseg_name)


# file = 'E:/Zhangjiakou_20200907/06_MAX/所有地块20210311/OSGB/0818'
#
# print(file)
#
# file2 = open(file+'/'+'new'+'.txt','w')

# 基本方法

def jb():
    alllist=os.listdir(u"D:\\notes\\python\\资料\\")
    for i in alllist:
        aa,bb=i.split(".")
        if 'python' in aa.lower():
            oldname= u"D:\\notes\\python\\资料\\"+aa+"."+bb
            newname=u"d:\\copy\\newname"+aa+"."+bb
            shutil.copyfile(oldname,newname)

def fztp():
    alllist = os.listdir(u"C:\\Users\PC\\Desktop\\wenjian1")

    for i in alllist:
        aa,bb=i.split(".")
        if 'png' in bb:
            oldname = u"C:\\Users\PC\\Desktop\\wenjian1\\" + aa + "." + bb
            newname = u"C:\\Users\PC\\Desktop\\wenjian2\\" + aa + "." + bb
            shutil.copyfile(oldname,newname)
        elif 'psd' in bb:
            print("跳过"+bb+"文件")
    print("复制"+bb+"完成")

# img1 = open("C:\Users\PC\Desktop\wenjian1\0537GXQA01B002AJ301T101.png",'r')



# 比较全面的方法

# coding:utf-8

def qmff():


    # shutil.copyfile("oldfile","newfile")       oldfile和newfile都只能是文件
    # 创建多级目录：os.makedirs（"/Users/ximi/version"）
    # 创建单个目录：os.mkdir（"project"）
    # #复制文件
    # shutil.copyfile('listfile.py', 'd:/test.py')
    # shutil.rmtree("dir")    空目录、有内容的目录都可以删
    # 检验给出的路径是否真地存:os.path.exists()
    # getpass.getuser()该函数返回登陆的用户名,不需要参数
    username = getpass.getuser()
    # 改变当前工作目录
    os.chdir('/Users/' + username + '/Documents/client/myProj/')
    # shutil.copyfile("oldfile","newfile")       oldfile和newfile都只能是文件
    # 创建多级目录：os.makedirs（"/Users/ximi/version"）
    # 创建单个目录：os.mkdir（"project"）
    # #复制文件
    # shutil.copyfile('listfile.py', 'd:/test.py')
    # shutil.rmtree("dir")    空目录、有内容的目录都可以删
    # 检验给出的路径是否真地存:os.path.exists()
    # getpass.getuser()该函数返回登陆的用户名,不需要参数
    username = getpass.getuser()
    # 改变当前工作目录
    os.chdir('/Users/' + username + '/Documents/client/myProj/')


# 文件的拷贝用shutil.copyfile(srcFilePath,dstFilePath)

def handleVersionFile():
    # os.getcwd()获取当前工作目录，即当前python脚本工作的目录路径。
    srcVersionFilePath = os.getcwd() + os.sep + "res/version/version.manifest"
    dstVersionFilePath = os.getcwd() + os.sep + "tools/myProj/version/version.manifest"

    versionDir = os.getcwd() + os.sep + "tools/myProj/version/"
    if not os.path.exists(versionDir):
        print(versionDir, '\n配置文件目录不存在，创建目录...')
        # os.mkdir(versionDir)
        os.makedirs(versionDir)
        print('创建配置文件目录成功！\n')

    srcProjectFilePath = os.getcwd() + os.sep + "res/version/project.manifest"
    dstProjectFilePath = os.getcwd() + os.sep + "tools/myProj/version/project.manifest"

    print('拷贝配置文件开始...')
    if os.path.exists(srcVersionFilePath):
        shutil.copyfile(srcVersionFilePath, dstVersionFilePath)

    if os.path.exists(srcProjectFilePath):
        shutil.copyfile(srcProjectFilePath, dstProjectFilePath)

    print('拷贝配置文件结束！\n')

# 文件夹的拷贝用shutil.copytree(dstResDir)

def handleAssetsFile():
    sourceSrcDir = os.getcwd() + os.sep + "src/"
    dstSrcDir = os.getcwd() + os.sep + "tools/myProj/assets/src/"
    sourceResDir = os.getcwd() + os.sep + "res/"
    dstResDir = os.getcwd() + os.sep + "tools/myProj/assets/res/"
    # 复制目录，olddir和newdir都只能是目录，且newdir必须不存在

    if os.path.exists(dstSrcDir):
        print(dstSrcDir, '存在先删除')
        # 如果要递归删除目录的内容，可使用shutil.rmtree()函数
        shutil.rmtree(dstSrcDir)

    print('拷贝代码文件夹开始...')
    shutil.copytree(sourceSrcDir, dstSrcDir)
    print('拷贝代码文件夹结束！\n')

    if os.path.exists(dstResDir):
        print(dstResDir, '存在先删除')
        shutil.rmtree(dstResDir)

    print('拷贝资源文件夹开始...')
    shutil.copytree(sourceResDir, dstResDir)
    print('拷贝资源文件夹结束！\n')





