import random

secret_number = random.randint(1, 10)
guess = None

print("🎲 Guess the number I'm thinking of (between 1 and 10):")

while guess != secret_number:
    try:
        guess = int(input("Your guess: "))
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("🎉 Correct! You guessed it.")
    except ValueError:
        print("Please enter a valid number.")
