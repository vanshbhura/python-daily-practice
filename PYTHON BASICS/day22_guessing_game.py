# Day 22: Number Guessing Game
# Topics:
# while loop, conditions, user input

secret_number = 7
guess = None

print("Guess the number between 1 and 10")

while guess != secret_number:
    guess = int(input("Enter your guess: "))

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed the number.")
