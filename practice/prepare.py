x = "God is good"
x = x.replace("good" , "great")
print(x)

firstName = "Ayomide"
lastName = "Laryea"
fullName = (firstName , lastName)
name = " ".join(fullName)
print(name)

name = input("Enter your name: ")
while name == "":
  print("You didn't type anything!")
  name = input("Please Enter your name: ")
print(f"Your name is {name}")