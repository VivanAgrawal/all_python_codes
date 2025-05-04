import random

def guess_number():
    target = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = input("Guess a number between 1-100: ")
        match guess:
            case _ if not guess.isdigit():
                print("Please enter a number!")
            case _:
                guess = int(guess)
                attempts += 1
                match guess:
                    case _ if guess < target:
                        print("Too low!")
                    case _ if guess > target:
                        print("Too high!")
                    case _:
                        print(f"Correct! You guessed it in {attempts} attempts!")
                        break
guess_number()