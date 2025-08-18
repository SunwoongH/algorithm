'''
Created by sunwoong on 2025/08/18
'''
import sys

parent = None

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
if n == 0:
    print(0)
    exit()
items = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
items.sort(key=lambda x: -x[0])
parent = [i for i in range(max(items, key=lambda x: x[1])[1] + 1)]
answer = 0

for i in range(len(items)):
    pos = find(items[i][1])
    if pos == 0:
        continue
    answer += items[i][0]
    union(pos - 1, pos)

print(answer)