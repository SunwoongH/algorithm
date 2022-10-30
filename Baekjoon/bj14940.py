'''
Created by sunwoong on 2022/10/30
'''
import sys
import heapq

def dijkstra(start_r, start_c):
    distance[start_r][start_c] = 0
    heap = [(0, start_r, start_c)]
    while heap:
        cost, r, c = heapq.heappop(heap)
        if distance[r][c] < cost:
            continue
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < m and board[dr][dc]:
                if distance[dr][dc] > distance[r][c] + board[dr][dc]:
                    distance[dr][dc] = distance[r][c] + board[dr][dc]
                    heapq.heappush(heap, (distance[dr][dc], dr, dc))

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
distance = [[sys.maxsize for _ in range(m)] for _ in range(n)]
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
start = None
unable = set()
for r in range(n):
    for c in range(m):
        if board[r][c] == 2:
            start = (r, c)
        elif not board[r][c]:
            unable.add((r, c))
dijkstra(start[0], start[1])
for r in range(n):
    for c in range(m):
        if not distance[r][c] or (r, c) in unable:
            print(0, end=' ')
        elif distance[r][c] == sys.maxsize:
            print(-1, end=' ')
        else:
            print(distance[r][c], end=' ')
    print()