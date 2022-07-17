'''
Created by sunwoong on 2022/07/17
'''
import sys
import collections
from typing import List

def diffusion(dust: List[int]) -> None:
    move = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    queue = collections.deque(dust)
    while queue:
        r, c, cost = queue.popleft()
        count = 0
        for pos in move:
            dr = r + pos[0]
            dc = c + pos[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < m and room[dr][dc] != -1:
                room[dr][dc] += cost // 5
                count += 1
        room[r][c] -= (cost // 5) * count
        
def left_rotate(pivot: int) -> None:
    curr_item = None
    check = True
    for pos in range(pivot + 1):
        if check and room[pos][0] == -1:
            curr_item = None
            room[pos].insert(1, 0)
            continue
        next_item = room[pos].popleft()
        if curr_item is not None:
            room[pos].appendleft(curr_item)
        curr_item = next_item
    for pos in range(pivot, 0, -1):
        next_item = room[pos].pop()
        if curr_item is not None:
            room[pos].append(curr_item)
        curr_item = next_item
    room[0].append(curr_item)
    
def right_rotate(pivot: int) -> None:
    curr_item = None
    check = True
    for pos in range(n - 1, pivot - 1, -1):
        if check and room[pos][0] == -1:
            curr_item = None
            room[pos].insert(1, 0)
            continue
        next_item = room[pos].popleft()
        if curr_item is not None:
            room[pos].appendleft(curr_item)
        curr_item = next_item
    for pos in range(pivot, n - 1):
        next_item = room[pos].pop()
        if curr_item is not None:
            room[pos].append(curr_item)
        curr_item = next_item
    room[n - 1].append(curr_item)

n, m, t = map(int, sys.stdin.readline().split())
room = []
air_purifier = []
for time in range(1, t + 1):
    dust = []
    if time == 1:
        for i in range(n):
            line = collections.deque(list(map(int, sys.stdin.readline().split())))
            for j in range(m):
                if line[j] >= 5:
                    dust.append((i, j, line[j]))
                elif line[j] == -1:
                    air_purifier.append((i, j))
            room.append(line)
    else:
        for i in range(n):
            for j in range(m):
                if room[i][j] >= 5:
                    dust.append((i, j, room[i][j]))
    diffusion(dust)
    left_rotate(air_purifier[0][0])
    right_rotate(air_purifier[1][0])
print(sum(map(sum, room)) + 2)