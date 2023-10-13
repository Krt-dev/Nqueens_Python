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
            return True
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row][col] = "Q"
                if backtrack(row + 1):
                    return True
                board[row][col] = "."

    if backtrack(0):
        return ["[".join(row) + "]" for row in board]
    else:
        return None

def display_solution(solution):
    if solution:
        for row in solution:
            print(row)
        print()
    else:
        print("No solution found.")

if __name__ == "__main__":
    N = int(input("Enter the board size (N): "))
    solution = solve_n_queens(N)
    
    print(f"Solution for {N}-Queens:")
    display_solution(solution)
