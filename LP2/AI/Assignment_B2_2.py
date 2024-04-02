
def is_safe(row, col, board, row_attacked, col_attacked, left_diag_attacked, right_diag_attacked):
    N = len(board)

    # Check row, column, diagonal attacks based on pre-computed information
    return not row_attacked[row] and not col_attacked[col] and not left_diag_attacked[row - col + N - 1] and not right_diag_attacked[row + col]

def update_attacks(row, col, row_attacked, col_attacked, left_diag_attacked, right_diag_attacked, add):
    N = len(row_attacked)

    row_attacked[row] = add
    col_attacked[col] = add
    left_diag_attacked[row - col + N - 1] = add
    right_diag_attacked[row + col] = add

def solve_n_queens(board, col, row_attacked, col_attacked, left_diag_attacked, right_diag_attacked):
    N = len(board)
    solutions = 0

    # Base case: All queens placed
    if col == N:
        # Print a solution (optional)
        for i in range(N):
            for j in range(N):
                print(int(board[i][j]), end=" ")
            print()
        print()
        return 1

    # Try placing queen in each row of this column
    for row in range(N):
        if is_safe(row, col, board, row_attacked, col_attacked, left_diag_attacked, right_diag_attacked):
            board[row][col] = True
            update_attacks(row, col, row_attacked, col_attacked, left_diag_attacked, right_diag_attacked, True)

            solutions += solve_n_queens(board, col + 1, row_attacked, col_attacked, left_diag_attacked, right_diag_attacked)

            board[row][col] = False  # Backtrack
            update_attacks(row, col, row_attacked, col_attacked, left_diag_attacked, right_diag_attacked, False)

    return solutions

if __name__ == "__main__":
    N = int(input("Enter the number of queens: "))

    # Dynamically create the boolean board
    board = [[False] * N for _ in range(N)]

    row_attacked = [False] * N
    col_attacked = [False] * N
    left_diag_attacked = [False] * (2 * N - 1)
    right_diag_attacked = [False] * (2 * N - 1)

    solutions = solve_n_queens(board, 0, row_attacked, col_attacked, left_diag_attacked, right_diag_attacked)

    if solutions == 0:
        print("Solution does not exist")
    else:
        print("Total solutions:", solutions)
