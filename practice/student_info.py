class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number
    def display_info(self):
            print(f"Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}")
         
name = input("Enter Your Name: ")
age = int(input("Enter Your Age: "))
roll_number = int(input("Enter Your Roll Number: "))

Student1 = Student(name, age, roll_number)

print("\nStudent Information: ")
Student1.display_info()