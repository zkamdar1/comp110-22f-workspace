"""EX02 - Making a one-shot wordle game."""

__author__ = "730476042"

secret_word: str = ("python")

user_guess: str = str(input(f"What is your {len(secret_word)}-letter guess? "))

while len(user_guess) != len(secret_word):
    new_guess: str = str(input(f"That was not {len(secret_word)} letters! Try again: "))
    user_guess = new_guess

#Above-asking user for guess

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
guess_result = ""

while i < len(secret_word):
    if user_guess[i] == secret_word[i]:
        guess_result = guess_result + (f"{GREEN_BOX}")
    else:
        guess_result = guess_result + (f"{WHITE_BOX}")
    i = i + 1

print(guess_result)

#Above- Indexing input and finding matching characters with secret word, outputing corresponding colored box. 

#matching_letter = False
#alter_indices = 0

#while matching_letter == False and alter_indices < len[secret_word]:
 #   if alter_indices == user_guess:
 #      matching_letter = True



if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!" )
