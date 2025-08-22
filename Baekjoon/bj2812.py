'''
Created by sunwoong on 2025/08/22
'''
import sys

n, k = map(int, sys.stdin.readline().split())
nums = list(map(int, list(sys.stdin.readline().rstrip())))
stack = []

for i in range(n):
    if not stack:
        stack.append(nums[i])
        continue
    while stack and stack[-1] < nums[i] and k > 0:
        k -= 1
        stack.pop()
    stack.append(nums[i])

while stack and k > 0:
    k -= 1
    stack.pop()

print(int(''.join(map(str, stack))))