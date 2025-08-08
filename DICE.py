import random

def roll_dice():
    return random.randint(1, 6)  # Roll a random number from 1 to 6

def main():
    print("dice roller")
    while True:
        user_input = input("Press Enter to roll the dice or type 'exit' to quit: ").strip().lower()
        
        if user_input == 'exit':
            print("goodbye! thanks for playing.")
            break
        
        result = roll_dice()
        print(f"You rolled a {result}\n")

if __name__ == "__main__":
    main()

