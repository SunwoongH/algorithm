'''
Created by sunwoong on 2023/02/25
'''
import sys
from collections import deque
input = sys.stdin.readline

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def labeling_by_bfs(start_r, start_c):
    global distance_visited
    distance_visited = [[False for _ in range(n)] for _ in range(n)]
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    distance_visited[start_r][start_c] = True
    pos = []
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n:
                if not board[dr][dc]:
                    if not distance_visited[dr][dc]:
                        distance_visited[dr][dc] = True
                        pos.append((dr, dc, 0))
                else:
                    if not visited[dr][dc]:
                        visited[dr][dc] = True
                        distance_visited[dr][dc] = True
                        queue.append((dr, dc))
    return pos
            
def distance_by_bfs(pos):
    queue = deque(pos)
    while queue:
        r, c, cost = queue.popleft()
        if board[r][c]:
            return cost
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n and not distance_visited[dr][dc]:
                distance_visited[dr][dc] = True
                queue.append((dr, dc, cost + 1))

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
distance_visited = None
total = sys.maxsize
for r in range(n):
    for c in range(n):
        if not visited[r][c] and board[r][c]:
            total = min(total, distance_by_bfs(labeling_by_bfs(r, c)))
print(total)