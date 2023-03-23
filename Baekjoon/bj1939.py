'''
Created by sunwoong on 2023/03/23
'''
import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

def dijkstra(start, end):
    heap = [(-sys.maxsize, start)]
    weight = [0 for _ in range(n + 1)]
    weight[start] = sys.maxsize
    while heap:
        cost, curr = heapq.heappop(heap)
        cost = abs(cost)
        if weight[curr] > cost:
            continue
        for next, next_cost in graph[curr]:
            if weight[next] < min(cost, next_cost):
                weight[next] = min(weight[curr], next_cost)
                heapq.heappush(heap, (-weight[next], next))
    return weight[end]

n, m = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
start, end = map(int, input().split())
print(dijkstra(start, end))