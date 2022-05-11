'''
Created by sunwoong 2022/05/11
'''
import sys
import collections

n = int(sys.stdin.readline())
a, b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)
    
count = 0
visited = [False] * (n + 1)
def dfs(u: int, cnt: int) -> None:
    if u == b:
        global count
        print(cnt)
        sys.exit(0)
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(v, cnt + 1)
dfs(a, 0)
print(-1)