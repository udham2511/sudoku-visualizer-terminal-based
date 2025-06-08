import time
import sys
import copy


# constants
RESET = "\033[0m"

GREEN = "\033[32m"
RED = "\033[31m"
WHITE = "\033[97m"

# count
steps = 0


def drawBoard(board: list[list[int]]) -> None:
    global steps

    for row in range(9):
        for col in range(9):
            color = WHITE if boardCopy[row][col] else RED

            if not boardCopy[row][col] and board[row][col]:
                color = GREEN

            print(color + str(board[row][col]) + RESET, end=" ")

        print()

    print()
    print("STEP:", steps)

    sys.stdout.write("\033[F" * (len(board) + 2))
    time.sleep(0.1)


def isValid(board: list[list[int]], row: int, col: int, num: int) -> bool:
    boxRow = row - row % 3
    boxCol = col - col % 3

    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

        if board[i // 3 + boxRow][i % 3 + boxCol] == num:
            return False

    return True


def solve(board: list[list[int]], row: int, col: int) -> bool:
    global steps

    if row == 8 and col == 9:
        return True

    if col == 9:
        col = 0
        row += 1

    if board[row][col] > 0:
        return solve(board, row, col + 1)

    for num in range(1, 10):
        if isValid(board, row, col, num):
            board[row][col] = num

            drawBoard(board)
            steps += 1

            if solve(board, row, col + 1):
                return True

        board[row][col] = 0

    return False


board = [
    [0, 0, 4, 0, 5, 0, 0, 0, 0],
    [9, 0, 0, 7, 3, 4, 6, 0, 0],
    [0, 0, 3, 0, 2, 1, 0, 4, 9],
    [0, 3, 5, 0, 9, 0, 4, 8, 0],
    [0, 9, 0, 0, 0, 0, 0, 3, 0],
    [0, 7, 6, 0, 1, 0, 9, 2, 0],
    [3, 1, 0, 9, 7, 0, 2, 0, 0],
    [0, 0, 9, 1, 8, 2, 0, 0, 3],
    [0, 0, 0, 0, 6, 0, 1, 0, 0],
]

boardCopy = copy.deepcopy(board)

if solve(board, 0, 0):
    pass

time.sleep(3)
