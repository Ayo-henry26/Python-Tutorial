import random
def guess_number():
    number = random.randint(1, 100)
    attempts = 0
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        if guess == number:
            print(f"Congrats, You got the guess in {attempts} attempts")
            break
        elif guess < number:
            print("Too low, Try Again")
        else:
            print("Too High, Try Again")
guess_number()