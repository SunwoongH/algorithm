'''
Created by sunwoong on 2025/10/09
'''
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
graph = defaultdict(list)

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)

dp = [[0, 1] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

def dfs(prev, curr):
    visited[curr] = True
    if prev is not None and len(graph[curr]) == 1 and prev == graph[curr][0]:
        return
    for next_node in graph[curr]:
        if not visited[next_node]:
            dfs(curr, next_node)
    for next_node in graph[curr]:
        if next_node == prev:
            continue
        dp[curr][0] += dp[next_node][1]
        dp[curr][1] += min(dp[next_node])

dfs(None, 1)
print(min(dp[1]))