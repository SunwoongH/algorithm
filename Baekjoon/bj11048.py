'''
Created by sunwoong on 2022/12/29
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
maze = [[0 for _ in range(m + 1)]]
for _ in range(n):
    maze.append([0] + list(map(int, input().split())))
for r in range(1, n + 1):
    for c in range(1, m + 1):
        maze[r][c] += max(maze[r - 1][c], maze[r][c - 1])
print(maze[n][m])