'''
Created by sunwoong on 2023/02/24
'''
import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

n, m, c = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    distance = [sys.maxsize for _ in range(n + 1)]
    distance[start] = 0
    queue = [(0, start)]
    while queue:
        cost, curr = heapq.heappop(queue)
        if distance[curr] < cost:
            continue
        for next, next_cost in graph[curr]:
            if distance[next] > distance[curr] + next_cost:
                distance[next] = distance[curr] + next_cost
                heapq.heappush(queue, (distance[next], next))
    max_time = 0
    count = -1
    for i in range(1, n + 1):
        if distance[i] != sys.maxsize:
            count += 1
            max_time = max(max_time, distance[i])
    return count, max_time

print(*dijkstra(c))