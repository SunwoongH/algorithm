'''
Created by sunwoong on 2022/07/27
'''
import sys

n = int(sys.stdin.readline())
honey = list(map(int, sys.stdin.readline().split()))
honey_right = honey[:]
honey_left = honey[:]
for i in range(n - 2, -1, -1):
    honey_right[i] += honey_right[i + 1]
for i in range(1, n):
    honey_left[i] += honey_left[i - 1]

result = 0
for i in range(1, n - 1):
    result = max(result, honey_right[1] + honey_right[i + 1] - honey[i])
for i in range(n - 2, 0, -1):
    result = max(result, honey_left[n - 2] + honey_left[i - 1] - honey[i])
for i in range(1, n - 1):
    result = max(result, honey_left[i] - honey_left[0] + honey_right[i] - honey_right[n - 1])
print(result)