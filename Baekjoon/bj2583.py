'''
Created by sunwoong on 2022/06/03
'''
import sys
sys.setrecursionlimit(10 ** 6)

m, n, k = map(int, sys.stdin.readline().split())
board = [[0 for _ in range(n)] for _ in range(m)]
for _ in range(k):
    left_x, left_y, right_x, right_y = map(int, sys.stdin.readline().split())
    for r in range(left_y, right_y):
        for c in range(left_x, right_x):
            if board[r][c] != 1:
                board[r][c] = 1

label = 0
result = []
move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
def dfs(r: int, c: int) -> None:
    if r < 0 or r >= m or c < 0 or c >= n or board[r][c] == 1:
        return
    global count
    board[r][c] = 1
    count += 1
    for oper in move:
        dfs(r + oper[0], c + oper[1])
        
for r in range(m):
    for c in range(n):
        if board[r][c] == 0:
            label += 1
            count = 0
            dfs(r, c)
            result.append(count)

print(label)
print(*sorted(result))