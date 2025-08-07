'''
Created by sunwoong on 2025/08/08

'''
from collections import defaultdict, deque

def bfs(n, start, graph, lock, key):
    lock_visited = [False for _ in range(n)]
    
    visited = [False for _ in range(n)]
    visited[start] = True
    
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        
        if node in key:
            lock.remove(key[node])
            if lock_visited[key[node]]:
                visited[key[node]] = True
                queue.append(key[node])
            del key[node]
        
        for next_node in graph[node]:
            if not visited[next_node]:
                if next_node in lock:
                    lock_visited[next_node] = True
                else:
                    visited[next_node] = True
                    queue.append(next_node)
    
    return all(visited)

def solution(n, path, order):
    graph = defaultdict(list)
    for u, v in path:
        graph[u].append(v)
        graph[v].append(u)
        
    lock = set()
    key = dict()
    
    for a, b in order:
        key[a] = b
        lock.add(b)
    
    if 0 in lock:
        return False
    
    return bfs(n, 0, graph, lock, key)
