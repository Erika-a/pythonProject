def sum(*numbers):
	total = 0.0
	for number in numbers:
		total += number 
		return total
	pass

print(sum(100.0,20.0,30.0))
print(sum(30.0,80.0))
print(sum(30.0,'80'))
print(sum(30.0,80.0,'80'))


def area(width,heiht):
	return width*heiht
	pass

print(area(320.0,480.0))
print(area(width=320.0,heiht=480.0))
print(area(heiht=480.0,width=320.0))


x = 200

def print_value():
	global x
	x = 100
	print("函数中x={0}".format(x))

print_value()
print("全局变量x={0}".format(x))
