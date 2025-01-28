import random

# Initialize scores
rock_paper_scissors_wins = 0
guess_the_number_wins = 0

while True:
    print("\nWelcome to the Classic Games!")
    print("\nChoose what game you want to play!")
    print("1. Rock-Paper-Scissors")
    print("2. Guess the Number")
    print("3. *Quit Game*")

    user_choice = input("\nChoose a game (1-2 or 3 to quit): ")
    
    if user_choice == '1':
        # Play the Rock, Paper, Scissors game
        user_wins = 0
        computer_wins = 0

        options = ["rock", "paper", "scissors"]

        # Welcome messages
        print("\nWelcome to the Game of Rock-Paper-Scissors!")
        print("\nType 'rock', 'paper', or 'scissors' to play.")
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

        print("\nYou won!", user_wins, "times.")
        print("The computer won!", computer_wins, "times.")
        rock_paper_scissors_wins += user_wins  # Update the total wins for the scoreboard
        # testing

    elif user_choice == '2':
        # Play the Guess the Number Game
        number_to_guess = random.randint(1, 100)
        attempts = 0

        print("\nWelcome to the game of Guess the Number!")
        print("\nI'm thinking of a number between 1 and 100.")
        print("What number must it be?")

        while True:
            user_guess = input("Enter your guess (or 'q' to quit): ")
            if user_guess.lower() == 'q':
                print("Goodbye!")
                break

            attempts += 1
            user_guess = int(user_guess)

            if user_guess < number_to_guess:
                print("\nToo low! Try again.")
            elif user_guess > number_to_guess:
                print("\nToo high! Try again.")
            else:
                print(f"\nCongratulations! You've guessed the number {number_to_guess} in {attempts} attempts.")
                guess_the_number_wins += 1  # Update total wins
                break

    elif user_choice == '3':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

# Display scoreboard
print("\n--- Scoreboard ---")
print(f"Rock-Paper-Scissors Wins: {rock_paper_scissors_wins}")
print(f"Guess the Number Wins: {guess_the_number_wins}")
print("Good bye! See you next time!")        