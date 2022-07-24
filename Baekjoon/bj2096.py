'''
Created by sunwoong on 2022/07/24
'''
import sys

min_case = [None for _ in range(3)]
max_case = [None for _ in range(3)]
n = int(sys.stdin.readline())
for i in range(n):
    num1, num2, num3 = map(int, sys.stdin.readline().split())
    if i == 0:
        min_case[0] = max_case[0] = num1
        min_case[1] = max_case[1] = num2
        min_case[2] = max_case[2] = num3
        continue
    min_prev, max_prev = min_case[:], max_case[:]
    min_case[0] = min(min_prev[0], min_prev[1]) + num1
    max_case[0] = max(max_prev[0], max_prev[1]) + num1
    min_case[1] = min(min_prev) + num2
    max_case[1] = max(max_prev) + num2
    min_case[2] = min(min_prev[1], min_prev[2]) + num3
    max_case[2] = max(max_prev[1], max_prev[2]) + num3
print(max(max_case), min(min_case))