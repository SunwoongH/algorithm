'''
Created by sunwoong on 2022/05/05
'''
import sys

n, c = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))
frequency = dict()
for i in range(len(sequence)):
    if sequence[i] not in frequency:
        frequency[sequence[i]] = [1, i]
    else:
        frequency[sequence[i]][0] += 1
result = sorted(frequency.items(), key=lambda x: (x[1][0], -x[1][1]), reverse=True)
for num in result:
    for _ in range(num[1][0]):
        print(num[0], end=' ')