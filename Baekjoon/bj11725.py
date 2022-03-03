'''
Created by sunwoong on 2022/03/03

>>> BFS(너비 우선 탐색)을 활용하여 각 노드의 부모 노드를 찾는 풀이
'''
import sys
import collections

n = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(n - 1):
    v, w = map(int, sys.stdin.readline().split())
    graph[v].append(w)
    graph[w].append(v)
    
parents = [None] * (n + 1)
visited = [False] * (n + 1)
def bfs(v):
    visited[v] = True
    queue = collections.deque([v])
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                parents[w] = v
                queue.append(w)
bfs(1)
for i in range(2, n + 1):
    print(parents[i])