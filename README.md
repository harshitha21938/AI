8 queens:
ALOGRITHM:
Initialize the Board:
Create an 8x8 chessboard initialized to 0, where 0 represents an empty cell.
Define Safe Function:
Create a function is_safe(board, row, col) that checks if it's safe to place a queen at position (row, col) by ensuring:
No queen exists in the same row to the left.
No queen exists in the upper diagonal to the left.
No queen exists in the lower diagonal to the left.
Recursive Backtracking:
Create a recursive function solve_n_queens(board, col) that solves the problem for one column at a time:
Base Case: If all queens are placed (col == 8), return True (problem solved).
Iterate over Rows: For the current column col, try placing a queen in each row row one by one:
Check if placing the queen in (row, col) is safe using the is_safe function.
If placing the queen is safe:
Place the queen by marking board[row][col] = 1.
Recursively attempt to place queens in the next column by calling solve_n_queens(board, col + 1).
If the recursive call returns True, the current placement is correct; propagate True.
If the recursive call returns False, backtrack by removing the queen from (row, col) (mark board[row][col] = 0).
If no valid row is found for the current column, return False to backtrack.
Initial Call:
Start by calling solve_n_queens(board, 0) for the first column and proceed recursively.
Solution Found:
If the function returns True, print or store the chessboard solution.
If no solution is possible, return a failure message.

