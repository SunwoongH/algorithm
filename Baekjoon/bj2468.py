'''
Created by sunwoong on 2022/06/04
'''
import sys
from copy import deepcopy
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
board = []
for _ in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))
    
move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
def dfs(r: int, c: int) -> None:
    if r < 0 or r >= n or c < 0 or c >= n or temp[r][c] == 0:
        return
    temp[r][c] = 0
    for oper in move:
        dfs(r + oper[0], c + oper[1])

result = 0
for k in range(1, max(map(max, board)) + 1):
    temp = deepcopy(board)
    count = 0
    for r in range(n):
        for c in range(n):
            if temp[r][c] < k:
                temp[r][c] = 0
    for r in range(n):
        for c in range(n):
            if temp[r][c] > 0:
                count += 1
                dfs(r, c)
    result = max(result, count)
print(result)