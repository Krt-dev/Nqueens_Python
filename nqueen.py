def to_determine_safe_cell(board, row, col, n):
 
    for i in range(row):
        if board[i][col] == 1:
            return False


    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def to_Solve(n):
    board = [[0 for _ in range(n)] for _ in range(n)]

    if to_Solve_util(board, 0, n):
        return board

    return None

def to_Solve_util(board, row, n):
    if row == n:
        return True

    for col in range(n):
        if to_determine_safe_cell(board, row, col, n):
            board[row][col] = 1
            if to_Solve_util(board, row + 1, n):
                return True
            board[row][col] = 0

    return False

def generate_Board(board):
    if board is None:
        print("No solution")
    else:
        for row in board:
            print(' '.join(['[Q]' if cell == 1 else '[.]' for cell in row]))

if __name__ == "__main__":
    n = int(input("Board size: "))
    answer = to_Solve(n)
    generate_Board(answer)
