"""
Lab 12
Let's guess some numbers!
"""

import random

# version 1

print("Welcome to the guessing game! You have 10 guesses.")

computer_guess = random.randint(1, 10)

game_on = True
number_tries = 9

while game_on and number_tries > 0:
    user_guess = input("Guess a number between 1 and 10.\n> ")
    user_guess = int(user_guess)
    if user_guess == computer_guess:
        print("You got it in just " + str(10 - number_tries) + " guesses!")
        game_on = False
    else:
        number_tries -= 1
        print("Wrong! You have " + str(number_tries + 1) + " tries left.\n")

print("Game over.\n")

# version 2

print("Let's try another version of the guessing game! This time you have unlimited guesses.")

computer_guess = random.randint(1, 10)

number_tries = 1

while True:
    user_guess = input("Guess a number between 1 and 10.\n> ")
    user_guess = int(user_guess)
    if user_guess == computer_guess:
        print(f"You got it in just {number_tries} guesses!")
        break
    else:
        number_tries += 1
        print("Wrong! Try again.\n")

print("Game over.\n")

# version 3

print("Let's try another version of the guessing game! This time the computer will help you out.")

computer_guess = random.randint(1, 10)

number_tries = 1

while True:
    user_guess = input("Guess a number between 1 and 10.\n> ")
    user_guess = int(user_guess)
    if user_guess == computer_guess:
        print(f"You got it in just {number_tries} guesses!")
        break
    else:
        number_tries += 1
        if user_guess > computer_guess:
            print("Wrong! Too high!\n")
        else:
            print("Wrong! Too low!\n")

print("Game over.\n")

# version 4

print("Not enough hints before? This version of the game will really help you out.")

computer_guess = random.randint(1, 10)

number_tries = 1
last_guess = 0

while True:
    user_guess = input("Guess a number between 1 and 10.\n> ")
    user_guess = int(user_guess)
    current_guess = user_guess

    if user_guess == computer_guess:
        print(f"You got it in just {number_tries} guesses!")
        break
    else:
        number_tries += 1
        if abs(current_guess - computer_guess) < abs(last_guess - computer_guess):
            print("Wrong! But you're closer than before!\n")
            last_guess = user_guess
        elif abs(current_guess - computer_guess) > abs(last_guess - computer_guess):
            print("Wrong! Now you're getting colder!\n")
            last_guess = user_guess
        elif current_guess == last_guess:
            print("Wrong! Try again.\n")
            last_guess = user_guess
        else:
            print("Wrong! Try again.\n")
            last_guess = user_guess

print("Game over.\n")

# version 5

number_tries = 1

user_guess = int(input("This time, enter a number between 1 and 10 for the computer to guess\n:"))

while True:
    computer_guess = random.randint(1, 10)
    if computer_guess == user_guess:
        print(computer_guess)
        print(f"The computer got it in just {number_tries} guesses!")
        break
    else:
        print(computer_guess)
        number_tries += 1
        continue

print("Game over, human.")