'''
Created by sunwoong 2022/05/10
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
   
def bfs(u) -> None:
    visited[u] = True
    queue = collections.deque([[u, 0]])
    while queue:
        u = queue.popleft()
        count[u[0]] = u[1]
        for v in graph[u[0]]:
            if not visited[v]:
                visited[v] = True
                queue.append([v, u[1] + 1])

result = dict()
for u in range(1, n + 1):
    visited = [False] * (n + 1)     
    count = collections.defaultdict(int)
    bfs(u)
    result[u] = sum(count.values())
print(min(result.items(), key=lambda x: x[1])[0])