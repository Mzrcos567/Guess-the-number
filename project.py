import random

def guess_the_number():
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 to 50.")
    
    secret_number = random.randint(1, 50)
    attempts = 0
    max_attempts = 5
    
    while attempts < max_attempts:
        try:
            guess =  int(input(f"Attempt {attempts + 1}/{max_attempts}: "))
        except ValueError:
            print("That's not a number. Try again.")
            continue
    
        attempts += 1
    
        if guess < secret_number:
            print("Too low.")
        elif guess > secret_number:
            print("Too high.")
        else:
            print(f"Correct! You guessed the number in {attempts} attempts")
            break
    else:
        print(f"Out of attempts! The number was {secret_number}.")
        
#Run the game
guess_the_number()