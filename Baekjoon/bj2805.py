'''
Created by sunwoong on 2022/03/01

>>> 이진 검색 활용 풀이
'''
import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))
low, high = 1, max(trees)
while low <= high:
    mid = low + (high - low) // 2
    length = sum(tree - mid for tree in trees if tree > mid)
    if length >= m:
        low = mid + 1
    else:
        high = mid - 1
print(high)