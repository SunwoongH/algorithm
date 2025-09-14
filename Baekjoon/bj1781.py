'''
Created by sunwoong on 2025/09/14
'''
import sys

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(sys.stdin.readline())
items = [[i + 1] + list(map(int, sys.stdin.readline().split())) for i in range(n)]
items.sort(key=lambda x: -x[2])
answer = 0
parent = [i for i in range(n + 1)]

for i in range(n):
    num, deadline, count = items[i]
    pos = find(deadline)
    if pos > 0:
        answer += count
        union(pos - 1, pos)

print(answer)