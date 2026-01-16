class Student_info:
    def __init__(self, name, age, matric_number):
        self.name = name
        self.age = age
        self.matric_number = matric_number
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Matric Number: {self.matric_number}")
        
name = input("Enter your name: ")
age = int(input("Enter your age: "))
matric_number = input("Enter your matric number: ")

Student = Student_info(name, age, matric_number)
Student.display_info()