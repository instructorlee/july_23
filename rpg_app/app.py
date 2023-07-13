import random
from classes.food import Food
from classes.player import Player

player = Player("Fred")

is_playing = True

print(f"Welcome to the game, {player.name}!")
print("Type 'help' for a list of commands.")

while is_playing:

    print(f"\nYour strength is {player.strength}.")
    command = input("Enter a command: ")

    if command == "quit":
        is_playing = False

    elif command == "help":
        print("\nAvailable commands:")
        print("\nquit - quits the game")
        print("help - prints this help message")

    elif command == "walk":
        """
            choose a direction
            distance / speed
            energy / health reduction
            feedback - you walked
        """

        direction = input("Which direction? (e, w, n, s): ") # enter 1 letter

        # validate data
        if direction not in "ewns":
            print("\nYou can't walk that way!")
            continue

        print(
            "\nYou walk "
            + {
                "e": "East", 
                "w": "West", 
                "n": "North",
                "s": "South"
            }[direction]
        )

        if player.walk() == 0:
            print("You Died")

        print("You see a dark, cold void.")

    else:
        print("\nUnknown command")

print("Thanks for playing!")
