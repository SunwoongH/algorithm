'''
Created by sunwoong 2022/08/01
'''
import sys

def divide(n: int, r: int, c: int) -> None:
    if n == 1:
        count[board[r][c]] += 1
        return
    target = board[r][c]
    check = True
    for i in range(r, r + n):
        for j in range(c, c + n):
            if target != board[i][j]:
                check = False
                break
        if not check:
            break
    if not check:
        for i in range(3):
            for j in range(3):
                divide(n // 3, r + i * (n // 3), c + j * (n // 3))
    else:
        count[target] += 1

count = [0, 0, 0]
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
divide(n, 0, 0)
print(count[-1], count[0], count[1], sep='\n')