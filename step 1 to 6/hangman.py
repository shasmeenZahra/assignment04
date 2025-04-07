import random

words = ["python", "laptop", "hangman", "stream", "coding"]
word = random.choice(words)
guessed = ["_"] * len(word)
attempts = 6
guessed_letters = []

print("Welcome to Hangman!")

while attempts > 0 and "_" in guessed:
    print("Word:", " ".join(guessed))
    print(f"Guesses left: {attempts}")
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for idx, letter in enumerate(word):
            if letter == guess:
                guessed[idx] = guess
    else:
        attempts -= 1
        print("Wrong guess!")

if "_" not in guessed:
    print("Congratulations! You won! 🎉")
else:
    print(f"You lost! The word was '{word}' 😞")
