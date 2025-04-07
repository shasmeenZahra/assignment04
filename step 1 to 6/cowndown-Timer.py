import time

try:
    seconds = int(input("Enter countdown time in seconds: "))
    while seconds > 0:
        print(f"Time left: {seconds} seconds")
        time.sleep(1)
        seconds -= 1
    print("Time's up! ⏰")
except ValueError:
    print("Please enter a valid number.")
