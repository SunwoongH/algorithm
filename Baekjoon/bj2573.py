'''
Created by sunwoong on 2022/12/28
'''
import sys
from collections import deque
input = sys.stdin.readline

SEA = 0

def melt_ice(iceberg):
    next_iceberg = []
    counting = []
    for r, c in iceberg:
        count = 0
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if ocean[dr][dc] == SEA:
                count += 1
        counting.append(count)
    for i, pos in enumerate(iceberg):
        r, c = pos
        if ocean[r][c] - counting[i] > 0:
            ocean[r][c] -= counting[i]
            next_iceberg.append((r, c))
        else:
            ocean[r][c] = SEA
    return next_iceberg

def check_island(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if ocean[dr][dc] != SEA and not visited[(dr, dc)]:
                visited[(dr, dc)] = True
                queue.append((dr, dc))

n, m = map(int, input().split())
ocean = []
iceberg = []
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
for i in range(n):
    line = list(map(int, input().split()))
    for j in range(m):
        if line[j] != SEA:
            iceberg.append((i, j))
    ocean.append(line)            
answer = 0
is_promising = False
while True:
    answer += 1
    iceberg = melt_ice(iceberg)
    visited = dict()
    for r, c in iceberg:
        visited[(r, c)] = False
    if iceberg:
        check_island(iceberg[0])
        if not all(visited.values()):
            is_promising = True
            break
    else:
        break
print(answer) if is_promising else print(0)