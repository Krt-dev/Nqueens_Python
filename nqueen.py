def is_safe(board, row, col, n):
    # Check the column on top of the current cell
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper-left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper-right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if solve_n_queens_util(board, 0, n):
        return board

    return None

def solve_n_queens_util(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            if solve_n_queens_util(board, row + 1, n):
                return True
            board[row][col] = 0

    return False

def display_board(board):
    if board is None:
        print("No solution exists.")
    else:
        for row in board:
            print(' '.join(['[Q]' if cell == 1 else '[.]' for cell in row]))

if __name__ == "__main__":
    n = int(input("Enter the board size (wN): "))
    solution = solve_n_queens(n)
    display_board(solution)
