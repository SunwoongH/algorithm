'''
Created by sunwoong on 2023/03/03
'''
import sys
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
    total = 0
    edge_count = 0
    while edge_count < n - 1:
        a, b, cost = edges.pop()
        parent_a = find(a)
        parent_b = find(b)
        if parent_a != parent_b:
            union(parent_a, parent_b)
            edge_count += 1
            total += cost
    return total

n, m = map(int, input().split())
parent = [i for i in range(n)]
edges = []
costs = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    costs += c
    edges.append((a, b, c))
edges.sort(key=lambda x: x[2], reverse=True)
print(costs - kruskal())