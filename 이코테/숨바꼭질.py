'''
Created by sunwoong on 2023/03/03
'''
import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

def dijkstra(start):
    distance = [sys.maxsize for _ in range(n + 1)]
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        cost, curr = heapq.heappop(heap)
        if distance[curr] < cost:
            continue
        for next, next_cost in graph[curr]:
            if distance[next] > distance[curr] + next_cost:
                distance[next] = distance[curr] + next_cost
                heapq.heappush(heap, (distance[next], next))
    max_distance = 0
    nodes = []
    for i in range(1, n + 1):
        if max_distance < distance[i]:
            max_distance = distance[i]
            nodes = [i]
        elif max_distance == distance[i]:
            nodes.append(i)
    return max_distance, nodes

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append((b, 1))
    graph[b].append((a, 1))
max_distance, nodes = dijkstra(1)
print(nodes[0], max_distance, len(nodes))