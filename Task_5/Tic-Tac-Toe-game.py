def print_board(board):
    print("\n")
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
    print("\n")


def check_winner(board, player):
    win_conditions = [
        [0,1,2],[3,4,5],[6,7,8],  
        [0,3,6],[1,4,7],[2,5,8],  
        [0,4,8],[2,4,6]          
    ]
    for condition in win_conditions:
        if all(board[i] == player for i in condition):
            return True
    return False


def choose_symbols():
    while True:
        player1 = input("Player 1, enter your symbol: ")

        if len(player1) != 1:
            print("Invalid! Enter only ONE character.")
            continue

        player2 = input("Player 2, enter your symbol: ")

        if len(player2) != 1:
            print("Invalid! Enter only ONE character.")
            continue

        if player1 == player2:
            print("Symbols must be different!")
            continue

        return player1, player2


def tic_tac_toe():
    board = [" "] * 9
    
    player1, player2 = choose_symbols()
    
    current_player = player1
    
    for turn in range(9):
        print_board(board)
        
        try:
            move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1
        except:
            print("Invalid input! Try again.")
            continue
        
        if move < 0 or move > 8 or board[move] != " ":
            print("Invalid move! Try again.")
            continue
        
        board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            return
        
        current_player = player2 if current_player == player1 else player1
    
    print_board(board)
    print("It's a draw!")


tic_tac_toe()