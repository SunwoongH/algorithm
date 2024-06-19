'''
Created by sunwoong on 2024/06/19

풀이 시간 - 20분
'''
from collections import deque

move = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def bfs(maps):
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    queue = deque([(0, 0, 1)])
    visited[0][0] = True
    while queue:
        r, c, count = queue.popleft()
        if r == len(maps) - 1 and c == len(maps[0]) - 1:
            return count
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < len(maps) and 0 <= dc < len(maps[0]):
                if maps[dr][dc] and not visited[dr][dc]:
                    visited[dr][dc] = True
                    queue.append((dr, dc, count + 1))
    return -1

def solution(maps):
    return bfs(maps)