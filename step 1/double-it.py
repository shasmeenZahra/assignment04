def double_it(number):
    return number * 2

# Store user entries for reference
history = []

print("🔁 Welcome to the Double-It Program!")
print("Type 'exit' to quit anytime.\n")

while True:
    user_input = input("Enter a number to double: ").strip().lower()
    
    if user_input == "exit":
        print("\n👋 Exiting program. Here's your session summary:")
        for i, (original, doubled) in enumerate(history, start=1):
            print(f"{i}. {original} → {doubled}")
        break

    try:
        number = float(user_input)
        result = double_it(number)
        history.append((number, result))

        # Provide feedback on the number
        if number > 0:
            nature = "positive"
        elif number < 0:
            nature = "negative"
        else:
            nature = "zero"

        print(f"✅ Your number is {nature}. Double of {number} is {result}\n")

    except ValueError:
        print("❌ Invalid input! Please enter a valid number.\n")
