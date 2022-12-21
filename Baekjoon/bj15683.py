'''
Created by sunwoong on 2022/12/21
'''
import sys
from copy import deepcopy
input = sys.stdin.readline

EMPTY = 0
WALL = 6
top = (-1, 0)
bottom = (1, 0)
right = (0, 1)
left = (0, -1)
cctv1 = (right, bottom, left, top)
cctv2 = ((left, right), (top, bottom))
cctv3 = ((top, right), (right, bottom), (bottom, left), (left, top))
cctv4 = ((left, top, right), (top, right, bottom), (right, bottom, left), (bottom, left, top))
cctv5 = ((top, bottom, right, left),)
cctv_table = {1: cctv1, 2: cctv2, 3: cctv3, 4: cctv4, 5: cctv5}

def make_case(cctvs, path, depth):
    if depth == len(cctvs):
        cases.append(path)
        return
    for case in cctv_table[cctvs[depth]]:
        make_case(cctvs, path + [case], depth + 1)

n, m = map(int, input().split())
board = []
cctvs = []
seen = []
for r in range(n):
    line = list(map(int, input().split()))
    for c in range(m):
        if line[c] in range(1, 6):
            cctvs.append((r, c))
            seen.append(line[c])
    board.append(line)
cases = []
answer = sys.maxsize
make_case(seen, [], 0)
for case in cases:
    temp = deepcopy(board)
    for i in range(len(cctvs)):
        if seen[i] != 1:
            for oper in case[i]:
                r = cctvs[i][0]
                c = cctvs[i][1]
                while True:
                    dr = r + oper[0]
                    dc = c + oper[1]
                    if 0 <= dr < n and 0 <= dc < m:
                        if temp[dr][dc] == WALL:
                            break
                        elif temp[dr][dc] == EMPTY:
                            temp[dr][dc] = '#'
                        r = dr
                        c = dc
                    else:
                        break
        else:
            r = cctvs[i][0]
            c = cctvs[i][1]
            while True:
                dr = r + case[i][0]
                dc = c + case[i][1]
                if 0 <= dr < n and 0 <= dc < m:
                    if temp[dr][dc] == WALL:
                        break
                    elif temp[dr][dc] == EMPTY:
                        temp[dr][dc] = '#'
                    r = dr
                    c = dc
                else:
                    break
    count = 0
    for r in range(n):
        for c in range(m):
            if temp[r][c] == EMPTY:
                count += 1
    answer = min(answer, count)
print(answer)