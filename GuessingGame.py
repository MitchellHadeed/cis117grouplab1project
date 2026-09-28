"""
Lab 1
Group #6
Author: Georgy Kuxin
Date: Sep 28, 2026
"""
import random

def guessing_game():
    """
    Plays a guessing game where the user has to guess a randomly generated number between 1 and 100. The user has 5 tries to guess the number correctly. After each guess, the program tells the user if their guess was to high or too low. If the user guesses the numebr correctly then the function tells the user they win otherwise it asks them if they want to play again.
    Author: Georgy Kuxin
    """
    play = "Y"

    while play == "Y":
        print("I'm thinking of a number between 1 and 100.")
        tries = 5
        number = random.randint(1,100)

        while tries > 0:
            guess = int(input("Guess what it is again: "))

            if guess == number:
                print("You got it!")
                break

            tries -= 1

            if tries == 0:
                print("Nope! You lost. The number was " + str(number))

            elif guess < number:
                print("Nope! Too low. Try again (" + str(tries) + " tries left).")

            else:
                print("Nope! Too high. Try again (" + str(tries) + " tries left).")

        play = input("Do you want to play again? (Y/N): ")

    print("Thanks for playing!")

if __name__== "__main__":
    guessing_game()
