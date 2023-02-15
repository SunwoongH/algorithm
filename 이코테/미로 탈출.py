'''
Created by sunwoong on 2023/02/15
'''
import sys
from collections import deque
input = sys.stdin.readline

PROMISING = '1'
MONSTER = '0'
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]

def bfs(start_r, start_c, end_r, end_c):
    queue = deque([(start_r, start_c)])
    distance[start_r][start_c] = 1
    while queue:
        r, c = queue.popleft()
        if r == end_r and c == end_c:
            return distance[r][c]
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < m and not distance[dr][dc] and board[dr][dc] == PROMISING:
                distance[dr][dc] = distance[r][c] + 1
                queue.append((dr, dc))

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
distance = [[0 for _ in range(m)] for _ in range(n)]
print(bfs(0, 0, n - 1, m - 1))