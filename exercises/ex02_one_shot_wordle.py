"""EX02 - Making a one-shot wordle game."""

__author__ = "730476042"

secret_word: str = ("python")

user_guess: str = str(input("What is your 6-letter guess? "))

while len(user_guess) != 6:
    new_guess: str = str(input("That was not 6 letters! Try again: "))
    user_guess = new_guess

if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!" )
