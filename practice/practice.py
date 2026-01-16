import functools


def countries(country = "Japan"):
    print("One of the best country in the world is " + country)
countries("USA")
countries("Russia")
countries()
#Passing a list through argument
def food(eat):
    for x in eat:
        print(x)
fruits = ["apple", "banana", "orange"]
food(fruits)
#You first find the recalled function value and use it to find the result
def tri_recursion(k):
    if k > 0:
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
tri_recursion(7)
#Decorators
def changecase(casing):
    def inner():
        return casing().upper()
    return inner
@changecase
def my_result():
    return "I want you all to be uppercase"
print(my_result())

#Argument in decoratored function
def up_case(new):
    def up(x):
        return new(x).upper()
    return up
@up_case
def new_case(name):
    return "Hello " + name
print(new_case("Ayomide"))

#When you don't know the number of argument you are passing use *args, **kwargs
def up_case(new):
    def up(*args, **kwargs):
        return new(*args, **kwargs).upper()
    return up
@up_case
def new_case(name):
    return "Hello " + name
print(new_case("Henry"))

#A decorator can accept it's own and transforms the casing based on the argument value
def changecase(n):
    def changecase(func):
        def myinner():
            if n == 1:
                a = func().lower()
            else:
                a =func().upper()
            return a
        return myinner
    return changecase
@changecase(1.)
def new_case():
    return "Hello Ayomide"
print(new_case())
#Multiple Decorators
def sci(func):
    def inner():
        return func().upper()
    return inner
def art(func):
    def inner():
        return func() + " remember, you will be the greatest"
    return inner
@sci
@art
def my_function():
    return "Ayohenry"
print(my_function())

#This is to call the name of your function
def myFunction():
    return "Have a good day"
print(myFunction.__name__)

#Calling a function name when using a decorator
def myFunction(func):
    @functools.wraps(func)
    def inner():
        return func().upper()
    return inner
@myFunction
def my_function():
    return "Have a good day"
print(my_function.__name__)