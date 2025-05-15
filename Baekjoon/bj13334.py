'''
Created by sunwoong on 2025/05/15
'''
import sys
import heapq

n = int(sys.stdin.readline())
point = []
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    point.append(sorted([a, b]))
d = int(sys.stdin.readline())
point.sort(key=lambda x: x[1])
seen = []
answer = 0

for start, end in point:
    init = end - d
    heapq.heappush(seen, start)
    while seen:
        start = heapq.heappop(seen)
        if start >= init:
            heapq.heappush(seen, start)
            break
    answer = max(answer, len(seen))
print(answer)