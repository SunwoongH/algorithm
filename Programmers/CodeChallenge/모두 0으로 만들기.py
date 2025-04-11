'''
Created by sunwoong on 2025/04/11
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

answer = 0

def dfs(graph, visited, prev, curr, counting):
    global answer
    visited[curr] = True
    for node in graph[curr]:
        if not visited[node]:
            dfs(graph, visited, curr, node, counting)
    if prev is None:
        return
    if counting[curr] > 0:
        counting[prev] += counting[curr]
        answer += counting[curr]
        counting[curr] = 0
    elif counting[curr] < 0:
        counting[prev] -= abs(counting[curr])
        answer += abs(counting[curr])
        counting[curr] = 0
    
def solution(a, edges):
    if not any(a):
        return 0
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False for _ in range(len(a))]
    dfs(graph, visited, None, 0, a)
    return -1 if any(a) else answer