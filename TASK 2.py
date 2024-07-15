import random

def guess_the_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("I'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?")

    while True:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low!")
        elif user_guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")
            break

# Run the game
guess_the_number()