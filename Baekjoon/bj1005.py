'''
Created by sunwoong on 2022/08/17
'''
import sys
import collections
import heapq

def topology_sort(target: int) -> int:
    heap = []
    for u in range(1, n + 1):
        if indegree[u] == 0:
            heapq.heappush(heap, (times[u], u))
    result = 0
    while heap:
        time, u = heapq.heappop(heap)
        if u == target:
            result = max(result, time)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                heapq.heappush(heap, (time + times[v], v))
    return result

test = int(sys.stdin.readline())
for _ in range(test):
    graph = collections.defaultdict(list)
    n, k = map(int, sys.stdin.readline().split())
    times = [0] + list(map(int, sys.stdin.readline().split()))
    indegree = [0 for _ in range(n + 1)]
    for _ in range(k):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        indegree[v] += 1
    target = int(sys.stdin.readline())
    print(topology_sort(target))