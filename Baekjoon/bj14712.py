'''
Created by sunwoong on 2022/08/14
'''
import sys

n, m = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(m)] for _ in range(n)]
result = 0

def dfs(position: int) -> None:
    if position == n * m:
        return
    dfs(position + 1)
    r = position // m
    c = position % m
    global result
    if position > m:
        if ((r - 1 >= 0 and c - 1 >= 0) and not(board[r - 1][c] and board[r - 1][c - 1] and board[r][c - 1]))\
            or c == 0:
            result += 1
            board[r][c] = 1
            dfs(position + 1)
            board[r][c] = 0
    else:
        result += 1
        board[r][c] = 1
        dfs(position + 1)
        board[r][c] = 0
dfs(0)
print(result + 1)