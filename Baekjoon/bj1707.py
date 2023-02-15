'''
Created by sunwoong on 2023/02/15
'''
import sys
from collections import defaultdict
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

RED = 1
BLUE = 2

def is_bipartite_graph(color, curr):
    visited[curr] = color
    for next in graph[curr]:
        if not visited[next]:
            if not is_bipartite_graph(BLUE if color == RED else RED, next):
                return False
        elif visited[next] == visited[curr]:
            return False
    return True

k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    visited = [False for _ in range(v + 1)]
    answer = True
    for i in range(1, v + 1):
        if not visited[i]:
            answer = is_bipartite_graph(RED, i)
            if not answer:
                break
    print("YES") if answer else print("NO")