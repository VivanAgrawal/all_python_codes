import random

def battleship():
    board_size = 5
    ship_row = random.randint(0, board_size-1)
    ship_col = random.randint(0, board_size-1)
    
    print("Let's play Battleship!")
    print("Guess a row and column between 0-4")
    
    for turn in range(4):
        print(f"\nTurn {turn + 1}")
        guess = input("Enter row and column (e.g., '2 3'): ").split()
        
        match guess:
            case [row, col] if row.isdigit() and col.isdigit():
                row, col = int(row), int(col)
                if not (0 <= row < board_size and 0 <= col < board_size):
                    print("Numbers must be between 0-4!")
                    continue
                
                if row == ship_row and col == ship_col:
                    print("Congratulations! You sunk my battleship!")
                    return
                else:
                    print("You missed my battleship!")
            case _:
                print("Please enter two numbers separated by a space!")
    
    print(f"\nGame over! The ship was at ({ship_row}, {ship_col})")
battleship()