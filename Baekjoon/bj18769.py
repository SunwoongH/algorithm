'''
Created by sunwoong on 2022/11/06
'''
import sys
from collections import deque

def find(a):
    while parent[a] != -1:
        a = parent[a]
    return a

def union(a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a
        
def kruskal(n):
    edge_count = 0
    result = 0
    while edge_count < n - 1:
        cost, a, b = edges.popleft()
        parent_a = find(a)
        parent_b = find(b)
        if parent_a != parent_b:
            union(parent_a, parent_b)
            edge_count += 1
            result += cost
    return result

test = int(sys.stdin.readline())
for _ in range(test):
    r, c = map(int, sys.stdin.readline().split())
    parent = [-1 for _ in range(r * c + 1)]
    edges = []
    node = 1
    for _ in range(r):
        costs = list(map(int, sys.stdin.readline().split()))
        for cost in costs:
            edges.append((cost, node, node + 1))
            node += 1
        node += 1
    node = 1
    for _ in range(r - 1):
        costs = list(map(int, sys.stdin.readline().split()))
        for cost in costs:
            edges.append((cost, node, node + c))
            node += 1
    edges = deque(sorted(edges))
    print(kruskal(r * c))