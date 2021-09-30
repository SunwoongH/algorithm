import sys

nums = list(sys.stdin.readline())
del nums[len(nums) - 1]
newNums = sorted(nums, reverse=True)
print(int(''.join(newNums)))