'''
문제 - 두 수의 합

풀이 방법 - 정렬 후 투 포인터 활용하여 풀이.
'''
import sys

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
answer = int(sys.stdin.readline())
nums.sort()
result = 0
left, right = 0, n - 1
while left < right:
    target = nums[left] + nums[right]
    if target == answer:
        result += 1
        left += 1
        right -= 1
    elif target < answer:
        left += 1
    else:
        right -= 1
print(result)