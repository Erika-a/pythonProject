import os
import shutil
import time


def gettime():
    T = time.time()
    t1 = time.strftime("%m%d", time.localtime(T))
    return t1


path1 = r'C:\Users\PC\Desktop\WindowsNoEditor\AirCityExplorer\Content\Paks\AirCityExplorer-WindowsNoEditor.pak'
path2 = r'E:\OSGB\{0}\3dt'.format(gettime())
if not os.path.exists(path2):
    os.makedirs(path2)
# path3 = input("输入路径：\n")
oldname = path1


# newname = os.path.join(path2,'yhhhhh.3dt')


class rename1(object):
    def __init__(self, filename, filepath):
        self.name = filename
        self.path = filepath


# T = rename1(path1,path2)
# print('路径为1111111111111\n{0}\n{1}'.format(T.name,T.path))


# 将文件夹1下的pak重命名放到文件夹2下
def FileRename1():
    if not os.path.exists(path1):
        print("路径下没有文件")
    if not os.path.exists(path2):
        os.makedirs(path2)

    if os.path.exists(path1):
        text1 = input("输入文件名字:")
        oldname = path1
        newname = os.path.join(path2, text1) + '.3dt'
        shutil.move(oldname, newname)
        print(oldname, "\n-----ok-----\n", newname)


def OpenFile():
    name = open(r'E:\OSGB\{0}\name1.txt'.format(gettime()), 'r', encoding='utf-8')
    names = name.read()
    namelist = names.split()

    return namelist


def FileRename2():
    cout1 = 0
    p = 0
    s = int(input("输入文件数量："))
    while True:
        if not os.path.exists(path1):
            time.sleep(1)
            print("第", cout1 + 1, "个文件，等待文件")
        if os.path.exists(path1):
            time.sleep(5)
            try:

                newname = (os.path.join(path2, OpenFile()[p]) + '.3dt')
                print(newname)

                shutil.move(oldname, newname)
                print(OpenFile()[p], "\n-----ok-----")
                p = p + 1

                cout1 = cout1 + 1
            except:
                print("文件正在使用")
        if cout1 == s:
            break
    print("-----ok-----")


def GetNames():
    tpath = input("输入文件路径：\n")
    ttybe = input("输入文件格式：\n")
    tlist = []
    namefile = open(path2.replace('3dt', '') + 'name1.txt', 'w', encoding='utf-8')
    for filepath, dirname, filenames in os.walk(tpath):
        for filename in filenames:
            if ttybe in filename:
                tlist.append(filename)
    tlist.sort()
    for i in tlist:
        namefile.write(i + '\n')
    namefile.close()


def findnamedel():
    delpath = r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0827\shapan'
    namefile = open(r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0827\name1.txt', 'r')
    alllist = namefile.read()
    filelist = os.listdir(delpath)
    cout1 = 0
    for i in filelist:
        if i in alllist:
            delpath1 = os.path.join(delpath, i)
            os.remove(delpath1)
            cout1 = cout1 + 1
            print(i + '-----ok')

    print(cout1, "个文件已删除")


def findfile():
    findpath = r'E:\Zhangjiakou_20210815\Zhangjiakou_20210815_files\3DT'
    namefile = open(findpath + '\\' + 'name.txt', 'r', encoding='utf-8')
    namelist = namefile.read()
    # print(namelist)
    for filepath, dirname, filenames in os.walk(findpath):
        for filename in filenames:

            if filename in namelist:
                print(filename.replace('.3dt', ''))
                print(filepath.replace('E:\Zhangjiakou_20210815\Zhangjiakou_20210815_files', ''))

def findsetfile():
    findpath = r'E:\Zhangjiakou_20200907\06_MAX\shapan\AirCityExplorer\Content\SPjiaohu1'
    namefile = open(path2.replace('3dt', '') + 'name1.txt', 'w', encoding='utf-8')
    tlist = []

    for filepath, dirname, filenames in os.walk(findpath):
        for filename in filenames:
            if '.umap' in filename and '3_' in filepath:
                tlist.append(filename)
    tlist.sort()
    for i in tlist:
        namefile.write(i + '\n')
    namefile.close()
    print('----------\n文件写入完成\n----------')







def TxtDel():
    lineList = []
    file = open(r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0827\name2.txt', 'r', encoding='utf-8')
    while 1:
        line = file.readline()
        if not line:
            print("Read file End or Error")
            break
        line2 = line.replace('.umap', '')

        lineList.append(line2)

    file.close()
    file = open(r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0827\name2-1.txt', 'w', encoding='UTF-8')
    for i in lineList:
        file.write(i)
    file.close()


def FindFile():
    alllist = os.listdir(path2)
    for i in alllist:
        Path = os.path.join(path2, i)
        size = os.stat(Path).st_size
        if size > 30000000:
            NewPath = os.path.join(path2 + '\\CU', i)
            shutil.copyfile(Path, NewPath)

    print("错误文件已复制")


def finddel():
    alllist = os.listdir(path2)
    for i in alllist:
        Path = os.path.join(path2, i)
        size = os.stat(Path).st_size
        if size > 30000000:
            os.remove(Path)
    print("错误文件已复制")

def renamefile():
    path1 = input('输入路径：\n')
    list = os.listdir(path1)
    for i in list:
        if 'B' in i:
            pass
        if 'B' not in i:
            oname = os.path.join(path1,i)
            nname = os.path.join(path1,'B' + i)
            shutil.move(oname,nname)
            print(i,"修改完成")

def rename4():
    path = r'E:\GS_\1_MAX\沙盘\乡'
    list = os.listdir(path)
    print(list)
    for i in list:
        oldname = os.path.join(path,i)
        newname = os.path.join(path,i.replace('bak','.max'))
        shutil.move(oldname,newname)
        print(f"{i}文件重命名完成")


# 所选路径下的文件格式移动到指定文件夹下
def getfiles():
    path = r'E:\OSGB\1104\3DT'
    path2 = r'E:\OSGB\1104\3DT'
    for dirname,dirpath,filenames in os.walk(path):
        for filename in filenames:
            if '.3dt' in filename:

                oldpath = os.path.join(dirname,filename)
                newpath = os.path.join(path2,filename)
                shutil.move(oldpath,newpath)
                time.sleep(0.3)
                if os.path.exists(dirname):
                    os.rmdir(dirname)
                print(f"\t\t{oldpath}\t\t{newpath}")
                print(f"{filename}\t移动完成,{dirname}\t删除完成")



def main():
    print("PAK文件重命名")
    print("功能:\n\t1.单文件改名\t2.批量文件改名\t3.文件名获取\t4.关闭")
    choese1 = int(input("选择功能:\n"))
    print("----------")
    print("导出路径是否更改，默认为以当天创建文件夹.")
    choese2 = input("1 or 2:")
    if choese2 == '1':
        path2 = input("输入路径：\n")
        print("路径为{0}".format(path2))
    if choese2 == '2' or choese2 is None:
        print("路径为默认")
    print("----------")

    if choese1 == 1:
        print("单文件改名")
        FileRename1()
    if choese1 == 2:
        FileRename2()
    if choese1 == 3:
        GetNames()
    if choese1 == 4:
        exit()






'''
界线四川
界线清海
十四市
'''
def rrr():
    print(OpenFile())
if __name__ == '__main__':
    FileRename1()
