s = """

	《出师表》
出师未捷身先死
长使英雄泪满襟
"""

print(s)



s_str = 'hello,world'
s_str.find('e')

print(s_str.find('e'))



text = 'AB CD EF GH IJ'
print(text.replace(' ','|',2))

print(text.replace(' ','|',))

print(text.replace(' ','|',1))




text = 'AB CD EF GH IJ'

print(text.split(' '))

print(text.split(' ', maxsplit=0))

print(text.split(' ', maxsplit=1))

print(text.split(' ', maxsplit=2))




stt="星期一星期二星期三星期四星期五星期六星期日"
stv=input("请输入星期数（1-7）：")
std=(int(stv)-1) * 3
stc=stt[std:std+3]
print("星期是"+str(stc)+".")

t1 = 1 , 2 , 3

