'''
Created by sunwoong on 2023/05/25
'''

import heapq
import sys
from collections import defaultdict

def solution(N, road, K):
    if N == 1:
        return 1
    graph = defaultdict(list)
    for start, end, cost in road:
        graph[start].append((end, cost))
        graph[end].append((start, cost))
    distance = [sys.maxsize for _ in range(N + 1)]
    distance[1] = 0
    heap = [(0, 1)]
    while heap:
        cost, curr = heapq.heappop(heap)
        if distance[curr] < cost:
            continue
        for next, next_cost in graph[curr]:
            if distance[next] > cost + next_cost:
                distance[next] = cost + next_cost
                heapq.heappush(heap, (distance[next], next))
    answer = 1
    for i in range(2, N + 1):
        if distance[i] <= K:
            answer += 1
    return answer