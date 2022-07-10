'''
Created by sunwoong on 2022/07/10
'''
import sys
import collections
import heapq

n, e = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(e):
    u, v, cost = map(int, sys.stdin.readline().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))
u, v = map(int, sys.stdin.readline().split())
    
def dijkstra(start: int, end: int) -> int:
    distance = [sys.maxsize] * (n + 1)
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

path = min(dijkstra(1, u) + dijkstra(u, v) + dijkstra(v, n), dijkstra(1, v) + dijkstra(v, u) + dijkstra(u, n))
if path >= sys.maxsize:
    print(-1)
else:
    print(path)