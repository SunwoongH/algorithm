'''
Created by sunwoong on 2022/08/07
'''
import sys
from typing import Tuple

n = int(sys.stdin.readline())
houes =[list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = 0
horizontal = [(0, 1),(1, 1)]
vertical = [(1, 0), (1, 1)]
diagonal = [(0, 1), (1, 0), (1, 1)]

def dfs(rear: Tuple[int], front: Tuple[int]) -> None:
    if front[0] == n - 1 and front[1] == n - 1:
        global result
        result += 1
        return
    for oper in horizontal if rear[0] == front[0] else vertical if rear[1] == front[1] else diagonal:
        dr = front[0] + oper[0]
        dc = front[1] + oper[1]
        if dr < n and dc < n and not houes[dr][dc]:
            if oper[0] == oper[1]:
                if dr - 1 < n and dc < n and dr < n and dc - 1 < n and not houes[dr - 1][dc] and not houes[dr][dc - 1]:
                    dfs(front, (dr, dc))
            else:
                dfs(front, (dr, dc))
                
if houes[n - 1][n - 1] == 1:
    print(result)
else:
    dfs((0, 0), (0, 1))
    print(result)