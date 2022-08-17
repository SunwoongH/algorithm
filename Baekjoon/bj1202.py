'''
Created by sunwoong on 2022/08/18
'''
import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jewels = []
bags = []
for _ in range(n):
    weight, cost = map(int, sys.stdin.readline().split())
    jewels.append((weight, cost))
for _ in range(k):
    weight = int(sys.stdin.readline())
    bags.append(weight)
jewels.sort()
bags.sort()

result = 0
heap = []
i = 0
for bag in bags:
    while i < n and jewels[i][0] <= bag:
        heapq.heappush(heap, (-jewels[i][1]))
        i += 1
    if heap:
        result += heapq.heappop(heap)
print(abs(result))