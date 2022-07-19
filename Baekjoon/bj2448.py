'''
Created by sunwoong on 2022/07/19
'''
import sys

n = int(sys.stdin.readline())
board = [[' ' for _ in range(n * 2 - 1)] for _ in range(n)]

def draw_star(n: int, height: int, start: int, end: int) -> None:
    if n == 3:
        board[height][(start + end) // 2] = board[height + 1][start + 1] = board[height + 1][end - 1] = '*'
        for i in range(start, end + 1):
            board[height + 2][i] = '*'
        return
    draw_star(n // 2, height, start + n // 2, end - n // 2)
    draw_star(n // 2, height + n // 2, start, start + n - 2)
    draw_star(n // 2, height + n // 2, start + n, end)

draw_star(n, 0, 0, n * 2 - 2)
for i in range(len(board)):
    for j in range(len(board[0])):
        print(board[i][j], end='')
    print()