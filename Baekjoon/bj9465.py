'''
Created by sunwoong on 2022/10/11
'''
import sys

test = int(sys.stdin.readline())
for _ in range(test):
    n = int(sys.stdin.readline())
    sequence = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    if n > 1:
        sequence[0][1] += sequence[1][0]
        sequence[1][1] += sequence[0][0]
        for i in range(2, n):
            sequence[0][i] += max(sequence[1][i - 2], sequence[1][i - 1])
            sequence[1][i] += max(sequence[0][i - 2], sequence[0][i - 1])
    print(max(sequence[0][n - 1], sequence[1][n - 1]))