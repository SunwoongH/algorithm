'''
Created by sunwoong on 2022/11/22
'''
import sys
from collections import defaultdict

def dfs(curr, end, total):
    if curr == end:
        print(total)
        return
    visited[curr] = True
    for next, distance in graph[curr]:
        if not visited[next]:
            dfs(next, end, total + distance)

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(n - 1):
    u, v, cost = map(int, sys.stdin.readline().split())
    graph[u].append((v, cost))
    graph[v].append((u, cost))
for _ in range(m):
    start, end = map(int, sys.stdin.readline().split())
    visited = [False for _ in range(n + 1)]
    dfs(start, end, 0)