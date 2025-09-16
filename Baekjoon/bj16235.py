'''
Created by sunwoong on 2025/09/16
'''
import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().split())
a = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
trees = []
for _ in range(m):
    r, c, age = map(int, sys.stdin.readline().split())
    trees.append((r, c, age))
food = [[5 for _ in range(n)] for _ in range(n)]

trees = deque(sorted(trees, key=lambda x: x[2]))

def spring_and_summer():
    global trees
    new_trees = deque()
    dead = []
    
    while trees:
        r, c, age = trees.popleft()
        if food[r - 1][c - 1] >= age:
            food[r - 1][c - 1] -= age
            new_trees.append((r, c, age + 1))
        else:
            dead.append((r, c, age))

    while dead:
        r, c, age = dead.pop()
        food[r - 1][c - 1] += age // 2

    trees = new_trees

move = [(1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (1, -1), (-1, 1), (-1, -1)]

def fall():
    extra = deque()
    for tree in trees:
        r, c, age = tree
        if age % 5 == 0:
            for oper in move:
                dr = r + oper[0]
                dc = c + oper[1]
                if 1 <= dr <= n and 1 <= dc <= n:
                    extra.append((dr, dc, 1))
    trees.extendleft(extra)

def winter():
    for r in range(n):
        for c in range(n):
            food[r][c] += a[r][c]

for _ in range(k):
    spring_and_summer()
    fall()
    winter()

print(len(trees))