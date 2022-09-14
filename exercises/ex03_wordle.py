"""EX03 - Complete Wordle game with 6 tries."""

__author__ = "730476042"


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


def emojified(guess: str, secret: str) -> str:
    """Returns a string of emojis based on matching characters."""
    assert len(guess) == len(secret)
    i: int = 0
    boxes: str = ""
    
    while i < len(secret):
        if guess[i] == secret[i]:
            boxes = boxes + (f"{GREEN_BOX}")
        else:
            if contains_char(secret, guess[i]) is True:
                boxes = boxes + (f"{YELLOW_BOX}")
            else:
                boxes = boxes + (f"{WHITE_BOX}")
        i = i + 1
    return boxes


def input_guess(length: int) -> str:
    """Prompts user until their guess meets expected length."""
    user_guess: str = str(input(f"Enter a {length} character word: "))

    while len(user_guess) != length:
        new_guess: str = str(input(f"That wasn't {length} chars! Try again: "))
        user_guess = new_guess

    return user_guess


def main() -> None:
    """The entrypoint of the program and main Wordle game."""
    secret_word: str = ("codes")

    turn: int = 1
    winner: bool = False

    while turn < 7 and winner is False:

        print(f"=== Turn {turn}/6 ===")
        results = input_guess(5)
        print(emojified(results, secret_word))
        
        if results == secret_word:
            winner = True
        else:
            turn = turn + 1
    
    if winner is True:
        print(f"You won in {turn}/6 turns!")
    elif winner is False:
        print("X/6 - Sorry, try again tommorrow!")


if __name__ == "__main__":
    main()