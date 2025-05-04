import random

def game():
    choices = ["rock", "paper", "scissors"]
    a = input("Choose rock, paper, or scissors: ").lower()
    opponent = random.choice(choices)
    
    match (a, opponent):
        case ("rock", "scissors") | ("paper", "rock") | ("scissors", "paper"):
            print(f"You win! opponent chose {opponent}")
        case _ if a == opponent:
            print(f"Tie! Both chose {a}")
        case _:
            print(f"You lose! opponent chose {opponent}")
            
game()x