"""Choosing your own adventure game."""

__author__ = "730476042"

# Taking care of a virtual pet like a tamagotchi. You are free to introduce additional variables, global or otherwise, for keeping track of a pet’s health.
from hashlib import new
import random

def greet() -> None:
    global player
    """Greet function to introduce user to game."""
    print("Welcome to Azaii: A solo Player game where you must survive the trecherous condtions of Azaii and make your way to the safety of Port Larco.")

    player = str(input("He who dares step foot on the sacred island of Azaii, State your Name: "))

    print(f"Welcome to Azaii, {player}.")


def path_of_snakes() -> None:
    """A direction the player can choose to take."""
    global points
    print("So you have decided to take the path of snakes.")
    print(input("Are you ready? "))
    print(f"Very well, I bid you good luck {player}.")

    opponents: list[str] = ["tiger", "wolf", "gorilla", "monkey"]
    opps_size: int = random.randint(3, 7) 
    i: int = 0
    game: list[str] = ["Heads", "Tails"]

    print(f"The path has chosen for you to encounter {opps_size} enemies. The enemy will flip a coin and you must guess if it is Heads or Tails. Every right guess is 2.0 points and every wrong guess is -0.5 points.")

    while i < opps_size:
        opp: str = random.choice(opponents)
        opp_choice = random.choice(game)
        user_guess = str(input(f"A wild {opp} has appeared. They have flipped a coin. What is you guess: Heads or Tails? "))

        while user_guess != game[0] or game[1]:
            new_guess = str(input(f"What is your guess: Heads or Tails? "))
            user_guess = new_guess


        if user_guess == opp_choice:
            points += 1.0
            print(f"Shucks, it was a lucky guess for {player}.")
        else:
            points -= 0.5
            print((f"Hahahaa, {opp_choice} will always win!!!"))

        i += 1

        




def main() -> None:
    """Main game function and entrypoint of Adventure."""
    points: float = 0.0
    player: str = ""
        # greet player first
        # enter experience
        # present player with 3 options
        # 1/3 options must be to end experience with goodbye message including points
        # 2/3 options result in function calls setting player off in different directions


if __name__ == "__main__":
    main()