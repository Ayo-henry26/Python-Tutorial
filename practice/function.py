import platform
from multiprocessing.managers import Array

import dunners as dun
import math
import json
#from dunners import person


#Object-Oriented Programming in Python (OOP)
#CLASSES AND OBJECTS
class myClass:
    x = 5
p1 = myClass()
print(p1.x)

#Using the __init__() Method
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
detail = person("Henry", 19)
print(detail.name)
print(detail.age)
detail.age = 20
print(detail.age)
#You can you the del keyword to delete an entire object

#Using the __str__() method
class school:
    def __init__(self, name, year):
        self.name = name
        self.year = year
    def __str__(self):
        return f"The name of this school is {self.name} and it was founded in {self.year}"
status = school("University of Ilorin", 1975)
print(status)

#Creating your own method
class company:
    def __init__(self, name, department):
        self.name = name
        self.department = department
    def myfunc(self):
        print(self.name, self.department)
off = company("MicroSoft", "IT")
off.myfunc()

#Inheritance
#Base class / Parent class
class Samsung:
    def __init__(self, model, year):
        self.model = model
        self.year = year
    def display_info(self):
        print(f"Samsung {self.model} was released in {self.year}")
#Derived class / Child class
class Sam(Samsung):
    #pass
#OR
    def __init__(self, model, year):#You can add the series here and just call the property
        # Samsung.__init__(self, model, year)
#OR
        super().__init__(model, year)
        #To add new properties when using the super()
        self.series = "S_Series"#Call the property here
    #Adding a method (like display_info)
    def welcome(self):
        print(f"I am the first person to buy Samsung {self.series} in {self.year}")
x = Sam("Galaxy S25 Ultra", 2025)#Add the property value here
# print(x.series)
# x.display_info()
x.welcome()

#ITERATORS using __iter__() and __next__()
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)
print(next(myit))
print(next(myit))
print(next(myit))
#Using for loop
for x in mytuple:
    print(x)

#Using the class and object to iterate
class myNumber:
    def __iter__(self):
        self.a = 1
        return self
    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration
myclass = myNumber()
myiter = iter(myclass)
for _ in myiter:
    print(_)

#Polymorphism (many forms) refers to methods, functions, operators with the same name that can be executed on
# many objects or classes
#len()
txt = "Hello World"
print(len(txt))
mylist = ["apple", "banana", "cherry"]
print(len(mylist))
#Class and Object
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Sail!")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def move(self):
        print("Fly!")
Car1 = Car("Ford", "Mustang")
Boat1 = Boat("Ibiza", "Touring 20")
Plane1 = Plane("Boeing", "747")
for _ in (Car1, Boat1, Plane1):
    _.move()

#Using Inheritance
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def move(self):
        print("Drive!")
class car(Vehicle):
    pass
class boat(Vehicle):
    def move(self):
        print("Sail!")
class plane(Vehicle):
    def move(self):
        print("Fly!")
car1 = car("Ford", "Mustang")
boat1 = boat("Touring 20", "Mustang")
plane1 = plane("Boeing", "747")
for _ in (car1, boat1, plane1):
    print(_.make)
    print(_.model)
    _.move()

#MODULES: Using the 'import' keyword to import the dunners.py and the 'as' keyword to create an alias for dunners
#'from' keyword is used to import only a specified part of the module
#print(person["age"])
x = platform.system() #To show the OS been used on your system
print(x)

dun.greeting("Henry")

a = dun.person
print(a)
#The dir() is used to examine an object properties
b = dir(dun)
print(b)


#MATH: Python has a set of built-in math functions, including an extensive math module, that allows you
#to perform mathematical tasks on numbers
#The min() and max() used to find the lowest and highest value in an iterable
p = (5, 10, 15, 20)
q = (10, 20, 30, 40)
print(min(p))
print(max(q))
#The abs() is used to return any value as a positive value
x = abs(-100)
print(x)
#The pow(value, index) is used to return the value raised to the power of the index
y = pow(25, 3)
print(y)
#The sqrt() is used to find the square root of a value
z = math.sqrt(625)
print(z)
r = math.ceil(23.4) #It round up the value
s = math.floor(23.9) #It round down the value
t = math.pi
print(r)
print(s)
print(t)

#JSON in Python
#Converting JSON to Python by using the loads() method
txt = '{"name" : "Henry", "age" : 25, "roll_number" : 76}'
txt2 = json.loads(txt)
print(txt2)
print(type(txt))
print(type(txt2))
#Converting Python to JSON by using the dumps() method
text = {"name" : "Henry", "age" : 25, "roll_number" : 76}
text1 = json.dumps(text)
print(text)
print(type(text))
print(type(text1))
#Conversion between python and JSON
  # Python                    |         JSON
  #      dictionary           |       Object
  #      list                 |       Array
  #      tuple                |       Array
  #      int                  |       Number
  #      float                |       Number
  #      str                  |       String
  #      True                 |       true
  #      False                |       false
  #      None                 |       null

x = {
    "name" : "Play",
    "age" : 36,
    "married" : False,
    "divorced" : False,
    "children" : None,
    "pets" : ("cat", "dog"),
    "cars" : [
        {"model" : "Dodge Charge", "year" : 2025},
        {"model" : "Lamborghini Revuelto", "year" : 2025}
    ]
}
#indent is used as a line breaker for the JSON result
#seperators is used to show the format of how it is organized usually in (", ", " : ") format
#sort_keys if True set the order of the dictionary / object alphabetically in ascending order
print(json.dumps(x,indent=4, sort_keys=True))
# print(json.dumps(x,indent=4, separators=(". ", " = ",)))


