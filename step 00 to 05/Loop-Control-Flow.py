# Function to display a custom number sequence using for loop
def custom_for_loop(start, end, step):
    print("\n Custom For Loop Output:")
    for i in range(start, end + 1, step):
        print(i, end=" ")
    print()

# Function to print even numbers up to a limit using while loop
def even_numbers_with_while(limit):
    print("\n Even Numbers using While Loop:")
    num = 0
    while num <= limit:
        if num % 2 == 0:
            print(num, end=" ")
        num += 1
    print()

# Function with break and else to simulate searching
def search_number(numbers, target):
    print(f"\n Searching for {target} in the list:")
    for num in numbers:
        print(f"Checking: {num}")
        if num == target:
            print("✅ Number found!")
            break
    else:
        print("❌ Number not found in the list.")

# Function with continue to skip undesired values
def skip_unwanted(numbers, skip_list):
    print("\n Skipping unwanted numbers using continue:")
    for num in numbers:
        if num in skip_list:
            continue
        print(num, end=" ")
    print()

# Nested loop example: Multiplication table
def multiplication_tables():
    print("\n Multiplication Tables (1 to 3):")
    for i in range(1, 4):
        print(f"\n📋 Table of {i}")
        for j in range(1, 11):
            print(f"{i} x {j} = {i*j}")

# Main Execution
custom_for_loop(1, 10, 1)
even_numbers_with_while(20)
search_number([5, 8, 12, 7, 3, 9], 7)
skip_unwanted([1, 2, 3, 4, 5, 6], [2, 4])
multiplication_tables()
