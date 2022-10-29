'''
Created by sunwoong on 2022/10/29
'''
import sys

h, w = map(int, sys.stdin.readline().split())
height = list(map(int, sys.stdin.readline().split()))
left_max_height = [0 for _ in range(w)]
right_max_height = [0 for _ in range(w)]
left_max_height[0] =  height[0]
right_max_height[-1] = height[-1]
for i in range(1, w):
    left_max_height[i] = max(left_max_height[i - 1], height[i])
    right_max_height[w - i - 1] = max(right_max_height[w - i], height[w - i - 1])
result = 0
for i in range(w):
    min_height = min(left_max_height[i], right_max_height[i])
    result += min_height - height[i]
print(result)