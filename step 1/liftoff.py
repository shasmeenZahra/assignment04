import time
import random

def simulate_beep():
    print("🔊 Beep...", end="", flush=True)
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="", flush=True)
    print()

def get_countdown_start():
    while True:
        try:
            user_input = input("⏳ Enter countdown start (e.g., 10): ")
            count = int(user_input)
            if count <= 0:
                raise ValueError
            return count
        except ValueError:
            print("❌ Please enter a valid positive number.\n")

def launch_countdown(start):
    print("\n🚀 Countdown begins!\n")
    messages = [
        "Check fuel systems...",
        "All engines running...",
        "Final system check...",
        "Ignition sequence start...",
        "T-minus liftoff...",
        "Brace yourself!"
    ]
    
    for i in range(start, 0, -1):
        msg = random.choice(messages) if i <= 5 else ""
        print(f"🔢 T-{i} {msg}")
        simulate_beep()
        time.sleep(1)
    
    print("\n🔥 Ignition!")
    time.sleep(0.5)
    print("🚀 Liftoff! We have a liftoff!\n")
    time.sleep(1)
    print("🌍 Leaving Earth's atmosphere...")

# Run the countdown
count_start = get_countdown_start()
launch_countdown(count_start)
