'''
Created by sunwoong on 2022/11/02
'''
import sys
from collections import deque

PROMISING = '.'
PERSON = '@'
FIRE = '*'
WALL = '#'
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def spread_of_fire(fires):
    queue = deque(fires)
    fires = []
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < h and 0 <= dc < w and (board[dr][dc] == PROMISING or board[dr][dc] == PERSON):
                board[dr][dc] = FIRE
                fires.append((dr, dc))
    return fires

def move_of_person(position):
    queue = deque(position)
    is_escape = False
    position = []
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < h and 0 <= dc < w:
                if board[dr][dc] == PROMISING:
                    board[dr][dc] = PERSON
                    position.append((dr, dc))
            else:
                is_escape = True
                break
        if is_escape:
            break
    return position, is_escape

test = int(sys.stdin.readline())
for _ in range(test):
    fires = []
    position = []
    board = []
    w, h = map(int, sys.stdin.readline().split())
    for r in range(h):
        line = list(sys.stdin.readline().rstrip())
        for c in range(w):
            if line[c] == PERSON:
                position.append((r, c))
            elif line[c] == FIRE:
                fires.append((r, c))
        board.append(line)
    time = 0
    while True:
        fires = spread_of_fire(fires)
        position, is_escape = move_of_person(position)
        time += 1
        if is_escape:
            print(time)
            break
        elif not position:
            print("IMPOSSIBLE")
            break