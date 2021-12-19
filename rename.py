import os
import shutil

path = r'C:\Users\Night7\Desktop\新建文件夹'

def getcout():
    t = open('name.txt')
    F = t.readline()
    return F

def rename():
    path = r'C:\Users\Night7\Desktop\新建文件夹'
    path2 = r''
    list1 = os.listdir(path)
    print(list1)


def getfile(path,path2):
    while True
    for dirpath, dirname, filenames in os.walk(path):
        for filename in filenames:
            if '.txt' in filename:
                oldname = os.path.join(dirpath,filename)
                newname = os.path.join(path2 + f'\\{getcout()}_' + filename)
                shutil.move(oldname,newname)
                print(f'{path2}\n{newname}')
    cout2 = int(getcout()) + 1
    file = open('name.txt','w')
    file.write(str(cout2))
    file.close()


if __name__ == '__main__':
    getfile(path = r'C:\Users\Night7\Desktop\新建文件夹',path2 = r'C:\Users\Night7\Desktop\新建文件夹 (2)')
