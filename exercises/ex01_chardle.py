"""EX01 - Chardle - A step towards Wordle."""

__author__ = "730476042"


chosen_word: str = str(input("Enter a 5-character word: "))

if len(chosen_word) > 5:
    print("Error: Word must contain 5 characters")
    exit()
else:
    if len(chosen_word) < 5:
        print("Error: Word must contain 5 characters")
        exit()


letter_choice: str = str(input("Enter a single character: "))

if len(letter_choice) > 1:
    print("Error: Character must be a single character.")
    exit()
else:
    if len(letter_choice) < 1:
        print("Error: Character must be a single character.")
        exit()


print("Searching for " + letter_choice + " in " + chosen_word)

count = 0

if letter_choice == chosen_word[0]:
    print(letter_choice + " found at index 0")
    count = count + 1

if letter_choice == chosen_word[1]:
    print(letter_choice + " found at index 1")
    count = count + 1

if letter_choice == chosen_word[2]:
    print(letter_choice + " found at index 2")
    count = count + 1

if letter_choice == chosen_word[3]:
    print(letter_choice + " found at index 3")
    count = count + 1
            
if letter_choice == chosen_word[4]:
    print(letter_choice + " found at index 4")
    count = count + 1


if count == 0:
    print("No instances of " + letter_choice + " found in " + chosen_word)
else:
    if count == 1:
        print("1 instance of " + letter_choice + " found in " + chosen_word)
    else:
        if count == 2:
            print("2 instances of " + letter_choice + " found in " + chosen_word)
        else:
            if count > 2:
                print(str(count) + " instances of " + letter_choice + " found in " + chosen_word)