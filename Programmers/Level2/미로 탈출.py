'''
Created by sunwoong on 2023/04/07
'''
from collections import deque
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(start_r, start_c, end_r, end_c, n, m, maps):
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[start_r][start_c] = True
    queue = deque([(start_r, start_c, 0)])
    while queue:
        r, c, time = queue.popleft()
        if r == end_r and c == end_c:
            return time
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < m and maps[dr][dc] != 'X' and not visited[dr][dc]:
                visited[dr][dc] = True
                queue.append((dr, dc, time + 1))
    return -1

def solution(maps):
    start = mid = end = None
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'E':
                end = (r, c)
            elif maps[r][c] == 'L':
                mid = (r, c)
    go_to_mid = bfs(start[0], start[1], mid[0], mid[1], len(maps), len(maps[0]), maps)
    if go_to_mid == -1:
        return -1
    go_to_end = bfs(mid[0], mid[1], end[0], end[1], len(maps), len(maps[0]), maps)
    if go_to_end == -1:
        return -1
    return go_to_mid + go_to_end