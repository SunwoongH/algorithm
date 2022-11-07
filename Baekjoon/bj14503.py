'''
Created by sunwoong on 2022/11/07
'''
import sys
from collections import deque

WALL = 1
PROMISING = 0
CLEAN = 2
move = {0 : (0, -1), 1 : (-1, 0), 2 : (0, 1), 3 : (1, 0)}
back_move = {0 : (1, 0), 1 : (0, -1), 2 : (-1, 0), 3 : (0, 1)}

def cleaning(start_r: int, start_c: int, direction: int) -> int:
    queue = deque([(start_r, start_c, direction)])
    board[start_r][start_c] = CLEAN
    cleaning_count = 1
    while queue:
        r, c, direction = queue.popleft()
        is_promising = False
        count = 0
        while not is_promising and count <= 4:
            if count == 4:
                br = r + back_move[direction][0]
                bc = c + back_move[direction][1]
                if board[br][bc] != WALL:
                    r = br
                    c = bc
                    count = 0
                    continue
                else:
                    break
            dr = r + move[direction][0]
            dc = c + move[direction][1]
            if board[dr][dc] == PROMISING:
                is_promising = True
                board[dr][dc] = CLEAN
                cleaning_count += 1
                queue.append((dr, dc, (direction + 3) % 4))
            else:
                count += 1
                direction = (direction + 3) % 4
    return cleaning_count

n, m = map(int, sys.stdin.readline().split())
start_r, start_c, direction = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
print(cleaning(start_r, start_c, direction))