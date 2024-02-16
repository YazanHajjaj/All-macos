# functions

"""def greet_user():
    print("hi there")
    print("welcome aboard")


print("start")
greet_user()
print("finish")


# parameters
def greet_user(first_name, last_name): # these are parameters
    print(f"hi {first_name} {last_name}")
    print("welcome aboard")


print("start")
greet_user("yazan", "hajjaj")
greet_user("hajjaj", "yazan")
print("finish")


# keyword arguments
def greet_user(first_name, last_name):
    print(f"hi {first_name} {last_name}")
    print("welcome aboard")


print("start")
# this a the keyword argument when there is no keyword it is a positional argument
greet_user(last_name="hajjaj", first_name="yazan") # you cant use a keyword argument first
# calc_cost(total=50, shipping=5, discount= 0.5)  #this a case where you use a keyword argument
print("finish")


# return statement

def square(number):
    return number * number


result = square(3)
print(square(3))  # 1st way
print(result)  # 2nd way


# creating reusable functions

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😔"

    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))

# Exceptions
try:
    age = int(input("age:"))
    income = 20000
    risk = income / age
    print(age)
except ZeroDivisionError:
    print("age cant be zero")
except ValueError:
    print("invalid value")"""

# Classes: to defines new types which are numbers strings list booleans ...

"""class Point: # pascal naming convention
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)

point2 = Point()
point2.x = 1


class Point:
    def __init__(self, x, y):  # init is initialize # constructor
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point = Point(10, 20)
print(point.x)


# a function in a class is called a method
class Person:
    def __init__(self, name):  # constructor
        self.name = name

    def talk(self):  # class method
        print(f"Hi i am {self.name}")
        # print("TALK")

# each object is  different instance of the person class
john = Person("yazan") 
# print(john.name)
john.talk()
bob = Person("hajjaj")
bob.talk() 


#  Inheritance  it will have all th method from the main class
class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    def bark(self):
        print("bark")


class Cat(Mammal):
    pass


dog1 = Dog()
dog1.walk()"""

# Modules used to break multiple code
"""
import co
from co import lbs_to_kg


lbs_to_kg(100)
print(co.lbs_to_kg(50))

numbers = [10, 3, 6, 2]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)

from co import find_max

numbers = [10, 3, 6, 2]
maximum = find_max(numbers)
print(maximum)
print(max(numbers))"""""

# packages
"""from ecom import shipping

shipping.calc_shipping()"""

# generating random values
import random

"""for i in range(1):
    print(random.random())
for i in range(3):
    print(random.randint(10, 20))

members = ["a", "b", "c", "g"]
leader= random.choice(members)
print(leader) 


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()
print(dice.roll())"""

# directory

"""from pathlib import Path

path = Path()
# print(path.mkdir())  # mkdir makes a new directory
# print(path.rmdir())  # removes directory
for file in path.glob("*.py"):
    print(file)
for file in path.glob("*"):
     print(file)"""
