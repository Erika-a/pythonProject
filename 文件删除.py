import os
import time
import shutil




def wjsc():
    path = 'C:\\Users\\PC\\Desktop\\wenjian1\\0537GXQA01B002AJ301T101.png'
    path2 = 'C:\\Users\\PC\\Desktop\\1\\'
    if os.path.exists(path):#删除单个文件
        os.remove(path)
        print('file delete ok!')
    else:
        print('-----------no file find!----------')

    if os.path.exists(path2):#删除文件夹，目录必须为空
        os.rmdir(path2)
        print('dir delete ok')
    else:
        print('-----------no dir find!-----------')

wjsc()

#递归删除目录
def dgsc():
    path ='C:\\Users\\PC\\Desktop\\wenjian1\\0537GXQA01B002AJ301T101.png'