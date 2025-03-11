'''
Created by sunwoong on 2025/03/11
'''
import sys
import heapq

classes = []

answer = 0
n = int(sys.stdin.readline())
nums = []
for _ in range(n):
    s, e = map(int, sys.stdin.readline().split())
    nums.append((s, e))

nums.sort()

for s, e in nums:
    if classes:
        _, ps, pe = heapq.heappop(classes)
        if pe > s:
            heapq.heappush(classes, (pe, ps, pe))
        heapq.heappush(classes, (e, s, e))
    else:
        heapq.heappush(classes, (e, s, e))
    answer = max(answer, len(classes))
print(answer)