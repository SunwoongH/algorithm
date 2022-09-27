'''
Created by sunwoong on 2022/09/27
'''
from collections import deque

def bfs(r, c, maps):
    move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(r, c, 1)])
    maps[r][c] = 0
    while queue:
        r, c, distance = queue.popleft()
        if r == len(maps) - 1 and c == len(maps[0]) - 1:
            return distance
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < len(maps) and 0 <= dc < len(maps[0]) and maps[dr][dc]:
                maps[dr][dc] = 0
                queue.append((dr, dc, distance + 1))
    return -1

def solution(maps):
    return bfs(0, 0, maps)