'''
Created by sunwoong on 2022/03/09

>>> 트리는 순환 경로가 없는 연결된 그래프이다. 따라서 입력된 그래프에서 순환 경로 여부를 BFS(너비 우선 탐색)로 검사하는 방식으로 풀이하였다.
'''
import sys
import collections

def bfs(u: int) -> bool:
    queue = collections.deque([u])
    is_tree = True
    while queue:
        u = queue.popleft()
        if visited[u]:
            is_tree = False
        else:
            visited[u] = True
            for v in graph[u]:
                if not visited[v]:
                    queue.append(v)
    return is_tree

case = 1
while True:
    n, m = map(int, sys.stdin.readline().split())
    if n == 0 and m == 0:
        break
    graph = collections.defaultdict(list)
    visited = [False for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        graph[u].append(v)
        graph[v].append(u)
    tree = 0
    for u in range(1, n + 1):
        if not visited[u]:
            if bfs(u):
                tree += 1
    if tree == 0:
        print(f'Case {case}: No trees.')
    elif tree == 1:
        print(f'Case {case}: There is one tree.')
    else:
        print(f'Case {case}: A forest of {tree} trees.')
    case += 1