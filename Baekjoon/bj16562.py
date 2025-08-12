'''
Created by sunwoong 2025/08/12
'''
import sys
from collections import defaultdict
sys.setrecursionlimit(10 ** 6)

def dfs(node, students, visited, graph):
    visited[node] = True
    cost = students[node - 1]

    for next_node in graph[node]:
        if not visited[next_node]:
            cost = min(dfs(next_node, students, visited, graph), cost)
    
    return cost

n, m, k = list(map(int, sys.stdin.readline().split()))
students = list(map(int, sys.stdin.readline().split()))
edges = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

visited = [False for _ in range(n + 1)]
visited[0] = True
graph = defaultdict(list)
for u, v in edges:
    graph[u].append(v)
    graph[v].append(u)

answer = 0

for i in range(1, n + 1):
    if not visited[i]:
        answer += dfs(i, students, visited, graph)

if all(visited) and answer <= k:
    print(answer)
else:
    print("Oh no")