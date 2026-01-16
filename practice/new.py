import time
import random
# print(random.random()) for creating floating point
print(random.randrange(1, 3)) # for picking whole number
print(random.uniform(1, 10)) #for picking a floating point

# Simulating a progress bar
for i in range(1, 101):
    print(f"\rProgress: {i}%", end="", flush=True)
    time.sleep(0.05)



if 1 > 2:
  print("Know your place")
else:
  print("You are not as big as you claim")

y = "In order to succeed you must know God"
index = y.find("God")
# index = y.find("Ayo") output is -1 because Ayo is not in the string
print(index)

rows = int(input("Enter the number of rows: "))
k = 0
for i in range(1, rows + 1):
    # Print spaces
    for j in range(1, (rows - i) + 1):
        print(end=" ")
    # Print asterisks
    while k != (2 * i - 1):
        print("*", end="")
        k = k + 1
    k = 0
    print()
