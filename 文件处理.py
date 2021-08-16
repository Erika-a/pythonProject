import turtle
import random



def dakai():
    fname = input("Enter filename:")
    infile = open(fname ,"r")
    data = infile.read()
    print(data)


# 遍历文件模板
"""
#通用代码框架
def tymb():
    file = open("somefile","r")
    for line in file.readline():

    file.close()

#简化代码框架
def jhmb():
    file = open("somefile","r")
    for line in file

    file.close()
"""


# 拷贝文件
def kaobei():
    # 定义输入文件变量
    f1 = input("Enter a souce file:").strip()
    f2 = input("Enter a souce file:").strip()
    # 定义文件打开变量
    infile = open(f1 ,"r")
    outfile = open(f2 ,"w")

    # 定义数字统计变量
    countlines = countchars = 0
    # 遍历文件
    for line in infile:
        countlines += 1
        countchars += len(line)
        outfile.write(line)
    # 输出文件里行数和文字个数
    print(countlines ,"lines and" ,countchars ,"chars copied")
    # 关闭文件
    infile.close()
    outfile.close()


def xie():
    f1 = open("data.txt" ,"w")
    st1 = ("300,0,144,1,0,0\n300,0,144,0,1,0\n300,0,144,0,0,1\n300,0,144,1,1,0\n300,0,108,0,1,1\n184,0,72,1,0,1\n184,0,72,0,0,0\n184,0,72,0,0,0\n184,0,72,0,0,0\n")


    f1.write(st1)
    print("写入了", "个字符")
    f1.close()


def darwsset():
    turtle.title('数据驱动的动态路径绘制')
    turtle.setup(800,600,0,0)

    pen = turtle.Turtle()
    pen.color("red")
    pen.width(5)
    pen.shape("turtle")
    pen.speed(1)
    return pen

def duqu():
    result=[]
    file = open("data.txt","r")
    for line in file:
        result.append(list(map(float,line.split(','))))
    return result


def darwsnake():
    l = duqu()
    p = darwsset()
    for i in range(len(l)):
        p.color((l[i][3],l[i][4],l[i][5]))
        p.fd(l[i][0])
        if l[i][1]:
            p.rt(l[i][2])
        else:
            p.lt(l[i][2])
    p.goto(0,0)


#多文件操作

def xie2():
    f1 = open("7dianhua.txt","w")
    str1 =( """姓名      电话
刘四 	 144 4793 8796 	 
刘一 	 185 8118 4371 	 
王三 	 160 5219 8194 	 
刘六 	 160 9094 2277 	 
赵七 	 185 5173 7950 	 
赵五 	 160 6176 4164 	 
杨七 	 157 1472 5614 	 """)
    str2 = ("")
    if f1 == str1:
        print("已存在相同内容")
    else:
        f1.write(str1)
        print("文件",f1.name,"写入完成")
    f1.close()

def xie3():
    f1 = open("7youxiang.txt","w")
    str1 =( """姓名      邮箱
刘四 	 908354526 @qq.com
刘一 	 839340375 @gmail.com
王三 	 553128881 @qq.com
刘六 	 752454892 @126.com
赵七 	 596527282 @gmail.com
赵五 	 965184385 @126.com
杨七 	 938197716 @qq.com""")
    str2 = ("")
    if f1 == str1:
        print("已存在相同内容")
    else:
        f1.write(str1)
        print("文件",f1.name,"写入完成")
    f1.close()


def rand1():
    for i in range(5):
        print(random.choice(seq=[157,160,185,144]),random.randint(1000,9999),random.randint(1000,9999))


def rand2():
    xname_list = ("张","王","李","刘","赵","孙","杨")
    mname_list = ("一","二","三","四","五","六","七")
    yx_list1 = ("@qq.com","@163.com","@126.com","@gmail.com")

    cname_list = 0


    for i in range(len(xname_list)):
        """
        numb_list = (random.choice(seq=[157, 160, 185, 144]),random.randint(1000, 9999),random.randint(1000, 9999))
        numb_list = str(numb_list)
        """
        listc = (random.choice(xname_list))+(random.choice(mname_list))
        yx = (random.choice(yx_list1))
        print(listc,"\t",random.choice(seq=[157, 160, 185, 144]),random.randint(1000, 9999),random.randint(1000, 9999),"\t",random.randint(100000000,999999999),yx)


def duowj():
    f1 = open('7dianhua.txt','rb')
    f2 = open('7youxiang.txt','rb')

    f1.readline()
    f2.readline()
    l1 = f1.readlines()
    l2 = f2.readlines()

    l1_name = []
    l1_nume = []
    l2_name = []
    l2_emal = []

    for line in l1:
        elements = line.split()
        l1_name.append(str(elements[0].decode('gbk')))
        l1_nume.append(str(elements[1].decode('gbk')))

    for line in l2:
        elements = line.split()
        l2_name.append(str(elements[0].decode('gbk')))
        l2_emal.append(str(elements[1].decode('gbk')))

    lines = []
    lines.append('姓名\t\t    电话\t\t    邮箱\n')

    for i in range(len(l1_name)):
        s = ''
        if l1_name[i] in l2_name:
            j = l2_name.index(l1_name[i])
            s = '\t\t'.join([l1_name[i],l1_nume[i],l2_emal[j]])
            s += '\n'

        else:
            s = '\t'.join([l1_name[i],l1_nume[i],str('    ------    ')])
            s += '\n'
        lines.append(s)

    for i in range(len(l2_name)):
        s = ''
        if l2_name[i] not in l1_name:
            s = '\t\t'.join([l2_name[i],str('    -----    '),l2_emal[i]])
            s += '\n'
        lines.append(s)

    f3 = open('7habing.txt','w')
    f3.writelines(lines)

    f1.close()
    f2.close()
    f3.close()

    print("合并文件成功")



duowj()