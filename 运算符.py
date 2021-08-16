# coding=utf-8



i = 0

while i * i < 10:
	i += 1
	if i == 3:
		break
	print(str(i)+'*'+str(i)+'=',i * i)
else:
	print('while over')
