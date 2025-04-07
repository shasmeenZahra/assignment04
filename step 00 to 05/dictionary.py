# Function to display the dictionary in a neat format
def display_person(person):
    print("\nCurrent person details:")
    for key, value in person.items():
        print(f"{key.capitalize()}: {value}")

# Nested dictionary with multiple layers of information
person = {
    "name": "Abrish",
    "age": 18,
    "city": "Lahore",
    "contact": {
        "email": "abrish@example.com",
        "phone": "123-456-7890"
    },
    "skills": ["Python", "JavaScript", "HTML", "CSS"],
    "education": {
        "highschool": {
            "name": "XYZ High School",
            "year": 2020
        },
        
    }
}

# Accessing values from the nested dictionary
print("Name:", person["name"])
print("Phone number:", person["contact"]["phone"])

# Updating existing values and adding new entries
person["age"] = 19
person["contact"]["email"] = "new_email@example.com"
person["hobbies"] = ["Reading", "Gaming", "Travelling"]

# Deleting keys from the dictionary
del person["city"]

# Add or update skills dynamically through user input
new_skill = input("\nEnter a new skill to add: ")
person["skills"].append(new_skill)

# Display all dictionary content neatly
display_person(person)

# More advanced operation - nested loop through nested dictionary
print("\nNested Dictionary Loop:")
for category, details in person["education"].items():
    if isinstance(details, dict):
        print(f"{category.capitalize()}:")
        for sub_key, sub_value in details.items():
            print(f"  {sub_key.capitalize()}: {sub_value}")
    else:
        print(f"{category.capitalize()}: {details}")

# Loop through list inside dictionary
print("\nSkills List:")
for skill in person["skills"]:
    print(f"- {skill}")
