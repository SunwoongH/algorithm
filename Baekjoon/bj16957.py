'''
Created by sunwoong 2025/09/05
'''
import sys

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    parent[b] = a
    count[a] += count[b]
    count[b] = 0

r, c = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(r)]
parent = [i for i in range(r * c + 1)]
count = [1 for _ in range(r * c + 1)]
move = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

for i in range(r):
    for j in range(c):
        lowest = None
        for oper in move:
            dr = i + oper[0]
            dc = j + oper[1]
            if 0 <= dr < r and 0 <= dc < c:
                if lowest is None:
                    lowest = [board[dr][dc], dr * c + dc + 1]
                    continue
                if lowest[0] > board[dr][dc]:
                    lowest = [board[dr][dc], dr * c + dc + 1]
        if lowest[0] < board[i][j]:
            union(lowest[1], i * c + j + 1)

board = [[0 for _ in range(c)] for _ in range(r)]
for i in range(r):
    for j in range(c):
        board[i][j] = count[i * c + j + 1]
for line in board:
    print(*line)