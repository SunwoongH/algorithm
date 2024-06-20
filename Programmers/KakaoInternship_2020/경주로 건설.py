'''
Created by sunwoong on 2024/06/20

풀이 시간 - 180분
'''

from collections import deque
import sys

move = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}

def bfs(board):
    costs = [[[sys.maxsize for _ in range(len(board))] for _ in range(len(board))] for _ in range(4)]
    for i in range(4):
        costs[i][0][0] = 0
    queue = deque([(None, 0, 0, 0)])
    while queue:
        prev, r, c, cost = queue.popleft()
        for d in move.keys():
            dr = r + move[d][0]
            dc = c + move[d][1]
            if 0 <= dr < len(board) and 0 <= dc < len(board) and board[dr][dc] == 0:
                if not prev or prev == move[d]:
                    if costs[d][dr][dc] > cost + 100:
                        costs[d][dr][dc] = cost + 100
                        queue.append((move[d], dr, dc, costs[d][dr][dc]))
                else:
                    if costs[d][dr][dc] > cost + 600:
                        costs[d][dr][dc] = cost + 600
                        queue.append((move[d], dr, dc, costs[d][dr][dc]))
    minimum_cost = sys.maxsize
    for i in range(4):
        minimum_cost = min(minimum_cost, costs[i][len(board) - 1][len(board) - 1])
    return minimum_cost

def solution(board):
    return bfs(board)