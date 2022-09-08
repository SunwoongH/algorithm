'''
Created by sunwoong on 2022/09/08
'''
import sys

triangle = [[0 for _ in range(i + 1)] for i in range(29)]

n, m, w = map(int, sys.stdin.readline().split())

for i in range(29):
    triangle[i][0] = 1
    triangle[i][i] = 1

for r in range(2, 29):
    for c in range(1, r):
        triangle[r][c] = triangle[r - 1][c - 1] + triangle[r - 1][c]

result = 0
count = 1
for r in range(n, n + w):
    result += sum(triangle[r - 1][m - 1:m - 1 + count])
    count += 1
print(result)