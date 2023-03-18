'''
Created by sunwoong on 2023/03/18
'''
import sys
from collections import deque
input = sys.stdin.readline

def is_finish(baby_shark):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque([baby_shark])
    board[baby_shark[0]][baby_shark[1]] = 0
    visited[baby_shark[0]][baby_shark[1]] = True
    while queue:
        r, c = queue.popleft()
        if baby_shark != (r, c) and board[r][c] and board[r][c] < size:
            board[baby_shark[0]][baby_shark[1]] = BABY_FISH
            return False
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n and not visited[dr][dc] and board[dr][dc] <= size:
                visited[dr][dc] = True
                queue.append((dr, dc))
    return True


def eat_fish(baby_shark):
    visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque([(*baby_shark, 0)])
    board[baby_shark[0]][baby_shark[1]] = 0
    visited[baby_shark[0]][baby_shark[1]] = True
    fish = []
    check = False
    minimum_count = None
    while queue:
        r, c, count = queue.popleft()
        if baby_shark != (r, c) and board[r][c] and board[r][c] < size:
            if not check:
                check = True
                fish.append((r, c))
                minimum_count = count
            else:
                if minimum_count == count:
                    fish.append((r, c))
                else:
                    break
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n and not visited[dr][dc] and board[dr][dc] <= size:
                visited[dr][dc] = True
                queue.append((dr, dc, count + 1))
    fish.sort()
    board[fish[0][0]][fish[0][1]] = BABY_FISH
    return (fish[0], minimum_count)

BABY_FISH = 9
n = int(input())
board = []
move = [(-1, 0), (0, -1), (1, 0), (0, 1)]
baby_shark = None
for r in range(n):
    line = list(map(int, input().split()))
    for c in range(n):
        if line[c] == BABY_FISH:
            baby_shark = (r, c)
            break
    board.append(line)
size = 2
time = 0
fish = 0
while True:
    if is_finish(baby_shark):
        print(time)
        break
    result = eat_fish(baby_shark)
    baby_shark = result[0]
    fish += 1
    if fish == size:
        size += 1
        fish = 0
    time += result[1]