def tic_tac_toe():
    board = [" "] * 9
    current_player = "X"
    
    while True:
        print_board(board)
        pos = input(f"Player {current_player}, enter position (1-9): ")
        
        match pos:
            case _ if not pos.isdigit() or int(pos) not in range(1, 10):
                print("Invalid position!")
                continue
            case _:
                pos = int(pos) - 1
                if board[pos] != " ":
                    print("Position already taken!")
                    continue
                
                board[pos] = current_player
                
                # Check win conditions
                win_conditions = [
                    [0,1,2], [3,4,5], [6,7,8],  # rows
                    [0,3,6], [1,4,7], [2,5,8],  # columns
                    [0,4,8], [2,4,6]            # diagonals
                ]
                
                for condition in win_conditions:
                    if all(board[i] == current_player for i in condition):
                        print_board(board)
                        print(f"Player {current_player} wins!")
                        return
                
                if " " not in board:
                    print_board(board)
                    print("It's a tie!")
                    return
                
                current_player = "O" if current_player == "X" else "X"