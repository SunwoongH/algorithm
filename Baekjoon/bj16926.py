'''
Created by sunwoong on 2022/08/02
'''
import sys

n, m, count = map(int, sys.stdin.readline().split())
curr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
for k in range(count):
    for margin in range(0, min(n, m) // 2):
        temp = curr[margin][margin]
        for c in range(margin, m - margin - 1):
            curr[margin][c] = curr[margin][c + 1]
        for r in range(margin, n - margin - 1):
            curr[r][m - margin - 1] = curr[r + 1][m - margin - 1]
        for c in range(m - margin - 1, margin, -1):
            curr[n - margin - 1][c] = curr[n - margin - 1][c - 1]
        for r in range(n - margin - 1, margin + 1, -1):
            curr[r][margin] = curr[r - 1][margin]
        curr[margin + 1][margin] = temp
for line in curr:
    print(*line)