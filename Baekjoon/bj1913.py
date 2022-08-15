'''
Created by sunwoong on 2022/08/15
'''
import sys

def board_implementation(n, start_r, start_c):
    global num
    if n == 1:
        board[start_r][start_c] = num
        return
    elif n == 0:
        return
    for r in range(start_r, start_r + n):
        board[r][start_c] = num
        num -= 1
    for c in range(start_c + 1, start_c + n):
        board[start_r + n - 1][c] = num
        num -= 1
    for r in range(start_r + n - 2, start_r - 1, -1):
        board[r][start_c + n - 1] = num
        num -= 1
    for c in range(start_c + n - 2, start_c, -1):
        board[start_r][c] = num
        num -= 1
    board_implementation(n - 2, start_r + 1, start_c + 1)

n = int(sys.stdin.readline())
target = int(sys.stdin.readline())
num = n * n
board = [[0 for _ in range(n)] for _ in range(n)]
board_implementation(n, 0, 0)
for line in board:
    print(*line)
for r in range(n):
    for c in range(n):
        if board[r][c] == target:
            print(r + 1, c + 1)
            break