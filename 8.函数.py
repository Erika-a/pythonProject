def rect_area(width,height):
	area = width * height
	return area

def print_area(width,height):
	area = width * height

	print("{0}x{1}长方形面积:{2}".format(width,height,area))
	pass
	pass

r_area = rect_area(320,480)

print("{0}x{1}长方形面积:{2:f}".format(320,480,r_area))

r_area = rect_area(width=320,height=480)

print("{0}x{1}长方形面积:{2:f}".format(320,480,r_area))



def make_coffee(name="卡布奇诺"):
	return "制作一杯{0}咖啡".format(name)


coffee1 = make_coffee("拿铁")
coffee2 = make_coffee()

print(coffee1)

print(coffee2)



def sum(*numbers):
	total = 0.0
	for number in numbers:
		total += number
	return total
	pass


print(sum(100.0,20.0,30.0))

print(sum(30.0,80.0))


def show_info(**info):
	print('-----show_info-----')
	for key, value in info.items():
		print('{0}-{1}'.format(key,value))

show_info(name='tony',age=18,sex=True)
show_info(sutdent_name='tony',sutdent_no='1000')




x = 20

def print_value():
	global x
	x = 10
	print("函数中x = {0}".format(x))


print_value()
print("全局变量x = {0}".format(x))


def add(a,b):
	return a+b

def sub(a,b):
	return a-b

def square(a):
	return a * a
	pass

def calc(opr):
	if opr == '+':
		return add
	else:
		return sub

	pass

f1 = calc('+')
f2 = calc('-')
print("10 + 5 = {0}".format(f1(10,5)))
print("10 - 5 = {0}".format(f2(10,5)))



# 提供过滤条件函数

def f1(x):
	return x >50 #找出大于50的元素

data1 = [66,15,91,28,98,50,7,80,99]

filtered = filter(f1,data1)

data2 = list(filtered)

print(data2)


# 提供变换规则的函数

def f1(x):
	return x * 2 #变换规则乘以2

data1 = [66,15,91,28,98,50,7,80,99]

mapped = map(f1,data1)

data2 = list(mapped)

print(data2)



def calc(opr):
	if opr == '+':
		return lambda a,b: (a + b)
	else:
		return lambda a,b: (a - b)
	pass

f1 = calc('+')
f2 = calc('-')
print("10 + 5 = {0}".format(f1(10,5)))
print("10 - 5 = {0}".format(f2(10,5)))


data1 = [66,15,91,28,98,50,7,80,99]

filtered = filter(lambda x: (x > 50),data1)

data2 =list(filtered)

print(data2)

mapped = map(lambda x: (x * 2),data1)

data3 = list(mapped)

print(data3)
