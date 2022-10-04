"""Choosing your own adventure game."""

__author__ = "730476042"
 
import random

winner_emoji: str = "\U0001F973"
loser_emoji: str = "\U0001F622"

def greet() -> None:
    global player
    """Greet function to introduce user to game."""
    print("Welcome to Azaii: A solo Player game where you must survive the trecherous condtions of Azaii and make your way to the safety of Port Larco.")

    player = str(input("He who dares step foot on the sacred island of Azaii, State your Name: "))

    print(f"Welcome to Azaii, {player}.")


def path_of_moon() -> None:
    """A direction the player can choose to take."""
    global points
    print("So you have decided to take the path of moon.")
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
        user_guess = str(input(f"A wild {opp} has appeared. They have flipped a coin. What is you guess {player}: Heads or Tails? "))

        while user_guess != game[0] or game[1]:
            new_guess = str(input(f"Please input guess: Heads or Tails? "))
            user_guess = new_guess


        if user_guess == opp_choice:
            points += 2.0
            print(f"Shucks, it was a lucky guess for {player}. Good job{winner_emoji}!")
        else:
            points -= 0.5
            print((f"Hahahaa, {opp_choice} will always win!!! Sucks for you {loser_emoji}."))

        i += 1

    if points > opps_size / 2:
        print((f"Congratulations {player}, you have managed to survive the dangers of the path of moon and earned {points} points. Welcome to Port Larco!!!{winner_emoji}"))
    else:
        print(f"You earned {points} points. Seems like you weren't cut out for the path of moon {player}. Come back soon{loser_emoji}!")


def path_of_sun(sun_points: int) -> int:
    """Another direction the player can choose to take.""" 
    print(f"The path of sun welcomes you {player}.")

    question_one: int = int(input("Please choose a number between 1 and 10......Choose carefully, your future is at stake."))

    if question_one >= 5:
        print(f"Very well {player}, you have earned 3 points{winner_emoji}. Good luck with the next question.")
        sun_points += 3
    elif question_one < 5:
        print(f"It seems the odds are against you {player}. You will gain no points{loser_emoji}. May you have better luck with the next question.")
    
    question_two: bool = bool(input("True or False: The surface of the sun is hotter than the lava."))

    while question_two != bool:
        new_guess = str(input(f"Please input guess: True or False? "))
        question_two = new_guess

    if question_two == True:
        print(f"It seems the odds are on your side {player}. You have earned 2 points{winner_emoji}. Good luck on the next one.")
        sun_points += 2
    elif question_two == False:
        print(f"Looks like someone needs to brush up on their knowledge of the sun. You have earned 0 points{loser_emoji}. Good luck with the next one.")


    print("Heres a hint for the next question, the number is be  t w  e  e ...")
    print(input("Guess the secret number."))
    print("Haha, just kidding. The secret number is between 5 and 10.")
    question_three: int = int(input("Guess the secret number."))
    secret_num: random.randint(5, 10)

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

def the_end() -> None:
    """A direction the player can choose that ends the game."""
    print(f"You have earned {points} points. Thank you for playing Welcome to Azaii. I hope you enjoyed your experience and can't wait to see you again!!")




def main() -> None:
    """Main game function and entrypoint of Adventure."""
    points: float = 0.0
    player: str = ""
    path_list: list[str] = ["path of sun", "path of moon", "the end"]
    player_path_choice: str = ""

    greet()

    while player_path_choice != path_list[2]:
        print(f"Welcome {player}. You must now choose the path you will take to Port Lacro.")
        player_path_choice = str(input("What path will you choose: path of moon, path of sun, the end"))

        while player_path_choice != path_list[0] or path_list[1] or path_list[2]:
            new_choice: str = str(input("Please choose your path: path of moon, path of sun, the end"))
            player_path_choice = new_choice


        if player_path_choice == path_list[0]:
            points = path_of_sun(points)
        elif player_path_choice == path_list[1]:
            path_of_moon()
    print(f"You have chosen to end the game.")
    print(f"{player} has earned {points} points.")
    print("See you next time!")
    exit()
        
    


if __name__ == "__main__":
    main()