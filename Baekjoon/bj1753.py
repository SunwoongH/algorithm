'''
문제 - 최단경로

풀이 방법 - 우선순위 큐(heap)를 활용한 다익스트라 풀이
'''
from typing import List
import sys, collections, heapq

n, e = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(e):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))
    
def dijkstra(n: int, start: int) -> List[int]:
    distance = [float('inf')] * (n + 1)
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        dist, v = heapq.heappop(heap)
        if distance[v] < dist:
            continue
        for adj_v, adj_dist in graph[v]:
            if distance[adj_v] > distance[v] + adj_dist:
                distance[adj_v] = distance[v] + adj_dist
                heapq.heappush(heap, (distance[adj_v], adj_v))
    return distance
    
distance = dijkstra(n, k)
for i in range(1, n + 1):
    if distance[i] == float('inf'): print('INF')
    else: print(distance[i])