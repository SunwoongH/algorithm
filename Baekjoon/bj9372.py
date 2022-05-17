'''
Created by sunwoong 2022/05/17
'''
import sys
import collections

def bfs(u: int) -> None:
    global count
    visited[u] = True
    queue = collections.deque([u])
    while queue:
        u = queue.popleft()
        count += 1
        for v in graph[u]:
            if not visited[v]:
                queue.appendleft(v)
                visited[v] = True

test = int(sys.stdin.readline())
for _ in range(test):
    n, m = map(int, sys.stdin.readline().split())
    graph = collections.defaultdict(list)
    visited = [False] * (n + 1)
    count = -1
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    bfs(1)
    print(count)