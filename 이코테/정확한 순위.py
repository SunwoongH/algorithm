'''
Created by sunwoong on 2023/03/03
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
scores = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    scores[a - 1][b - 1] = 1
for k in range(n):
    for r in range(n):
        for c in range(n):
            if not scores[r][c] and scores[r][k] and scores[k][c]:
                scores[r][c] = 1
answer = 0
for r in range(n):
    count = 0
    for c in range(n):
        if scores[r][c] == 1:
            count += 1
        if scores[c][r] == 1:
            count += 1
    if count == n - 1:
        answer += 1
print(answer)