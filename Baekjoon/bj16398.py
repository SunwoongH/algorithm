'''
Created by sunwoong on 2023/01/04
'''
import sys
input = sys.stdin.readline

parent = None

def find(a):
    while parent[a] != -1:
        a = parent[a]
    return a

def union(a, b):
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

n = int(input())
parent = [-1 for _ in range(n)]
board = [list(map(int, input().split())) for _ in range(n)]
edges = []
for r in range(n):
    for c in range(r + 1, n):
        edges.append((r, c, board[r][c]))
edges.sort(key=lambda x: -x[2])
edge_count = 0
answer = 0
while edge_count < n - 1:
    a, b, cost = edges.pop()
    parent_a = find(a)
    parent_b = find(b)
    if parent_a != parent_b:
        union(parent_a, parent_b)
        edge_count += 1
        answer += cost
print(answer)