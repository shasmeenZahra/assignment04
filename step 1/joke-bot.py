import random
import time

def get_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don’t skeletons fight each other? They don’t have the guts.",
        "I told my computer I needed a break, and it said: 'No problem, I’ll go to sleep.'",
        "Why did the math book look sad? Because it had too many problems.",
        "Parallel lines have so much in common... it’s a shame they’ll never meet."
    ]
    return random.choice(jokes)

def ask_user():
    print("\nHi! I'm JokeBot 🤖. I can tell you a random joke to make you smile!")
    while True:
        user_input = input("\nWould you like to hear a joke? (yes/no/more): ").strip().lower()

        if user_input == "yes" or user_input == "more":
            print("\nFetching a hilarious joke... 🎲")
            time.sleep(1)
            joke = get_joke()
            print("\n😂 Here's your joke:")
            print(f"\"{joke}\"")
        elif user_input == "no":
            print("\nAlright! Have a great day ahead 😇")
            break
        else:
            print("\nHmm, I didn't get that. Please type 'yes', 'no', or 'more'.")

if __name__ == "__main__":
    ask_user()
