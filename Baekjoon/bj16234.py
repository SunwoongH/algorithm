'''
Created by sunwoong on 2022/09/01
'''
import sys
import collections
from typing import Tuple, Set

n, start, end = map(int, sys.stdin.readline().split())
people = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
union = [[0 for _ in range(n)] for _ in range(n)]

def bfs(start_r: int, start_c: int, allocation_number: int) -> Tuple[Set[Tuple[int]], int]:
    move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
    queue = collections.deque([(start_r, start_c)])
    visited = set()
    visited.add((start_r, start_c))
    union_people = 0
    check = False
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n and (dr, dc) not in visited and (not union[r][c] or union[r][c] != union[dr][dc]) and start <= abs(people[r][c] - people[dr][dc]) <= end:
                if not check:
                    check = True
                union[dr][dc] = allocation_number
                queue.append((dr, dc))
                visited.add((dr, dc))
                union_people += people[dr][dc]
    if check:
        union[start_r][start_c] = allocation_number
        union_people += people[start_r][start_c]
    return visited, union_people
        
day = 0
allocation_number = 1
while True:
    visited_ground = []
    for r in range(n):
        for c in range(n):
            visited, union_people = bfs(r, c, allocation_number)
            if len(visited) > 1:
                visited_ground.append((visited, union_people))
                allocation_number += 1
    for visited, union_people in visited_ground:
        for r, c in visited:
            people[r][c] = union_people // len(visited)
    if not visited_ground:
        break
    day += 1
print(day)