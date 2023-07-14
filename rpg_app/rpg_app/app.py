import random
from classes.food import Food
from classes.player import Player
from classes.weapon import Weapon

player = Player("Fred")

is_playing = True

available_weapons = [
    ("sword", 10, 2),
    ("shield", 4, 6),
    ("chain mail", 0, 4),
    ("axe", 15, 2),
    ("bow", 5, 0),
    ("dagger", 3, 0),
    ("mace", 12, 2),
]

available_foods = [  # TUPLES!
    ("apple", 5),
    ("bread", 10),
    ("ale", 12),
    ("cheese", 8),
]

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

        roll = random.randint(1, 10)

        if roll < 0:
            pass # attacker

        elif roll < 0:
            pass # food

        elif roll < 11: # find a weapon
            weapon_choice = available_weapons[random.randint(0, len(available_weapons) - 1)]
            weapon = player.add_weapon(Weapon(weapon_choice[0], weapon_choice[1], weapon_choice[2]))
            print(f"\nYou found {weapon.name}!")

        else:
            print("You see a dark, cold void.")

    elif command == "list food":
        pass

    elif command == "eat":
        # will need a follow up question?
        pass

    elif command == "list weapons":
        
        print("\nYou have the following weapons:")

        if len(player.weapons) == 0:
            print("You have no weapons! Run!")

        else:
            for weapon in player.weapons:
                print(f"{weapon.name} - {weapon.damage} / {weapon.defense}")

    else:
        print("\nUnknown command")

print("Thanks for playing!")
