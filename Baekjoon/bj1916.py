'''
Created by sunwoong on 2022/07/13
'''
import sys
import heapq
import collections

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))
start, end = map(int, sys.stdin.readline().split())

def dijkstra(start: int, end: int) -> int:
    distance = [sys.maxsize for _ in range(n + 1)]
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        cost, u = heapq.heappop(heap)
        if distance[u] < cost:
            continue
        for adj_v, adj_cost in graph[u]:
            if distance[adj_v] > cost + adj_cost:
                distance[adj_v] = cost + adj_cost
                heapq.heappush(heap, (distance[adj_v], adj_v))
    return distance[end]
print(dijkstra(start, end))