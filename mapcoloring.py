def print_board(board):
    """Print the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the current player has won."""
    # Check rows
    for row in board:
        if all([cell == player for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    # Check diagonals
    if all([board[i][i] == player for i in range(3)]) or \
       all([board[i][2 - i] == player for i in range(3)]):
        return True

    return False

def is_full(board):
    """Check if the board is full (i.e., no empty spaces)."""
    return all([cell != ' ' for row in board for cell in row])

def main():
    """Main function to run the Tic-Tac-Toe game."""
    board = [[' ' for _ in range(3)] for _ in range(3)]
    players = ['X', 'O']
    turn = 0

    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        player = players[turn % 2]
        print(f"Player {player}'s turn.")
        
        # Get move from the player
        while True:
            try:
                row, col = map(int, input("Enter row and column (0, 1, 2) separated by space: ").split())
                if board[row][col] == ' ':
                    board[row][col] = player
                    break
                else:
                    print("Cell already occupied. Try again.")
            except (ValueError, IndexError):
                print("Invalid input. Enter row and column as two numbers between 0 and 2.")

        print_board(board)

        if check_winner(board, player):
            print(f"Player {player} wins!")
            break

        if is_full(board):
            print("It's a draw!")
            break

        turn += 1

if _name_ == "_main_":
    main()