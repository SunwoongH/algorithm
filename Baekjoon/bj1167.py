'''
Created by sunwoong on 2022/03/04

>>> 입력된 트리에서 DFS(깊이 우선 탐색)를 활용하여 임의의 두 정점 사이의 거리 중 가장 긴 거리를 구하는 풀이
'''
import sys
import collections

n = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    queue = collections.deque(data)
    u = queue.popleft()
    while queue[0] != -1:
        v = queue.popleft()
        length = queue.popleft()
        graph[u].append((v, length))

visited = [False] * (n + 1)
max_length = 0
def dfs(u: int) -> int:
    global max_length
    visited[u] = True
    length = [0]
    for v in graph[u]:
        if not visited[v[0]]:
            length.append(dfs(v[0]) + v[1])
    if len(length) >= 2:
        length.sort(reverse=True)
        max_length = max(max_length, length[0] + length[1])
    else:
        max_length = max(max_length, length[0])
    return max(length)
dfs(1)
print(max_length)