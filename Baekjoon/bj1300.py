'''
Created by sunwoong on 2025/03/02
'''

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

low = 1
high = k

answer = 0

while low <= high:
    value = (low + high) // 2
    count = 0
    for i in range(n):
        count += min(n, value // (i + 1))
    if count < k:
        low = value + 1
    else:
        answer = value
        high = value - 1

print(answer)