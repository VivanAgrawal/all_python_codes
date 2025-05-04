import random

def hangman():
    words = ["python", "programming", "hangman", "developer", "keyboard"]
    secret = random.choice(words)
    guessed = set()
    attempts = 6
    
    while attempts > 0:
        display = "".join([letter if letter in guessed else "_" for letter in secret])
        print(f"\nWord: {display}")
        print(f"Attempts left: {attempts}")
        print(f"Guessed letters: {' '.join(guessed)}")
        
        guess = input("Guess a letter: ").lower()
        
        match guess:
            case _ if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter!")
                continue
            case _ if guess in guessed:
                print("You already guessed that letter!")
                continue
            case _:
                guessed.add(guess)
                if guess not in secret:
                    attempts -= 1
                    print("Wrong guess!")
        
        if all(letter in guessed for letter in secret):
            print(f"\nCongratulations! You guessed the word: {secret}")
            return
    
    print(f"\nGame over! The word was: {secret}")
hangman()