'''
Created by sunwoong on 2022/11/20
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
stack = [n - 1]
for i in range(n - 2, -1, -1):
    while stack and sequence[stack[-1]] <= sequence[i]:
        j = stack.pop()
        sequence[j] = i + 1
    stack.append(i)
while stack:
    j = stack.pop()
    sequence[j] = 0
print(*sequence)