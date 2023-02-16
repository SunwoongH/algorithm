'''
Created by sunwoong on 2023/02/16
'''
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))
low, high = 0, max(rice_cakes)
while low <= high:
    mid = (low + high) // 2
    total = 0
    for cake in rice_cakes:
        if mid < cake:
            total += cake - mid
    if total >= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)