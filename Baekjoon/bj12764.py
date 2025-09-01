'''
Created by sunwoong on 2025/09/01
'''
import sys
import heapq
from collections import defaultdict

n = int(sys.stdin.readline())
tasks = []
for _ in range(n):
    p, q = map(int, sys.stdin.readline().split())
    tasks.append((p, q))
tasks.sort(key=lambda x: x[0])

heap = []

answer = 0
sequence = 1
count = defaultdict(int)
waiting = []

for i in range(n):
    p, q = tasks[i]
    if not heap:
        heapq.heappush(heap, (q, sequence))
        count[sequence] += 1
        sequence += 1
    else:
        while heap:
            pq, prev_sequence = heapq.heappop(heap)
            if pq < p:
                heapq.heappush(waiting, prev_sequence)
            else:
                heapq.heappush(heap, (pq, prev_sequence))
                break
        if waiting:
            prev_sequence = heapq.heappop(waiting)
            heapq.heappush(heap, (q, prev_sequence))
            count[prev_sequence] += 1
        else:
            heapq.heappush(heap, (q, sequence))
            count[sequence] += 1
            sequence += 1
    
    answer = max(answer, len(heap))

result = []
for item in count.items():
    result.append(item[1])
print(answer)
print(*result)