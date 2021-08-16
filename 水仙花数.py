# conding=utf-8






for i in range(100,1000):
	if i == (i // 100) ** 3 + (i % 10) ** 3 + (i % 100 // 10) ** 3:
		print(i)

# a = 152 // 100
# b = 152 % 10
# c = 152 % 100 // 10

# print(a)
# print(b)
# print(c)