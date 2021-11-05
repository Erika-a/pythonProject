import os
import time


# 获取文件创建时间

def cjsj(file):
    return [
        time.ctime(os.path.getatime(file)),#访问时间
        time.ctime(os.path.getctime(file)),#创建时间
        time.ctime(os.path.getmtime(file))#最近修改时间
    ]

filename = r'E:\A'

filetime = time.localtime(os.path.getmtime(filename))


print(time.ctime(os.path.getatime(filename)))

print(os.stat(filename).st_mtime)

print(time.localtime(1629197073.1452785))

print(time.strftime("%Y-%m-%d-%H:%M:%S",filetime))

print(time.strftime("%Y%m%d%H%M%S",filetime))

print(os.path.getatime(filename))
print(os.path.getctime(filename))
print(os.path.getmtime(filename))


print(time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(os.path.getatime(filename))))
print(time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(os.path.getctime(filename))))
print(time.strftime("%Y-%m-%d-%H:%M:%S",time.localtime(os.path.getmtime(filename))))

time1 = os.path.getatime(filename)
time2 = os.path.getmtime(filename)

if time1 >= time2:
    print("ture")
else:
    print('flase')
