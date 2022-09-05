'''
Created by sunwoong on 2022/09/05
'''
import sys

n, k = map(int, sys.stdin.readline().split())
origin_k = k
sequence = list(map(int, sys.stdin.readline().split()))

left = right = 0
result = 0
while right < n:
    if sequence[right] % 2 != 0:
        k -= 1
    right += 1
    while k < 0:
        if sequence[left] % 2 != 0:
            k += 1
        left += 1
    result = max(result, right - left)
print(result - origin_k + k)