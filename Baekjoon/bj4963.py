'''
Created by sunwoong 2022/05/09
'''
import sys
sys.setrecursionlimit(10 ** 6)

dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
def dfs(r, c) -> None:
    if r < 0 or r >= h or c < 0 or c >= w or map_table[r][c] != 1:
        return
    map_table[r][c] = 0
    for i in range(8):
        dfs(r + dr[i], c + dc[i])

while True:
    w, h = map(int, sys.stdin.readline().split())
    if not w and not h:
        break
    map_table = []
    for _ in range(h):
        map_table.append(list(map(int, sys.stdin.readline().split())))
    count = 0
    for r in range(h):
        for c in range(w):
            if map_table[r][c] == 1:
                dfs(r, c)
                count += 1
    print(count)