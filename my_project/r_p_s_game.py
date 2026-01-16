# #MY OWN VERSION
import random
# def r_p_s():
#     options = ("Rock", "Paper", "Scissors")
#     while True:
#         ccomputer_choice = random.choice(options)
#         choice = input("Rock, Paper, Scissors? (r/p/s)").lower()
#         if choice == 'r':
#             print("You chose Rock")
#             print(f"Computer chose {ccomputer_choice}")
#             if ccomputer_choice == "Scissor":
#                 print("You Win")
#                 break
#             elif ccomputer_choice == "Paper":
#                 print("You Lose")
#                 break
#             else:
#                 print("It's a tie\nPlay Again")
#         elif choice == 'p':
#             print("You chose Paper")
#             print(f"Computer chose {ccomputer_choice}")
#             if ccomputer_choice == "Rock":
#                 print("You Win")
#                 break
#             elif ccomputer_choice == "Scissors":
#                 print("You Lose")
#                 break
#             else:
#                 print("It's a tie\nPlay Again")
#         elif choice == 's':
#             print("You chose Scissors")
#             print(f"Computer chose {ccomputer_choice}")
#             if ccomputer_choice == "Paper":
#                 print("You Win")
#                 break
#             elif ccomputer_choice == "Rock":
#                 print("You Lose")
#                 break
#             else:
#                 print("It's a tie\nPlay Again")
#         else:
#             print("Invalid Choice")
# r_p_s()
# def play_again():
#     while True:
#         continue_game = input("Continue (y/n)").lower()
#         if continue_game == 'y':
#             r_p_s()
#         elif continue_game == 'n':
#             print("Thanks for playing")
#             break
#         else:
#             print("Invalid input")
# play_again()

#MY SECOND TRIAL 
# choices = ('r', 'p', 's')
# full_choices = {
#     'r' : '🪨',
#     'p' : '📃',
#     's' : '✂️'
# }
# while True:
#     user_choice = input("Rock, Paper, Scissor(r/p/s)")
#     if user_choice not in choices:
#         print("Invalid Choice")
#         continue

#     computer_choice = random.choice(choices)

#     print(f"You chose {full_choices[user_choice]}")
#     print(f"Computer chose {full_choices[computer_choice]}")

#     if user_choice == computer_choice:
#         print("It's a tie")
#     elif(
#         (user_choice == 'r' and computer_choice == 's') or
#         (user_choice == 's' and computer_choice == 'p') or
#         (user_choice == 'p' and computer_choice == 'r')
#     ):
#         print("You win")
#     else:
#         print("You lose")
#     play_again = input("Continue (y/n)").lower()
#     if play_again == 'n':
#         print("Thanks for playing")
#         break

#THIRD TRIAL USING MODULARIZAION (FUNCTION)
ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
full_choices = {
    'r' : '🪨',
    'p' : '📃',
    's' : '✂️'
}
choices = tuple(full_choices.keys())

def get_choices():
    while True:
        user_choice = input("Rock, Paper, Scissors? (r/p/s)")
        if user_choice  in choices:
            return user_choice
        else:
            print("Invalid Choice")

def show_results(user_choice, computer_choice):
    print(f"You chose {full_choices[user_choice]}")
    print(f"Computer chose {full_choices[computer_choice]}")

def determine_winnings(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a tie")
    elif(
        (user_choice == ROCK and computer_choice == SCISSORS) or
        (user_choice == SCISSORS and computer_choice == PAPER) or
        (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("You win")
    else:
        print("You lose")
    
def re_play():
    while True:
        user_choice = get_choices()

        computer_choice = random.choice(choices)

        show_results(user_choice, computer_choice)

        determine_winnings(user_choice, computer_choice)

        play_again = input("Will you like to continue?(y/n)").lower()
        if play_again == 'n':
            print("Thanks for playing")
            break
re_play()