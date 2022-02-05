'''
문제 - 바이러스

풀이 방법 - graph를 인접 리스트로 만든 후 DFS(재귀)로 풀이
'''
import sys
import collections

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(m):
    v, w = map(int, sys.stdin.readline().split())
    graph[v].append(w)
    graph[w].append(v)
    
visited = []
def dfs(v):
    visited.append(v)
    for w in graph[v]:
        if w not in visited:
            dfs(w)
dfs(1)
print(len(visited) - 1)