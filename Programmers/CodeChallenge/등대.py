'''
Created by sunwoong on 2025/04/17
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

def dfs(graph, curr, visited, dp):
    visited[curr] = True
    for node in graph[curr]:
        if not visited[node]:
            cost = dfs(graph, node, visited, dp)
            dp[curr][0] += cost[1]
            dp[curr][1] += min(cost[0], cost[1])
    return dp[curr]

def solution(n, lighthouse):
    graph = defaultdict(list)
    for u, v in lighthouse:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)
    dp = [[0, 1] for _ in range(n)]
    visited = [False for _ in range(n)]
    dfs(graph, 0, visited, dp)
    return min(dp[0][0], dp[0][1])