"""An example of conditonal (if-else) statements."""

SECRET: int = 3

print("I'm thinking of a number between 1-5, what is it?")
guess: int = int(input("What is your guess? "))

if guess == SECRET:
    print("You guessed correctly!!!")
    print("Have a wondeful day!!!")
else:
    print("Sorry, you guessed incorrectly :( ")
    if guess > SECRET:
        print("You guessed to high!")
    else:
        print("You guessed to low!")        

print("Game Over.")
