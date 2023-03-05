# NEKO-NEKO
NEKO-NEKO is a text-based adventure game about taking care of a needy cat. The game is played in the terminal and the player's goal is to keep the cat happy by responding to its changing moods with different actions.

## Gameplay

The game starts with the player being given a random starting mood for the cat. There are four possible moods: mad, wild, hungry, bored, and sleepy. The player will then be given a hint, chosen randomly from a pool for that mood, and must choose an action in response. Each action will either increase or decrease the cat's mood.

### The available actions are:
    (f)eed: Give the cat food.
    (l)eave alone: Leave the cat alone.
    (o)utside: Let the cat outside.
    (p)lay: Play with the cat.
    (s)nuggle: Snuggle with the cat.
    (q)uit: End the game.

The player must enter a lowercase letter corresponding to the action they wish to do. This is then run through an input validation function to ensure only 'f', 'p', 's', 'l', 'o' or 'q' is entered. If not, the player is prompted to enter a lowercase letter and can try again. If they enter 'q', the program terminates.

If the player chooses the correct action based on the cat's mood, the cat's mood will increase by one point. If the player chooses an incorrect action, the cat's mood will decrease by one point.

The game ends when the cat's mood reaches either 0 or 56. If the mood reaches 0, the cat runs away and the game is over. If the mood reaches 6, the cat is happy and the player wins the game. At this point, the player can choose to either replay the game (with a random starting mood and random hints, for variability), or end the program.

## Installation and Usage

NEKO-NEKO requires Python 3 to run. To play the game, simply download or clone the repository, navigate to the game's directory in your terminal, and run the main.py file with Python. Or, you can play it directly on [Replit](https://replit.com/@aclongo/cat-adventure?v=1).

Follow the on-screen instructions to play the game.
