'''
Created by sunwoong on 2022/08/06
'''
import sys
import collections
import heapq

def dijkstra(start: int) -> int:
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
    item = 0
    for u in range(1, n + 1):
        if distance[u] <= m:
            item += items[u]
    return item

n, m, r = map(int, sys.stdin.readline().split())
items = [0] + list(map(int, sys.stdin.readline().split()))
graph = collections.defaultdict(list)
for _ in range(r):
    u, v, cost = map(int, sys.stdin.readline().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))
result = 0
for u in range(1, n + 1):
    result = max(result, dijkstra(u))
print(result)