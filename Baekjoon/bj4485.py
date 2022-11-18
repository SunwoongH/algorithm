'''
Created by sunwoong on 2022/11/18
'''
import sys
import heapq

def bfs(start_r, start_c, end_r, end_c):
    heap = [(board[start_r][start_c], start_r, start_c)]
    distance = [[-1 for _ in range(n)] for _ in range(n)]
    distance[start_r][start_c] = board[start_r][start_c]
    while heap:
        cost, r, c = heapq.heappop(heap)
        if r == end_r and c == end_c:
            return distance[end_r][end_c]
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n and distance[dr][dc] == -1:
                distance[dr][dc] = cost + board[dr][dc]
                heapq.heappush(heap, (distance[dr][dc], dr, dc))

move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
i = 1
while True:
    n = int(sys.stdin.readline())
    if not n:
        break
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    print(f'Problem {i}: {bfs(0, 0, n - 1, n - 1)}')
    i += 1