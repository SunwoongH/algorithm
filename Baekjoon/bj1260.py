'''
문제 - DFS와 BFS

풀이 방법 - graph를 인접 리스트로 만든 후 DFS(재귀), BFS(반복)로 풀이
'''
import sys
import collections

n, m, start = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    v, w = map(int, sys.stdin.readline().split())
    graph[v].append(w)
    graph[w].append(v)
for edge in graph:
    graph[edge].sort()
    
visited_dfs = []
visited_bfs = []
def dfs(v):
    visited_dfs.append(v)
    for w in graph[v]:
        if w not in visited_dfs:
            dfs(w)

def bfs(v):
    visited_bfs.append(v)
    queue = collections.deque([v])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if w not in visited_bfs:
                visited_bfs.append(w)
                queue.append(w)
dfs(start)
bfs(start)
print(*visited_dfs)
print(*visited_bfs)