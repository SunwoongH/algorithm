'''
Created by sunwoong on 2022/08/16
'''
import sys
import heapq
from typing import List

def find(child: int) -> int:
    while parent[child] != -1:
        child = parent[child]
    return child

def union(u_parent: int, v_parent: int) -> None:
    if u_parent > v_parent:
        parent[u_parent] = v_parent
    else:
        parent[v_parent] = u_parent
        
def kruskal(heap: List[int]) -> int:
    i = 0
    result = 0
    while i < n - 1:
        cost, u, v = heapq.heappop(heap)
        u_parent = find(u)
        v_parent = find(v)
        if u_parent != v_parent:
            union(u_parent, v_parent)
            i += 1
            result += cost
    return result

n, e = map(int, sys.stdin.readline().split())
heap = []
parent = [-1 for _ in range(n + 1)]
for _ in range(e):
    u, v, cost = map(int, sys.stdin.readline().split())
    heapq.heappush(heap, (cost, u, v))
print(kruskal(heap))