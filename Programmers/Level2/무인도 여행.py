'''
Created by sunwoong on 2023/04/20
'''
from collections import deque
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(r, c, visited, maps):
    queue = deque([(r, c)])
    visited[r][c] = True
    total = int(maps[r][c])
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < len(maps) and 0 <= dc < len(maps[0]) and not visited[dr][dc] and maps[dr][dc] != 'X':
                visited[dr][dc] = True
                total += int(maps[dr][dc])
                queue.append((dr, dc))  
    return total

def solution(maps):
    visited = [[False for _ in range(len(maps[0]))] for _ in range(len(maps))]
    answer = []
    for r in range(len(maps)):
        for c in range(len(maps[0])):
            if not visited[r][c] and maps[r][c] != 'X':
                print(r, c)
                answer.append(bfs(r, c, visited, maps))
    answer.sort()
    return answer if answer else [-1]