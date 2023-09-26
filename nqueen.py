def is_safe(board, row, col, N):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == "Q":
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens(N):
    board = [["." for _ in range(N)] for _ in range(N)]

    def backtrack(row):
        if row == N:
            solutions.append(["".join(row) for row in board])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = "Q"
                backtrack(row + 1)
                board[row][col] = "."

    solutions = []
    backtrack(0)
    return solutions

def display_solution(solution):
    for row in solution:
        print("[" + "][".join(row) + "]")
    print()

if __name__ == "__main__":
    N = int(input("Enter the board size (N): "))
    solutions = solve_n_queens(N)
    
    if solutions:
        print(f"Found {len(solutions)} solution(s) for {N}-Queens:")
        for solution in solutions:
            display_solution(solution)
    else:
        print(f"No solutions found for {N}-Queens.")
