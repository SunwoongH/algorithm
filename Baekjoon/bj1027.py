'''
Created by sunwoong on 2022/12/12
'''
import sys
input = sys.stdin.readline

n = int(input())
heights = list(zip(range(1, n + 1), list(map(int, input().split()))))
answer = 0
for i in range(n):
    inclines = []
    for j in range(n):
        if i == j:
            inclines.append(0)
            continue
        incline = (heights[i][1] - heights[j][1]) / (heights[i][0] - heights[j][0])
        inclines.append(incline)
    left = right = 0
    left_pivot = right_pivot = None
    for k in range(i - 1, -1, -1):
        if left_pivot is None:
            left_pivot = inclines[k]
            left += 1
            continue
        if left_pivot > inclines[k]:
            left_pivot = inclines[k]
            left += 1
    for k in range(i + 1, n):
        if right_pivot is None:
            right_pivot = inclines[k]
            right += 1
            continue
        if right_pivot < inclines[k]:
            right_pivot = inclines[k]
            right += 1
    answer = max(answer, left + right)
print(answer)