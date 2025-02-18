'''
Created by sunwoong on 2025/02/18
'''

import sys
sys.setrecursionlimit(10 ** 6)

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
outer = set()

def dfs(storage, visited, r, c):
    visited[r][c] = True
    if (r, c) not in outer:
        outer.add((r, c))
        
    for oper in move:
        dr = r + oper[0]
        dc = c + oper[1]
        if 0 <= dr < len(storage) and 0 <= dc < len(storage[0]) and not visited[dr][dc] and storage[dr][dc] == "":
            dfs(storage, visited, dr, dc)
        
def ship_out(storage, request):
    temp = []
    if len(request) == 1:
        for r in range(len(storage)):
            for c in range(len(storage[0])):
                if storage[r][c] == request:
                    is_promising = False
                    for oper in move:
                        dr = r + oper[0]
                        dc = c + oper[1]
                        if dr < 0 or dr >= len(storage) or dc < 0 or dc >= len(storage[0]) or (dr, dc) in outer:
                            is_promising = True
                            break
                    if is_promising:
                        temp.append((r, c))
    else:
        for r in range(len(storage)):
            for c in range(len(storage[0])):
                if storage[r][c] == request[0]:
                    temp.append((r, c))
    for r, c in temp:
        is_promising = False
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if dr < 0 or dr >= len(storage) or dc < 0 or dc >= len(storage[0]) or (dr, dc) in outer:
                is_promising = True
                break
        if is_promising:
            outer.add((r, c))
        storage[r][c] = ""

def solution(storage, requests):
    answer = 0
    storage = list(map(list, storage))
    
    for request in requests:
        visited = [[False for _ in range(len(storage[0]))] for _ in range(len(storage))]
        for r, c in list(outer):
            dfs(storage, visited, r, c)
        ship_out(storage, request)
    
    for r in range(len(storage)):
        for c in range(len(storage[0])):
            if storage[r][c] != "":
                answer += 1
            
    return answer