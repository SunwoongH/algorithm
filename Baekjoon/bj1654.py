'''
Created by sunwoong on 2022/02/28

>>> 이진 검색 활용 풀이
'''
import sys

k, n = map(int, sys.stdin.readline().split())
lans = [int(sys.stdin.readline()) for _ in range(k)]
max_length = sum(lans) // n
left, right = 1, max_length
while left <= right:
    mid = left + (right - left) // 2
    length = 0
    for lan in lans:
        length += lan // mid
    if length >= n:
        left = mid + 1
    else:
        right = mid - 1
print(right)