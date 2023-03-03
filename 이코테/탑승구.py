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

gate = int(input())
airplane = int(input())
parent = [i for i in range(gate + 1)]
result = 0
for _ in range(airplane):
    data = int(input())
    possible = find(data)
    if not possible:
        break
    union(possible - 1, possible)
    result += 1
print(result)