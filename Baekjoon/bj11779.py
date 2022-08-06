'''
Created by sunwoong on 2022/08/06
'''
import sys
import collections
import heapq
from typing import Tuple, List

def dijkstra(start: int, end: int) -> Tuple[int, List[int]]:
    distance = [sys.maxsize for _ in range(n + 1)]
    parent = [None for _ in range(n + 1)]
    distance[start] = 0
    path = collections.deque()
    heap = [(0, start, None)]
    while heap:
        cost, curr, prev = heapq.heappop(heap)
        if distance[curr] < cost:
            continue
        parent[curr] = prev
        for adj_v, adj_cost in graph[curr]:
            if distance[adj_v] > cost + adj_cost:
                distance[adj_v] = cost + adj_cost
                heapq.heappush(heap, (distance[adj_v], adj_v, curr))
    curr = end
    path.appendleft(end)
    while curr != start:
        curr = parent[curr]
        path.appendleft(curr)
    return distance[end], path

graph = collections.defaultdict(list)
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
for _ in range(m):
    u, v, cost = map(int, sys.stdin.readline().split())
    graph[u].append((v, cost))
start, end = map(int, sys.stdin.readline().split())
min_cost, min_path = dijkstra(start, end)
print(min_cost, len(min_path), sep='\n')
print(*min_path)