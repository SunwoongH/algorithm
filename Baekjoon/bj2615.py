'''
Created by sunwoong on 2022/09/26
'''
import sys

SIZE = 19
FLOOR = 0

def check(r, c, color):
    position = (r, c)
    left_count = 0
    right_count = 0
    for i in range(c + 1, c + 6):
        if 0 <= i < SIZE and board[r][i] == color:
            left_count += 1
        else:
            break
    for i in range(c - 1, c - 6, -1):
        if 0 <= i < SIZE and board[r][i] == color:
            right_count += 1
            position = (r, i)
        else:
            break
    if left_count + right_count == 4:
        return (color, position)
    position = (r, c)
    left_count = 0
    right_count = 0
    for i in range(r + 1, r + 6):
        if 0 <= i < SIZE and board[i][c] == color:
            left_count += 1
        else:
            break
    for i in range(r - 1, r - 6, -1):
        if 0 <= i < SIZE and board[i][c] == color:
            right_count += 1
            position = (i, c)
        else:
            break
    if left_count + right_count == 4:
        return (color, position)
    position = (r, c)
    left_count = 0
    right_count = 0
    for i in range(1, 6):
        if 0 <= r - i < SIZE and 0 <= c + i < SIZE and board[r - i][c + i] == color:
            left_count += 1
        else:
            break
    for i in range(-1, -6, -1):
        if 0 <= r - i < SIZE and 0 <= c + i < SIZE and board[r - i][c + i] == color:
            right_count += 1
            position = (r - i, c + i)
        else:
            break
    if left_count + right_count == 4:
        return (color, position)
    position = (r, c)
    left_count = 0
    right_count = 0
    for i in range(1, 6):
        if 0 <= r + i < SIZE and 0 <= c + i < SIZE and board[r + i][c + i] == color:
            left_count += 1
        else:
            break
    for i in range(-1, -6, -1):
        if 0 <= r + i < SIZE and 0 <= c + i < SIZE and board[r + i][c + i] == color:
            right_count += 1
            position = (r + i, c + i)
        else:
            break
    if left_count + right_count == 4:
        return (color, position)
    return (0, position)

board = [list(map(int, sys.stdin.readline().split())) for _ in range(SIZE)]
for r in range(SIZE):
    for c in range(SIZE):
        if board[r][c] != FLOOR:
            result, position = check(r, c, board[r][c])
            if result != 0:
                print(result)
                print(position[0] + 1, position[1] + 1)
                sys.exit(0)
print(0)