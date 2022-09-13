"""EX03 - Complete Wordle game with 6 tries."""

__author__ = "730476042"


from urllib.parse import uses_relative


def contains_char(string: str, character: str) -> bool:
    """Returns True if character is found in string."""
    assert len(character) == 1
    matching_letter = False
    secret_index = 0
    
    while matching_letter is False and secret_index < len(string):
        if character[0] == string[secret_index]:
            matching_letter = True
        else: 
            secret_index = secret_index + 1    
    if matching_letter is True:
        return True
    else:
        return matching_letter


WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def emojified(guess: str, secret:str) -> str:
    """Returns a string of emojis based on matching characters."""
    assert len(guess) == len(secret)
    i: int = 0
    boxes: str = ""
    
    while i < len(secret):
        if guess[i] == secret[i]:
            boxes = boxes + (f"{GREEN_BOX}")
        else:
            if contains_char(secret, guess[i]) == True:
                boxes = boxes + (f"{YELLOW_BOX}")
            else:
                boxes = boxes + (f"{WHITE_BOX}")
        i = i + 1
    return(boxes)


def input_guess(length: int) -> str:
    """Prompts user until their guess meets expected length."""
    
    user_guess: str = str(input(f"Enter a {length} character word: "))

    while len(user_guess) != length:
        new_guess: str = str(input(f"That wasn't {length} chars! Try again: "))
        user_guess = new_guess

    return user_guess
