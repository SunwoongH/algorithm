'''
Created by sunwoong on 2022/05/18
'''
import sys
sys.setrecursionlimit(10 ** 6)

n, m, k = map(int, sys.stdin.readline().split())
table = [[0 for _ in range(m)] for _ in range(n)]
for _ in range(k):
    u, v = map(int, sys.stdin.readline().split())
    table[u - 1][v - 1] = 1
    
move = [(0, 1), (-1, 0), (1, 0), (0, -1)]
def dfs(r, c) -> None:
    if r < 0 or r >= n or c < 0 or c >= m or table[r][c] == 0:
        return
    global count
    count += 1
    table[r][c] = 0
    for operation in move:
        dfs(r + operation[0], c + operation[1])

result = 0
for r in range(n):
    for c in range(m):
        if table[r][c] == 1:
            count = 0
            dfs(r, c)
            result = max(result, count)
print(result)