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
    
            