'''
Created by sunwoong on 2022/12/09
'''
from collections import defaultdict, deque

def bfs(n, start, graph):
    queue = deque([(start, 0)])
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    result = 0
    shortest_path = -1
    while queue:
        curr, edge_count = queue.popleft()
        if edge_count > shortest_path:
            result = 1
            shortest_path = edge_count
        elif edge_count == shortest_path:
            result += 1
        for next in graph[curr]:
            if not visited[next]:
                visited[next] = True
                queue.append((next, edge_count + 1))
    return result

def solution(n, edge):
    graph = defaultdict(list)
    for u, v in edge:
        graph[u].append(v)
        graph[v].append(u)
    return bfs(n, 1, graph)