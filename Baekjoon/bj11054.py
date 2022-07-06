'''
Created by sunwoong on 2022/07/06
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
upper = [0 for _ in range(n)]
lower = [0 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            upper[i] = max(upper[i], upper[j])
    upper[i] += 1
for i in range(n - 1, -1, -1):
    for j in range(n - 1, i, -1):
        if sequence[j] < sequence[i]:
            lower[i] = max(lower[i], lower[j])
    lower[i] += 1
    
distance = 0
for i in range(n):
    distance = max(distance, upper[i] + lower[i])
print(distance - 1)