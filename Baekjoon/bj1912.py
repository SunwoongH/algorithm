'''
Created by sunwoong on 2022/07/22
'''
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
result = nums[0]
for i in range(1, len(nums)):
    nums[i] = max(nums[i], nums[i - 1] + nums[i])
    result = max(result, nums[i])
print(result)