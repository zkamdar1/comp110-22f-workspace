"""Choosing your own adventure game."""

__author__ = "730476042"
 
import random

winner_emoji: str = "\U0001F973"
loser_emoji: str = "\U0001F622"
points: int = 0
player: str = ""


def greet() -> None:
    """Greet function to introduce user to game."""
    global player
    print("Welcome to Azaii: A solo Player game where you must survive the trecherous condtions of Azaii and make your way to the safety of Port Larco.")

    player = str(input("State your Name: "))

    print(f"Welcome to Azaii, {player}.")


def path_of_moon() -> None:
    """A direction the player can choose to take."""
    global points
    print("So you have decided to take the path of moon.")
    input("Are you ready? ")
    print(f"Very well, I bid you good luck {player}.")

    opponents: list[str] = ["tiger", "wolf", "gorilla", "monkey"]
    opps_size: int = random.randint(3, 7) 
    i: int = 0
    game: list[str] = ["Heads", "Tails"]

    print(f"The path has chosen for you to encounter {opps_size} enemies. The enemy will flip a coin and you must guess if it is Heads or Tails. Every right guess is 2 points and every wrong guess is 0 points.")

    while i < opps_size:
        opp: str = random.choice(opponents)
        opp_choice = random.choice(game)
        user_guess = str(input(f"A wild {opp} has appeared. They have flipped a coin. What is you guess {player}: Heads or Tails? "))

        if user_guess == opp_choice:
            points += 2
            print(f"Shucks, it was a lucky guess for {player}. Good job{winner_emoji}!")
        else:
            points -= 0
            print((f"Hahahaa, {opp} will always win!!! Sucks for you {loser_emoji}."))

        i += 1

    if points > opps_size / 2:
        print((f"Congratulations {player}, you have managed to survive the dangers of the path of moon and earned {points} points. Welcome to Port Larco!!!{winner_emoji}"))
    else:
        print(f"You earned {points} points. Seems like you weren't cut out for the path of moon {player}. Come back soon{loser_emoji}!")


def path_of_sun(sun_points: int) -> int:
    """Another direction the player can choose to take.""" 
    print(f"The path of sun welcomes you {player}.")

    question_one: int = int(input("Please choose a number between 1 and 10......Choose carefully, your future is at stake. "))

    if question_one >= 5:
        print(f"Very well {player}, you have earned 3 points{winner_emoji}. Good luck with the next question.")
        sun_points += 3
    elif question_one < 5:
        print(f"It seems the odds are against you {player}. You will gain no points{loser_emoji}. May you have better luck with the next question.")
    
    question_two: bool = bool(input("True or False: The surface of the sun is hotter than the lava. "))

    if question_two is True:
        print(f"It seems the odds are on your side {player}. You have earned 2 points{winner_emoji}. Good luck on the next one.")
        sun_points += 2
    elif question_two is False:
        print(f"Looks like someone needs to brush up on their knowledge of the sun. You have earned 0 points{loser_emoji}. Good luck with the next one.")

    print("Heres a hint for the next question, the number is be  t w  e  e ...")
    input("Guess the secret number.")
    print("Haha, just kidding. The secret number is between 5 and 10.")

    question_three: int = int(input("Guess the secret number. "))
    secret_num: int = random.randint(5, 10)

    if question_three == secret_num:
        print(f"Congratulations {player}, you have guessed the secret number which has earned you 10 points{winner_emoji}.")
        sun_points += 10
    else:
        print(f"Sorry {player}. Better luck next time.{loser_emoji}")

    if sun_points > 5:
        print((f"Congratulations {player}, you have earned {sun_points} points and managed to survive the dangers of the path of sun. Welcome to Port Larco!!!{winner_emoji}"))
    else:
        print(f"Seems like you weren't cut out for the path of sun {player}{loser_emoji}. Come back soon!")
        print(f"You earned {sun_points} points.")
    return (sun_points)


def the_end() -> None:
    """A direction the player can choose that ends the game."""
    print(f"You have earned {points} points. Thank you for playing Welcome to Azaii. I hope you enjoyed your experience and can't wait to see you again!!")
    exit()


def main() -> None:
    """Main game function and entrypoint of Adventure."""
    points = 0
    path_list: list[str] = ["path of sun", "path of moon", "the end"]
    player_path_choice: str = ""

    greet()

    while player_path_choice != path_list[2]:
        print(f"Welcome {player}. You must now choose the path you will take to Port Lacro.")
        player_path_choice = str(input("What path will you choose: path of moon, path of sun, the end "))

        if player_path_choice == path_list[0]:
            points = path_of_sun(points)
        elif player_path_choice == path_list[1]:
            path_of_moon()
    the_end()


if __name__ == "__main__":
    main()