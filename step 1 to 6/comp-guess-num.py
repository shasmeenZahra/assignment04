print("Think of a number between 1 and 100, and I'll try to guess it!")

low = 1
high = 100
feedback = ""

while feedback != "correct":
    guess = (low + high) // 2
    print(f"My guess is {guess}")
    feedback = input("Is it too high, too low, or correct? ").lower()

    if feedback == "too high":
        high = guess - 1
    elif feedback == "too low":
        low = guess + 1

print("Yay! I guessed your number 🎉")
