import random

def get_valid_int(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"❌ Value must be at least {min_val}.")
            elif max_val is not None and val > max_val:
                print(f"❌ Value must be at most {max_val}.")
            else:
                return val
        except ValueError:
            print("❌ Invalid input. Please enter an integer.")

def generate_random_numbers(count, min_val, max_val, unique=False):
    if unique:
        if count > (max_val - min_val + 1):
            print("❌ Error: Not enough unique numbers in the given range.")
            return []
        return random.sample(range(min_val, max_val + 1), count)
    else:
        return [random.randint(min_val, max_val) for _ in range(count)]

# Main program
print("🎲 Random Number Generator – Advanced")

count = get_valid_int("How many numbers do you want to generate? ", 1)
min_val = get_valid_int("Enter the minimum value: ")
max_val = get_valid_int("Enter the maximum value: ", min_val + 1)

unique_choice = input("Do you want unique numbers? (yes/no): ").strip().lower()
unique = unique_choice == "yes"

sort_choice = input("Do you want to sort the output? (yes/no): ").strip().lower()
sort_output = sort_choice == "yes"

numbers = generate_random_numbers(count, min_val, max_val, unique)

if numbers:
    if sort_output:
        numbers.sort()
    print("\n✅ Here are your random numbers:")
    print(numbers)
    print(f"\n📊 Summary: Total = {len(numbers)}, Min = {min(numbers)}, Max = {max(numbers)}")
