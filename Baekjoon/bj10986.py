'''
Created by sunwoong on 2025/06/12
'''
import sys

n, m = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
remain = [0 for _ in range(m)]

remain[sequence[0] % m] += 1
for i in range(1, len(sequence)):
    sequence[i] += sequence[i - 1]
    remain[sequence[i] % m] += 1

answer = remain[0]
for i in range(len(remain)):
    answer += remain[i] * (remain[i] - 1) // 2
print(answer)