'''
Created by sunwoong on 2022/07/22
'''
def draw_star(n: int, start_r: int, end_r: int, start_c: int, end_c: int) -> None:
    if n == 1:
        board[start_r][end_c] = '*'
        return
    draw_star(n - 1, start_r + 2, end_r - 2, start_c + 2, end_c - 2)
    for r in range(start_r, end_r + 1):
        board[r][start_c] = board[r][end_c] = '*'
    for c in range(start_c + 1, end_c):
        board[start_r][c] = board[end_r][c] = '*'

n = int(input())
board = [[' ' for _ in range(5 + (n - 2) * 4)] for _ in range(5 + (n - 2) * 4)]
draw_star(n, 0, 4 + (n - 2) * 4, 0, 4 + (n - 2) * 4)
for line in board:
    print(''.join(line))