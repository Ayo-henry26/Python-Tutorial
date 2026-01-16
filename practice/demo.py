import re
import cowsay
cowsay.dragon("Good Morning")
# #Mutable and Immutable
# #Immutable types - str, int, float, bool, byte, tuple
# #Mutable types - list, set, dictionary and some third party libraries
# #IMMUTABLE EXAMPLES
# x= (1, 2)
# y = x
# x = (1, 2, 3)
# print(x, y)
# #MUTABLE EXAMPLES
# x = [1, 2]
# y = x
# x = [1, 2, 3]
# print(x, y)
# def complicated_function(a, b, c = True, d = False):
#     print(a, b, c, d)
#     pass
# complicated_function(*[1, 2], **{"c" : "Hello", "d" : "Dude"})
#
# if __name__ == "__main__":
#     print("run")
#
# #LAMBDA
# x = lambda a : a + 6
# print(x(6))
#
# y = lambda p, q : p * q
# print(y(5, 6))
#
# #Using la,bda in a function
# def myfunc(n):
#     return lambda x: n * x
# mydoubler = myfunc(2)
# mytripler = myfunc(3)
# print(mydoubler(13))
# print(mytripler(13))

# class Student:
#     def __init__(self, name, age, matric_no):
#         self.name = name
#         self.age = age
#         self.matric_no = matric_no
#     def display_info(self):
#         print(f"Your name is {self.name}, age is {self.age} and your matric no is {self.matric_no}")
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))
# matric_no = input("Enter your matric no: ")
# student = Student(name, age, matric_no)
# student.display_info()

class Counter:
    def __init__(self):
        self.value = 1
    def count_up(self):
        self.value += 1
    def count_down(self):
        self.value -= 1
    def __str__(self):
        return f"Value is: {self.value}"
    def __add__(self, other):
        if isinstance(other, Counter):
            return self.value + other.value
        raise Exception("Invalid Type")
count1 = Counter()
count2 = Counter()

count1.count_up()
count2.count_up()

print(count1, count2)
print(count1 + count2)


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def __str__(self):
        return f"{self.make} {self.model} {self.year}"
    def __repr__(self):
        return f"Make : {self.make}, Model : {self.model}, Year : {self.year}"
car = Car("Dodge", "Charger", 2025)
print(str(car))
print(repr(car))


#RegEx: Regular Expression is a sequence of characters that forms a search pattern and can be
#used to check if a string contains the specified search pattern.
text = "This beauty is from Spain"
x = re.search("^The.*Spain$", text)
print(x)
if x:
    print("Yes, It match")
else:
    print("No information seen")

# pattern = "[a-zA-Z0-9]+@[a-zA-Z]+.(com|net|org)"
#
# while True:
#     user_input = input("Enter your email: ")
#     if user_input != '':
#         if (re.search(pattern, user_input)) is not None:
#             print("Valid Email")
#             break
#         else:
#             print("Invalid Email, Enter a valid email")
#     else:
#         print("You didn't input anything")


#The try, except, and finally statement and else statement with them
# i = 10
try:
    print(i)
except:
    print("An Exception occurred")
#You can have multiple except statement
else:
    print("Nothing went wrong")
finally:
    print("If it doesn't work, try giving it a value")

#Real life example of try...except
try:
    f = open("test.txt")
    try:
        f.write("Python is the best")
    except:
        print("Something went wrong when writing the file")
    finally:
        f.close()
except:
    print("Something went wrong in opening the file")

#raise keyword
num = -1
if num < 0:
    raise Exception("Number needs to be positive")

st = "-1"
if not type(st) is int:
    raise TypeError("Number needs to be an integer")

