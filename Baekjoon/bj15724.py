'''
Created by sunwoong on 2022/07/29
'''
import sys

n, m = map(int, sys.stdin.readline().split())
people = [[0 for _ in range(m + 1)]]
for _ in range(n):
    people.append([0] + list(map(int, sys.stdin.readline().split())))

for r in range(2, n + 1):
    for c in range(1, m + 1):
        people[r][c] += people[r - 1][c]
for c in range(2, m + 1):
    for r in range(1, n + 1):
        people[r][c] += people[r][c - 1]

k = int(sys.stdin.readline())
for _ in range(k):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    print(people[x2][y2] - people[x1 - 1][y2] - people[x2][y1 - 1] + people[x1 - 1][y1 - 1])