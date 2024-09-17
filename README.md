
# Rock, Paper, Scissors - Python Game 🎮✊📄✂️

This project is a simple yet classic **Rock, Paper, Scissors** game implemented in Python. The player competes against the computer by selecting either Rock, Paper, or Scissors, and the winner is determined based on traditional game rules.

## How the Game Works:

- **Rock beats Scissors** ✊ > ✂️
- **Scissors beats Paper** ✂️ > 📄
- **Paper beats Rock** 📄 > ✊
- If both the player and computer choose the same, it results in a draw.

## Game Features:

- Interactive command-line interface.
- Randomized computer choices.
- Clear win/loss/draw outcomes displayed to the player.

## Code Overview:

```python
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
```

## How to Play:

1. **Clone or download** this repository to your local machine.
2. **Run** the Python script:
    ```bash
    python rock_paper_scissors.py
    ```
3. When prompted, **enter your choice**:
    - `r` for Rock
    - `p` for Paper
    - `s` for Scissors
4. The game will compare your choice with the computer's and display the result (win, lose, or draw).

## Requirements:

- **Python 3.x** installed on your system.

## Future Improvements:

- Add a score tracker for multiple rounds.
- Implement a graphical user interface (GUI) for better user experience.
- Add the ability to replay the game without restarting the script.

## License:

This project is open-source under the MIT License. Feel free to modify and distribute as you like!
