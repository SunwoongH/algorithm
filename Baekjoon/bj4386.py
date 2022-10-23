'''
Created by sunwoong on 2022/10/23
'''
import sys 
import heapq
from math import sqrt
from collections import defaultdict

def find(a: int) -> int:
    while parent[a] != -1:
        a = parent[a]
    return a

def union(a: int, b: int) -> int:
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def kruskal() -> int:
    edge_count = 0
    total_cost = 0
    while edge_count < n - 1:
        cost, a, b = heapq.heappop(edges)
        parent_a = find(a)
        parent_b = find(b)
        if parent_a != parent_b:
            union(parent_a, parent_b)
            edge_count += 1
            total_cost += cost
    return total_cost

n = int(sys.stdin.readline())
edges = []
star = defaultdict(tuple)
parent = [-1 for _ in range(n + 1)]
for i in range(n):
    x, y = map(float, sys.stdin.readline().split())
    star[i] = (x, y)
for i in range(n):
    for j in range(i + 1, n):
        distance = sqrt(pow(star[i][0] - star[j][0], 2) + pow(star[i][1] - star[j][1], 2))
        heapq.heappush(edges, (distance, i, j))
print("%.2f" %kruskal())