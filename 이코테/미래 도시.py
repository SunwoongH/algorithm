'''
Created by sunwoong on 2023/02/24
'''
import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
x, k = map(int, input().split())

def dijkstra(start, end):
    distance = [int(1e9) for _ in range(n + 1)]
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        cost, curr = heapq.heappop(queue)
        if distance[curr] < cost:
            continue
        for next in graph[curr]:
            if distance[next] > distance[curr] + 1:
                distance[next] = distance[curr] + 1
                heapq.heappush((distance[next], next))
    return distance[end]

total = dijkstra(1, k) + dijkstra(k, x)
print(total) if total < int(1e9) else print(-1)