class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

person1 = Person("John", 30)
person1.greet()

person2 = Person("ALice", 27)
person2.greet()


class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

    def say_hello(self, user):
        print(
            f"Sending message to {user.username}, Yoooo {user.username}, it's {self.username}"
            )
        
user1 = User("Ghost", "ghost@gmail.com", "ghost23")
user2 = User("Shadow", "shadow,@gmail.com", "shadow45")

user1.say_hello(user2)