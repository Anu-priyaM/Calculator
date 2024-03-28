import random
def guess_the_number():
    """Function to play the Guess the Number game"""
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100. Can you guess what it is?")
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    while True:
        try:
            guess = int(input("Enter your guess (between 1 and 100): "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        attempts += 1
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts.")
            break
# Run the game
guess_the_number()
