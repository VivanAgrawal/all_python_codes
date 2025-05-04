import random

def word_jumble():
    words = ["python", "jumble", "easy", "difficult", "answer", "xylophone"]
    word = random.choice(words)
    jumbled = "".join(random.sample(word, len(word)))
    
    print(f"The jumbled word is: {jumbled}")
    
    for attempt in range(3, 0, -1):
        guess = input(f"Guess the word ({attempt} attempts left): ").lower()
        
        match guess:
            case correct if correct == word:
                print("Congratulations! You guessed it!")
                return
            case _:
                print("Wrong guess!")
    
    print(f"\nGame over! The word was: {word}")
    
word_jumble()