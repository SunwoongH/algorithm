'''
Created by sunwoong on 2025/01/29
'''

from collections import deque

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(s_r, s_c, visited, land, land_table, k):
    queue = deque([(s_r, s_c)])
    path = []
    visited[s_r][s_c] = True
    
    while queue:
        r, c = queue.popleft()
        
        path.append((r, c))
        
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < len(land) and 0 <= dc < len(land[0]):
                if not visited[dr][dc] and land[dr][dc]:
                    visited[dr][dc] = True
                    queue.append((dr, dc))
        
    for r, c in path:
        land_table[(r, c)] = (len(path), k)

def solution(land):
    visited = [[False for _ in range(len(land[0]))] for _ in range(len(land))]
    land_table = dict()
    answer = 0
    
    flag = 1
    
    for r in range(len(land)):
        for c in range(len(land[0])):
            if not visited[r][c] and land[r][c]:
                bfs(r, c, visited, land, land_table, flag)
                flag += 1
    
    for c in range(len(land[0])):
        seen = set()
        for r in range(len(land)):
            if (r, c) in land_table:
                if land_table[(r, c)] not in seen:
                    seen.add(land_table[(r, c)])
        answer = max(sum([cost for cost, _ in seen]), answer)
            
    return answer