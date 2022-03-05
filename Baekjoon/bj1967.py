'''
Created by sunwoong on 2022/03/05

>>> 입력된 트리에서 DFS(깊이 우선 탐색)를 활용하여 임의의 두 정점 사이의 거리 중 가장 긴 거리를 구하는 풀이
'''
import sys
import collections
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
graph = collections.defaultdict(list)
for _ in range(n - 1):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

max_length = 0
def dfs(u: int) -> int:
    global max_length
    length = [0]
    for v, w in graph[u]:
        length.append(dfs(v) + w)
    if len(length) >= 2:
        length.sort(reverse=True)
        max_length = max(max_length, length[0] + length[1])
    else:
        max_length = max(max_length, length[0])
    return max(length)
dfs(1)
print(max_length)