"""
 CLI - Command Line Interface
"""
import random

is_playing = True

while is_playing :

    print(random.randint(1, 10))
    response = input("\nWhat is your name? ")

    if response.lower() == "quit":
        is_playing = False
    
    else:
        print(f"Hello {response}!")

print("Have a nice day!")

"""
    Requirements:
        - User enters their guess
        - User is told if their guess is too high or too low
            - continue guessing
        - User is told if they guessed correctly
            - print total number of guesses
            - end game
            - Thank the user for playing
"""