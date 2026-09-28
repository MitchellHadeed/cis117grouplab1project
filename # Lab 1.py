# Lab 1
# Group #: ______
# Authors: Mitchell Hadeed, __________________
# Date: 09/22/2026

import random


def rock_paper_scissors():
    """
    Plays a Rock-Paper-Scissors game!!
    This code randomly chooses paper, scissors, or rock.
    The user typing the code in chooses one of the three options.
    The function determines whether the user wins, loses,
    or ties with the computer.
    """

    play_again = "Y"

    while play_again.upper() == "Y":

        computer = random.randint(1, 3)

        print("\n1. Paper")
        print("2. Scissors")
        print("3. Rock")

        player = int(input("Enter your choice: "))

        if player < 1 or player > 3:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        if computer == 1:
            computer_name = "paper"
        elif computer == 2:
            computer_name = "scissors"
        else:
            computer_name = "rock"

        if player == 1:
            player_name = "paper"
        elif player == 2:
            player_name = "scissors"
        else:
            player_name = "rock"

        print(f"You chose {player_name}.")
        print(f"The computer chose {computer_name}.")

        if player == computer:
            print("It is a tie!")

        elif player == 1 and computer == 3:
            print("You won! Paper covers rock.")

        elif player == 2 and computer == 1:
            print("You won! Scissors cut paper.")

        elif player == 3 and computer == 2:
            print("You won! Rock crushes scissors.")

        elif computer == 1 and player == 3:
            print("You lost! Paper covers rock.")

        elif computer == 2 and player == 1:
            print("You lost! Scissors cut paper.")

        elif computer == 3 and player == 2:
            print("You lost! Rock crushes scissors.")

        play_again = input("Do you want to play again? (Y/N): ")


if __name__ == "__main__":
    rock_paper_scissors()