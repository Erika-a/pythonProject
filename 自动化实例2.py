import pyautogui
import time


# while True:
#     time.sleep(1)
#     pyautogui.moveRel(0,1)
#     time.sleep(1)
#     pyautogui.moveRel(1,0)
#     time.sleep(1)
#     pyautogui.moveRel(-1,0)
#     time.sleep(1)
#     pyautogui.moveRel(0,-1)
#
#


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting")

    def roll_over(self):
        print(f"{self.name} roll_over")


my_dog = Dog('willie', 6)

print(f"My dog name is {my_dog.name}")
print(f"My dog is {my_dog.age} years old")

my_dog.sit()
my_dog.roll_over()


class Restaurant:

    def __init__(self, restaurant_name, cuisine_tybe):
        self.restaurant_name = restaurant_name
        self.cuisine_tybe = cuisine_tybe
        self.number_served = 0

    def describe_restaurant(self):
        print(f"{self.restaurant_name} {self.cuisine_tybe}")

    def open_restaurant(self):
        print(f"{self.restaurant_name}is open now")

    def re_staurant(self):
        print(f"{self.number_served} 人经过这家餐厅")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number2):
        self.number_served += number2


rt1 = Restaurant('兰州拉面', '面')
print(f"{rt1.describe_restaurant()}\n{rt1.open_restaurant()}")
rt1.re_staurant()
rt1.set_number_served(5)
rt1.re_staurant()
rt1.increment_number_served(7)
rt1.re_staurant()
rt2 = Restaurant('沙县小吃', '粉')
print(f"{rt2.describe_restaurant()}\n{rt2.open_restaurant()}")
rt2.re_staurant()
rt2.set_number_served(7)
rt2.re_staurant()
rt2.increment_number_served(9)
rt2.re_staurant()
rt3 = Restaurant('安徽板面', '面')

print(f"{rt3.describe_restaurant()}\n{rt3.open_restaurant()}")


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer = 0

    def get_descriptive_name(self):
        long_name = f"{self.year}{self.make}{self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer} miles on it ")

    def update_odometer(self, mileage):
        self.odometer = mileage

    def increment_odometer(self, miles):
        self.odometer += miles


my_new_car = Car('audi', 'a4', 2019)

print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(23_500)

my_new_car.read_odometer()

my_new_car.increment_odometer(100)

my_new_car.read_odometer()

import random


class Die:

    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):
        for i in range(10):
            print(random.randint(1,self.sides))

#
# rd = Die(20)
# rd.roll_die()


class Cp:

    def __init__(self):
        self.number = ['0','1','2','3','4','5','6','7','8','9','10']
        self.zimu = ['a','b']

    def cp(self):
        inzm = input("输入你的彩票号码：\n").split(',')
        list = []
        for i in range(2):
            list += random.choice(self.number)
        for i in range(2):
            list += random.choice(self.zimu)

        if inzm == list:
            print(inzm)
            print(list)
            print("彩票中了")

        else:
            print(inzm)
            print(list)
            print("彩票没中")

    def cp2(self):
        inzm = []
        list = []
        cs = 0

        while True:
            for i in range(1):
                list.append(random.choice(self.number))
            for i in range(2):
                list.append(random.choice(self.zimu))

            for i in range(1):
                inzm.append(random.choice(self.number))
            for i in range(2):
                inzm.append(random.choice(self.zimu))


            if inzm == list:

                print(inzm)
                print(list)
                print(f"彩票经过{cs + 1}次中了")
                break

            else:
                cs += 1
                # time.sleep(0.1)
                print(inzm)
                print(list)
                print(f"彩票{cs}次没中,继续循环")
                inzm.clear()
                list.clear()

    def list(self):
        print(self.number)
        print(self.zimu)
        print(self.number + self.zimu)


cp = Cp()

cp.cp2()

