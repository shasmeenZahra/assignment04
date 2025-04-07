# Function to check if a number is Positive, Negative, or Zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

# Function to compare two numbers
def compare_two_numbers(a, b):
    if a > b:
        return "a is greater"
    elif a < b:
        return "b is greater"
    else:
        return "Both are equal"

# Function to compare multiple numbers
def compare_multiple_numbers(*args):
    max_num = max(args)
    min_num = min(args)
    avg_num = sum(args) / len(args)
    return f"Max: {max_num}, Min: {min_num}, Average: {avg_num:.2f}"

# Taking multiple inputs
numbers = input("Enter multiple numbers separated by space: ").split()
numbers = [int(num) for num in numbers]  # Convert to integers

# Check for each number whether it's Positive, Negative, or Zero
print("\nNumber Analysis:")
for num in numbers:
    result = check_number(num)
    print(f"The number {num} is {result}")

# Comparing two fixed numbers
a = 10
b = 20
print("\nComparison of a and b:")
print(compare_two_numbers(a, b))

# Comparing multiple numbers
print("\nComparison of multiple numbers:")
print(compare_multiple_numbers(*numbers))
