'''
Created by sunwoong on 2022/12/15
'''
from collections import deque

parents = None

def find(a):
    while parents[a] != -1:
        a = parents[a]
    return a

def union(a, b):
    if a > b:
        parents[a] = b
    else:
        parents[b] = a
        
def kruskal(n, edges):
    edge_count = 0
    total_cost = 0
    while edge_count < n - 1:
        a, b, cost = edges.popleft()
        parent_a = find(a)
        parent_b = find(b)
        if parent_a != parent_b:
            union(parent_a, parent_b)
            edge_count += 1
            total_cost += cost
    return total_cost

def solution(n, costs):
    global parents
    parents = [-1 for _ in range(n)]
    return kruskal(n, deque(sorted(costs, key=lambda x: x[2])))