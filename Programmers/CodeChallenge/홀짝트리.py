'''
Created by sunwoong on 2025/07/29
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(node, graph, visited, result):
    visited[node] = True
    
    if (node % 2) == (len(graph[node]) % 2):
        result[0] += 1
    else:
        result[1] += 1
    
    for next_node in graph[node]:
        if not visited[next_node]:
            dfs(next_node, graph, visited, result)

def solution(nodes, edges):
    graph = defaultdict(list)
    visited = [False for _ in range(max(nodes) + 1)]
    answer = [0, 0]
    
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    
    for node in nodes:
        if not visited[node]:
            result = [0, 0]
            dfs(node, graph, visited, result)
            if result[0] == 1:
                answer[0] += 1
            if result[1] == 1:
                answer[1] += 1
    
    return answer