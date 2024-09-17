import random

'''
1 for Rock
-1 for Paper
0 for Scissors
'''

# Randomly choosing for the computer
computer = random.choice([1, -1, 0])

# User input
you_str = input("Enter your Choice (r for Rock, p for Paper, s for Scissors): ").lower()

# Dictionaries to convert user input and computer's choice to meaningful terms
youdict = {"r": 1, "p": -1, "s": 0}
reverse_dict = {1: "Rock", -1: "Paper", 0: "Scissors"}

# Input validation
if you_str not in youdict:
    print("Invalid input! Please enter 'r', 'p', or 's'.")
else:
    # Assigning the user choice from the dictionary
    you = youdict[you_str]

    # Displaying the choices
    print("******************")
    print(f"You chose: {reverse_dict[you]}")
    print(f"Computer chose: {reverse_dict[computer]}")
    print("******************")

    # Game logic
    if computer == you:
        print("It's a draw!")
    else:
        # Checking all possible win/lose conditions
        if computer == -1 and you == 1:  # You: Rock, Computer: Paper
            print("You Win! Congratulations")
        elif computer == -1 and you == 0:  # You: Scissors, Computer: Paper
            print("You Win! Congratulations")
        elif computer == 1 and you == -1:  # You: Paper, Computer: Rock
            print("You lose! Try again")
        elif computer == 1 and you == 0:  # You: Scissors, Computer: Rock
            print("You lose! Try again")
        elif computer == 0 and you == -1:  # You: Paper, Computer: Scissors
            print("You lose! Try again")
        elif computer == 0 and you == 1:  # You: Rock, Computer: Scissors
            print("You Win! Congratulations")
        else:
            print("Something went wrong! Try again.")
