'''
Created by sunwoong on 2023/03/12
'''
import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

def dijkstra(start):
    heap = []
    distance = [sys.maxsize for _ in range(n + 1)]
    for node in start:
        distance[node] = 0
        heapq.heappush(heap, (0, node))
    while heap:
        cost, curr = heapq.heappop(heap)
        if distance[curr] < cost:
            continue
        for next, next_cost in graph[curr]:
            if distance[next] > cost + next_cost:
                distance[next] = cost + next_cost
                heapq.heappush(heap, (distance[next], next))
    return distance

def find_maximum_city(distance):
    maximum_i = 1
    maximum_cost = distance[maximum_i] if distance[maximum_i] != sys.maxsize else -1
    for i in range(2, n + 1):
        if distance[i] != sys.maxsize and distance[i] > maximum_cost:
            maximum_i = i
            maximum_cost = distance[i]
    return maximum_i, maximum_cost

n, m, k = map(int, input().split())
graph = defaultdict(list)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))
interview = list(map(int, input().split()))
print(*find_maximum_city(dijkstra(interview)), sep='\n')