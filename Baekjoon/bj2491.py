'''
Created by sunwoong on 2022/10/06
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]

for i in range(1, n):
    if sequence[i - 1] <= sequence[i]:
        increase[i] = increase[i - 1] + 1
    if sequence[i - 1] >= sequence[i]:
        decrease[i] = decrease[i - 1] + 1
print(max(max(increase), max(decrease)))
        