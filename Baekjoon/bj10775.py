'''
Created by sunwoong on 2025/04/30
'''

import sys

g = int(sys.stdin.readline())
p = int(sys.stdin.readline())
order = []
for _ in range(p):
    order.append(int(sys.stdin.readline()))
gates = [i for i in range(g + 1)]

def find(x):
    if x == gates[x]:
        return x
    gates[x] = find(gates[x])
    return gates[x]

def union(x, y):
    x = find(x)
    y = find(y)
    if x > y:
        gates[x] = y
    else:
        gates[y] = x

count = 0
for plain in order:
    pos = find(plain)
    if pos == 0:
        break
    count += 1
    union(pos - 1, pos)
print(count)