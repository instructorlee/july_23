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

    else:
        print("\nUnknown command")

print("Thanks for playing!")
