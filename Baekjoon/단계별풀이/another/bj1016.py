import sys
import math

minV, maxV = map(int, sys.stdin.readline().split())
nums = list([i for i in range(minV, maxV + 1)])

firstV = nums[0]
lastV = nums[len(nums) - 1]
for i in range(2, round(math.sqrt(nums[len(nums) - 1])) + 1):
    start = firstV // (i ** 2)
    for j in range((i ** 2) * start , lastV + 1, i ** 2):
        if j - firstV < 0 or nums[j - firstV] == 0: continue
        else: nums[j - firstV] = 0
print(len(nums) - nums.count(0))