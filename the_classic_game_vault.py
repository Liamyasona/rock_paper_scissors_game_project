import random

while True:
    print("\nWelcome to the Classic Games!")
    print("1. Rock-Paper-Scissors")
    print("2. Guess the Number")
    print("3. Quit")


user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

# Welcome messages
print("Welcome to the Game of Rock-Paper-Scissors!")
print("Type 'rock', 'paper', or 'scissors' to play.")
print("Type 'q' to quit the game.")

while True:
    user_input = input("Your choice: ").lower()
    if user_input == "q": 
        break

    if user_input not in options:
        print("Invalid input. Please try again.")
        continue
    
    # Program picks their choice
    random_number = random.randint(0, 2)
    
    # rock: 0, paper: 1, scissors: 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You won!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("You won!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("You won!")
        user_wins += 1

    elif user_input == computer_pick:
        print("It's a draw!")

    else:
        print("You lost!")
        computer_wins += 1

print("You won!", user_wins, "times.")
print("The computer won!", computer_wins, "times.")
print("Goodbye!")
# testing
