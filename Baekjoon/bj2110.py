'''
Created by sunwoong on 2022/03/02

>>> 이진 검색 활용 풀이
'''
import sys

n, c = map(int, sys.stdin.readline().split())
coordinates = [int(sys.stdin.readline()) for _ in range(n)]
coordinates.sort()
low, high = 0, coordinates[-1] - coordinates[0]
while low <= high:
    mid = low + (high - low) // 2
    router, count = 0, 1
    for i in range(1, n):
        if coordinates[i] - coordinates[router] >= mid:
            router = i
            count += 1
    if count >= c:
        low = mid + 1
    else:
        high = mid - 1
print(high)