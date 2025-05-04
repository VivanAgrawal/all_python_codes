import random

def dice_game():
    print("Dice Rolling Simulator")
    print("Commands: roll, quit")
    
    while True:
        match input("\nWhat would you like to do? ").lower():
            case "roll":
                dice1 = random.randint(1, 6)
                dice2 = random.randint(1, 6)
                total = dice1 + dice2
                
                print(f"You rolled: {dice1} and {dice2} (Total: {total})")
                
                match total:
                    case 7 | 11:
                        print("You win!")
                    case 2 | 3 | 12:
                        print("You lose!")
                    case _:
                        print("Roll again!")
            
            case "quit":
                print("Thanks for playing!")
                return
            
            case _:
                print("Invalid command!")
dice_game()