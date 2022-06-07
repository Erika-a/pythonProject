import os
import shutil
import pyxms

path = r'C:\Users\PC\Desktop\2FDB'
path2 = r'E:\OSGB\1228'
# path2 = r'E:\Zhangjiakou_20200907\新张家口\FDB导出'

def getcout():
    t = open('name.txt')
    F = t.readline()
    return F

def rename():
    path = r'C:\Users\Night7\Desktop\新建文件夹'
    path2 = r''
    list1 = os.listdir(path)
    print(list1)


def getfile():
    for dirpath, dirname, filenames in os.walk(path):
        for filename in filenames:
            if '.fbx' in filename:
                oldname = os.path.join(dirpath,filename)
                newname = os.path.join(path2 + f'\\{getcout()}_' + filename)
                shutil.move(oldname,newname)
                print(f'{path2}\n{newname}')
    cout2 = int(getcout()) + 1
    file = open('name.txt','w')
    file.write(str(cout2))
    file.close()
    shutil.rmtree(path)
    os.mkdir(path)
    if os.path.exists(path):
        print(True)

def redir():
    # list = os.listdir(path)
    #
    # for i in list:
    #     t = os.path.join(path,i)
    #     os.remove(t)
    # print(list)
    shutil.rmtree(path)
    os.mkdir(path)
    if os.path.exists(path):
        print(True)
if __name__ == '__main__':
    getfile()