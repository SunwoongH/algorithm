'''
Created by sunwoong on 2025/08/05
'''
from collections import deque, defaultdict

def bfs(start, graph, n):
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    queue = deque([(start, 0)])
    
    target, distance, is_unique = None, 0, True
    
    while queue:
        node, cost = queue.popleft()
        
        if cost > distance:
            target, distance, is_unique = node, cost, True
        elif cost == distance:
            is_unique = False
        
        for next_node in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, cost + 1))
    
    return [target, distance, is_unique]

def solution(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    start, _, _ = bfs(1, graph, n)
    
    start, distance, is_unique = bfs(start, graph, n)
    
    if not is_unique:
        return distance
    
    _, _, is_unique = bfs(start, graph, n)
    
    if is_unique:
        return distance - 1

    return distance