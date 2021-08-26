import os
import shutil
import time

path1 = r'C:\Users\PC\Desktop\WindowsNoEditor\AirCityExplorer\Content\Paks\AirCityExplorer-WindowsNoEditor.pak'
path2 = r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0827\shapan'
oldname = path1
# newname = os.path.join(path2,'yhhhhh.3dt')




#将文件夹1下的pak重命名放到文件夹2下
def FileRename1():
    if not os.path.exists(path1):
        print("路径下没有文件")

    if os.path.exists(path1):
        text1 = input("输入文件名字:")
        oldname = path1
        newname = os.path.join(path2,text1) + '.3dt'
        shutil.move(oldname,newname)
        print(oldname,"\n-----ok-----\n",newname)

def OpenFile():
    name = open(r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0827\name2-1.txt','r')
    names = name.read()
    namelist = names.split()

    return namelist



def FileRename2():
    cout1 = 0
    p = 0
    while True:
        if not os.path.exists(path1):
            time.sleep(1)
            print("第",cout1 + 1,"个文件，等待文件")
        if os.path.exists(path1):
            time.sleep(5)
            try:

                newname = (os.path.join(path2,OpenFile()[p]) + '.3dt')
                shutil.move(oldname,newname)
                print(OpenFile()[p],"\n-----ok-----")
                p = p + 1


                cout1 = cout1 + 1
            except:
                print("文件正在使用")
        if cout1 == 37:
            break
    print("-----ok-----")

def GetNames():
    list = os.listdir(r'E:\Zhangjiakou_20200907\06_MAX\shapan\AirCityExplorer_hqf\Content\京张铁路弃线改造')
    namefile = open(r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0827\name1.txt','w')

    for i in list:
        namefile.write(i+'\n')


    print(list)

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
        Path = os.path.join(path2,i)
        size = os.stat(Path).st_size
        if size > 30000000:
            NewPath = os.path.join(path2 + '\\CU',i)
            shutil.copyfile(Path,NewPath)

    print("错误文件已复制")


if __name__ == '__main__':
    FindFile()
