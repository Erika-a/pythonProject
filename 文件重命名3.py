import os
import shutil
import time


path1 = 'C:\\Users\\PC\Desktop\\新建文件夹 (2)\\京投'
path2 = 'C:\\Users\\PC\\Desktop\\新建文件夹 (3)\\京投'

def findfbx():

    global newname
    list = os.listdir(path2)
    for dirpath,dirname,filenames in os.walk(path1):
        for filename in filenames:
            if '.fbx' in filename and filename not in list:
                oldname = os.path.join(dirpath,filename)
                if dirpath.split('\\')[-2] in filename:
                    newname = os.path.join(path2,filename)
                elif dirpath.split('\\')[-2] not in filename:
                    newname = os.path.join(path2, dirpath.split('\\')[-2] + '_' + filename)

                # newname = os.path.join(path2, dirpath.split('\\')[-2] + '_' + filename)
                shutil.move(oldname,newname)
                print("\n{0}\n\n\t移动到了\n\n{1}\n".format(oldname,newname))
            # elif '.fbx' in filename and filename in list:
            #     print(filename)
            #     print(dirpath)


if __name__ == '__main__':
    findfbx()