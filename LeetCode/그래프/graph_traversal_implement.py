'''
Graph Traversal implement

DFS(Depth First Search) & BFS(Breadth First Search) 구현하기
'''

graph = {
    1 : [2, 3, 4],
    2 : [5], 
    3 : [5],
    4 : [],
    5 : [6, 7],
    6 : [],
    7 : [3],
}

# DFS 재귀 구조로 구현
def recursive_dfs(v, visited=[]):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            visited = recursive_dfs(w, visited)
    return visited

# DFS 반복 구조로 구현 - 스택 ADT
def iterative_dfs(v):
    visited = []
    stack = [v]
    while stack:
        v = stack.pop()
        if v not in visited:
            visited.append(v)
            for w in graph[v]:
                stack.append(w)
    return visited

# BFS 반복 구조로 구현 - 큐 ADT
def iterative_bfs(v):
    visited = [v]
    queue = [v]
    while queue:
        v = queue.pop(0)
        for w in graph[v]:
            if w not in visited:
                visited.append(w)
                queue.append(w)
    return visited
        
print(*recursive_dfs(1))
print(*iterative_dfs(1))
print(*iterative_bfs(1))