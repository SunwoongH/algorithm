'''
Created by sunwoong on 2022/09/09
'''
import sys

n = int(sys.stdin.readline())
sequence = []
for _ in range(n):
    num = float(sys.stdin.readline())
    sequence.append(num)

result = sequence[0]
for i in range(1, n):
    sequence[i] = max(sequence[i], sequence[i - 1] * sequence[i])
    result = max(result, sequence[i])
print("%.3f" %result)