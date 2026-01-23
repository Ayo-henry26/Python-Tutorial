import random
while True:
    roll = input("Will you like to roll the dice (Y/n)").lower()
    if roll == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f"({die1}, {die2})")
    elif roll == 'n':
        print("Thanks for playing")
        break
    else:
        print("Invalid roll")