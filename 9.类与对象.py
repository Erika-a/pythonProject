# coding=utf-8

class car(object):
	pass


class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name,age):
		self.name = name
		self.age = age

d = Dog('球球',2)
print('我们家狗狗名叫{0},{1}岁了。'.format(d.name,d.age))



class Dog(object):
	"""docstring for Dog"""
	def __init__(self, name,age,sex='雌性'):
		self.name = name
		self.age = age 
		self.sex = sex

d1 = Dog('球球',2)
d2 = Dog('哈哈',1,'雄性')
d3 = Dog(name='拖布',sex='雄性',age=3)


print('{0}:{1}岁{2}。'.format(d1.name,d1.age,d1.sex))
print('{0}:{1}岁{2}。'.format(d2.name,d2.age,d2.sex))
print('{0}:{1}岁{2}。'.format(d3.name,d3.age,d3.sex))


class Dog(object):
	def __init__(self,name,age,sex = "雄性"):
		self.name = name
		self.age = age
		self.sex = sex


	def run(self):
		print("{}在跑...".format(self.name))


	def speak(self,sound):
		print('{}在叫,"{}"!'.format(self.name,sound))


dog = Dog('球球',2)
dog.run()
dog.speak('汪  汪  汪')

# 类变量

class Account:
	interest_rate = 0.0568

	def __init__(self,owner,amount):
		self.owner = owner
		self.amount = amount

account = Account('tony',800000.0)

print('账户名：{0}'.format(account.owner))
print('账户金额:{0}'.format(account.amount))
print('利率:{0}'.format(Account.interest_rate))


# 类方法

class Account:
	interest_rate = 0.0668

	def __init__(self,owner,amount):
		self.owner = owner
		self.amount = amount

	@classmethod
	def interest_by(cls,amt):
		return cls.interest_rate * amt

interest = Account.interest_by(12000.0)

print('计算利息:{0:.4f}'.format(interest))
	
# 私有实例变量

class Account:
	__interest_rate = 0.0568

	def __init__(self,owner,amount):
		self.owner = owner
		self.__amount = amount


	def desc(self):
		print("{0}金额：{1}利率：{2}".format(self.owner,self.__amount,Account.__interest_rate))


account = Account('tony',800000.0)
account.desc()

print('账户名：{0}'.format(account.owner))
# print('账户金额{0}'.format(account.__amount))
# print('利率{0}'.format(Account.__interest_rate))

# 私有方法


class Account:
	__interest_rate = 0.0568

	def __init__(self,owner,amount):
		self.owner = owner
		self.__amount = amount
	
	def __get_info(self):
		return"{0}金额：{1}利率：{2}".format(self.owner,self.__amount,Account.__interest_rate)

	def desc(self):
		print(self.__get_info())


account = Account('tony',800000.0)
account.desc()
# account.__get_info()

class Dog:


	def __init__(self,name,age,sex='雌性'):
		self.name = name
		self.__age = age


	def run(self):
		print("{}正在跑。。。".format(self.name))

	def get_age(self):
		return self.__age


	def set_age(self,age):
		self.__age = age


dog = Dog('球球',2)
print('狗狗年龄{}'.format(dog.get_age()))
dog.set_age(3)
print('修改后的狗狗年龄{}'.format(dog.get_age()))


class Dog:


	def __init__(self,name,age,sex='雌性'):
		self.name = name
		self.__age = age


	def run(self):
		print("{}正在跑。。。".format(self.name))

# 	@property
# 	def age(self):
# 		return self._age
	
# 	@age.setter
# 	def age(self,age):
# 		self.__age = age

# dog = Dog('球球',2)
# print('狗狗年龄{}'.format(dog.age)

# dog.age(3)

# print('修改后的狗狗年龄{}'.format(dog.age)


class Animal:

	def __init__(self,name):
		self.name = name

	def show_info(self):
		return"动物的名字:{0}".format(self.name)

	def move(self):
		print("动一动。。。")

class Cat(Animal):

	def __init__(self,name,age):
		super().__init__(name)
		self.age = age

cat = Cat('tom',2)
cat.move()
print(cat.show_info())


class Horse:
	def __init__(self, name):
		self.name = name

	def show_info(self):
		return "马的名字：{0}".format(self.name)

	def run(self):
		print("马跑。。。")

class Donkey:
	def __init__(self,name):
		self.name = name

	def show_info(self):
		return "驴的名字：{0}".format(self.name)

	def run(self):
		print("驴跑。。。")

	def roll(self):
		print("驴打滚。。。")


class Mule(Horse,Donkey):

	def __init__(self,name,age):
		super().__init__(name)
		self.age = age

m = Mule('骡宝莉',2)
m.run()
m.roll()
print(m.show_info())






