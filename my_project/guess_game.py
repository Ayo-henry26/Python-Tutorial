import random
#MY SECOND TRY
number = random.randint(1, 100)
attempts = 0
while True:
    attempts += 1
    guess = input("Enter your guess? ")
    if guess.isdigit():
        guess = int(guess)
        if guess == number:
            print(f"You guessed the correct number in {attempts} attempts")
            break
        elif guess > number:
            print("Try again, Too High")
        else:
            print("Try again, Too Low")
    else:
        print("Enter a number valid number")


#VIDEO SOLUTION
# import random
# number = random.randint(0, 100)
# while True:
#     try:
#         guess = int(input("Enter your guess? "))
#         if guess < number:
#             print("Too low, Try again")
#         elif guess > number:
#             print("Too high, Try again")
#         else:
#             print("Congratulations, You guessed the right number")
#             break
#     except ValueError:
#        print("Enter a valid number")

#MY FIRST TRY
# import random
# number = random.randint(0, 100)
# attempts = 0
# while True:
    # guess = int(input("Enter your guess? "))
    # attempts += 1
    # if guess == number:
    #     print(f"You guess the correct number in {attempts} attempts")
    #     break
    # elif guess > number:
    #     print("Too high, Try again")
    # else:
    #     print("Too low, Try again")