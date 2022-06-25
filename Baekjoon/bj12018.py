'''
Created by sunwoong on 2022/06/25
'''
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
result = 0
heap = []
for _ in range(n):
    people, threshold = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    data.sort(reverse=True)
    if threshold > people:
        heapq.heappush(heap, 1)
    else:
        heapq.heappush(heap, data[threshold - 1])

while heap:
    target = heapq.heappop(heap)
    if m - target >= 0:
        m -= target
        result += 1
    else:
        break
print(result)