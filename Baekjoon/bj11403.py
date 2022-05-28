'''
Created by sunwoong on 2022/05/28
'''
import sys

n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

for k in range(n):
    for start in range(n):
        for end in range(n):
            if board[start][k] and board[k][end]:
                board[start][end] = 1

for line in board:
    print(*line)