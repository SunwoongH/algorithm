'''
Created by sunwoong on 2022/03/28
'''
import sys

n = int(sys.stdin.readline())

def solve(start: int) -> bool:
    if len(missing) == start:
        for line in board:
            print(''.join(map(str, line)))
        return True
    is_solve = False
    r, c = missing[start]
    for num in range(1, 10):
        if not row[r][num] and not column[c][num] and not square[(r // 3) * 3 + (c // 3)][num] and not is_solve:
            row[r][num] = column[c][num] = square[(r // 3) * 3 + (c // 3)][num] = True
            board[r][c] = num
            is_solve = solve(start + 1)
            row[r][num] = column[c][num] = square[(r // 3) * 3 + (c // 3)][num] = False
            board[r][c] = 0
    return is_solve

for _ in range(n):
    board = [list(map(int, list(sys.stdin.readline().rstrip('\n')))) for _ in range(9)]
    board_check, missing = True, []
    row = [[False for _ in range(10)] for _ in range(9)]
    column = [[False for _ in range(10)] for _ in range(9)]
    square = [[False for _ in range(10)] for _ in range(9)]
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                missing.append((i, j))
            else:
                if row[i][board[i][j]] or column[j][board[i][j]] or square[(i // 3) * 3 + (j // 3)][board[i][j]]:
                    board_check = False
                    break
                else:
                    row[i][board[i][j]] = column[j][board[i][j]] = square[(i // 3) * 3 + (j // 3)][board[i][j]] = True
    if not board_check:
        print("Could not complete this grid.")
        print()
        continue
    if not solve(0):
        print("Could not complete this grid.")
    print()