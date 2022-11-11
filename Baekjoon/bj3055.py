'''
Created by sunwoong on 2022/11/11
'''
import sys
from collections import deque

ROCK = 'X'
WATER = '*'
PROMISING = '.'
HEDGEHOG = 'S'
END = 'D'

def spread_of_water(water):
    queue = deque(water)
    next_water = []
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < R and 0 <= dc < C and (board[dr][dc] == PROMISING or board[dr][dc] == HEDGEHOG):
                board[dr][dc] = WATER
                next_water.append((dr, dc))
    return next_water

def move_of_hegehog(hedgehog):
    queue = deque(hedgehog)
    next_hedgehog = []
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < R and 0 <= dc < C:
                if board[dr][dc] == PROMISING:
                    board[dr][dc] = HEDGEHOG
                    next_hedgehog.append((dr, dc))
                elif board[dr][dc] == END:
                    return next_hedgehog, True
    return next_hedgehog, False

R, C = map(int, sys.stdin.readline().split())
board = []
hedgehog = []
water = []
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
for i in range(R):
    line = list(sys.stdin.readline().rstrip())
    for j in range(C):
        if line[j] == HEDGEHOG:
            hedgehog.append((i, j))
        elif line[j] == WATER:
            water.append((i, j))
    board.append(line)
time = 0
while True:
    water = spread_of_water(water)
    hedgehog, is_finish = move_of_hegehog(hedgehog)
    time += 1
    if is_finish:
        print(time)
        break
    elif not hedgehog:
        print("KAKTUS")
        break