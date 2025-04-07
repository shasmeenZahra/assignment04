print("Welcome to Mad Libs! Please provide the following words:")

name = input("Enter a name: ")
place = input("Enter a place: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
animal = input("Enter an animal: ")

story = f"""
Once upon a time, {name} went to {place} to {verb}.
It was a very {adjective} day, and suddenly a {animal} appeared out of nowhere!
{name} couldn't believe it and ran away screaming!
"""

print("\nHere’s your Mad Libs story:")
print(story)
