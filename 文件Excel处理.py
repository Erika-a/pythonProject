import xlsxwriter
import os
import time

def excel1():
    wb = xlsxwriter.Workbook('C:\\Users\\PC\\Desktop\\111.xlsx')
    # 在G盘xxoo文件下创建103的excel
    worksheet = wb.add_worksheet('s001')
    # 103的excel的sheet页名称为s001
    worksheet.write(0,0,123456)
    worksheet.write(2,1,664)
    worksheet.write(1,5,250)
    # 写入信息
    wb.close()

def excel2():
    file = xlsxwriter.Workbook('C:\\Users\\PC\\Desktop\\文件名称对比.xlsx')
    list = os.listdir(r'E:\Zhangjiakou_20200907\06_MAX\所有地块20210311\OSGB\0827\shapan')
    worksheet = file.add_worksheet('name')
    l = 0
    h = 5

    for i in list:
        if '.3dt' in i:
            worksheet.write(l,h,i)
            l = l + 1
            if l >= 20:
                l = 0
                h = h + 2
            print(i+'写入完毕-------')
    print('excel file ok')
    file.close()


if __name__ == '__main__':
    excel2()
