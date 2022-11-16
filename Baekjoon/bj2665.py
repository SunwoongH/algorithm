'''
Created by sunwoong on 2022/11/16
'''
import sys
import heapq

def bfs(start_r, start_c, end_r, end_c):
    heap = [(0, start_r, start_c)]
    visited = [[sys.maxsize for _ in range(n)] for _ in range(n)]
    visited[start_r][start_c] = 0
    while heap:
        count, r, c = heapq.heappop(heap)
        if r == end_r and c == end_c:
            return visited[end_r][end_c]
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < n and visited[dr][dc] == sys.maxsize:
                visited[dr][dc] = (1 if board[dr][dc] == 0 else 0) + count
                heapq.heappush(heap, (visited[dr][dc], dr, dc))
        
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
n = int(sys.stdin.readline())
board = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
print(bfs(0, 0, n - 1, n - 1))