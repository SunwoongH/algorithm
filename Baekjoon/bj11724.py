'''
Created by sunwoong on 2022/05/08
'''
import sys
import collections
sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (n + 1)
def dfs(u: int) -> None:
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v)

count = 0
for node in range(1, n + 1):
    if not visited[node]:
        count += 1
        dfs(node)
print(count)