'''
Created by sunwoong on 2024/08/01

풀이 시간 - 30분
'''
import heapq
from collections import defaultdict
import sys

def solution(n, roads, sources, destination):
    graph = defaultdict(list)
    
    for road in roads:
        graph[road[0]].append(road[1])
        graph[road[1]].append(road[0])

    distance = [sys.maxsize for _ in range(n + 1)]
    distance[destination] = 0
    heap = [(0, destination)]
    
    while heap:
        cost, node = heapq.heappop(heap)
        if distance[node] < cost:
            continue
        
        for next_node in graph[node]:
            if distance[next_node] > cost + 1:
                distance[next_node] = cost + 1
                heapq.heappush(heap, (distance[next_node], next_node))
    answer = []
    for s in sources:
        if distance[s] == sys.maxsize:
            answer.append(-1)
        else:
            answer.append(distance[s])
            
    return answer