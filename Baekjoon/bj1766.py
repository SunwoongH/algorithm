'''
Created by sunwoong on 2022/08/29
'''
import sys
import heapq
import collections
from typing import List

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
indegree = [0 for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort() -> List[int]:
    result = []
    heap = []
    for i in range(1, n + 1):
        if indegree[i] == 0:
            heapq.heappush(heap, i)
    while heap:
        curr = heapq.heappop(heap)
        result.append(curr)
        for next in graph[curr]:
            indegree[next] -= 1
            if indegree[next] == 0:
                heapq.heappush(heap, next)
    return result
print(*topology_sort())