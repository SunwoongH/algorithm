'''
Created by sunwoong on 2023/03/30
'''
import sys
import math
input = sys.stdin.readline

parent = None

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def kruskal():
    edge_count = 0
    min_cost = 0
    while edge_count < n - 1 - union_count:
        a, b, cost = edges.pop()
        parent_a = find(a)
        parent_b = find(b)
        if parent_a != parent_b:
            union(parent_a, parent_b)
            edge_count += 1
            min_cost += cost
    return min_cost

n, m = map(int, input().split())
union_count = 0
parent = [i for i in range(n + 1)]
coordinates = []
for _ in range(n):
    x, y = map(int, input().split())
    coordinates.append((x, y))
for _ in range(m):
    a, b = map(int, input().split())
    parent_a = find(a)
    parent_b = find(b)
    if parent_a != parent_b:
        union_count += 1
        union(parent_a, parent_b)
edges = []
for i in range(n):
    for j in range(i + 1, n):
        edges.append((i + 1, j + 1, math.sqrt(pow(coordinates[i][0] - coordinates[j][0], 2) + pow(coordinates[i][1] - coordinates[j][1], 2))))
edges.sort(key=lambda x: x[2], reverse=True)
print("%.2f" %kruskal())