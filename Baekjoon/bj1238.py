'''
Created by sunwoong on 2022/07/12
'''
import sys
import heapq
import collections

n, m, x = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().split())
    graph[start].append((end, cost))

def dijkstra(is_select: bool, start: int, end=None):
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
    return distance if not is_select else distance[end]

call_distance = [0] + [dijkstra(True, i, x) for i in range(1, n + 1)]
callback_distance = dijkstra(False, x)
distance = [call_distance[i] + callback_distance[i] for i in range(1, n + 1)]
print(max(distance))