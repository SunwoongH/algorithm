'''
Created by sunwoong on 2024/08/28
'''
from collections import defaultdict
import heapq
import sys

def solution(n, paths, gates, summits):
    answer = []
    
    starts = set(gates)
    
    graph = defaultdict(list)
    for u, v, cost in paths:
        graph[u].append((v, cost))
        graph[v].append((u, cost))
        
    maximum = [sys.maxsize for _ in range(n + 1)]
    heap = []
    for summit in summits:
        maximum[summit] = 0
        heapq.heappush(heap, (0, summit, summit))
        
    while heap:
        cost, curr, summit = heapq.heappop(heap)
        if maximum[curr] < cost:
            continue
        
        if curr in starts:
            answer.append([summit, cost])
            continue
        
        for next, next_cost in graph[curr]:
            if maximum[next] > max(next_cost, cost):
                maximum[next] = max(next_cost, cost)
                heapq.heappush(heap, (maximum[next], next, summit))
            elif maximum[next] == max(next_cost, cost):
                if next in starts:
                    answer.append([summit, maximum[next]])
    
    answer.sort(key=lambda x: (x[1], x[0]))
    
    return answer[0]