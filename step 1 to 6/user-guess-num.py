import random

number = random.randint(1, 100)
guess = None

print("Guess the number I'm thinking of (between 1 and 100)")

while guess != number:
    try:
        guess = int(input("Your guess: "))
        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! 🎉")
    except ValueError:
        print("Please enter a valid number.")
