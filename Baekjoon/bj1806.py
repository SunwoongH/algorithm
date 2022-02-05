'''
문제 - 부분 합

풀이 방법 - 투 포인터 활용하여 풀이
'''
import sys

n, s = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
result = sys.maxsize
left, right = 0, 0
target = nums[0]
while True:
    if target < s:
        right += 1
        if right == n:
            break
        target += nums[right]
    else:
        result = min(result, right - left + 1)
        target -= nums[left]
        left += 1
if result == sys.maxsize:
    print(0)
else:
    print(result)