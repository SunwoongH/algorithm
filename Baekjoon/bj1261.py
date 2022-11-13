'''
Created by sunwoong on 2022/11/13
'''
import sys
import heapq

def bfs(start_r: int, start_c: int, end_r: int, end_c: int) -> int:
    heap = [(0, start_r, start_c)]
    visited = [[sys.maxsize for _ in range(m)] for _ in range(n)]
    visited[start_r][start_c] = 0
    while heap:
        count, r, c = heapq.heappop(heap)
        if r == end_r and c == end_c:
            return visited[r][c]
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < m and visited[dr][dc] == sys.maxsize:
                visited[dr][dc] = count + maze[dr][dc]
                heapq.heappush(heap, (visited[dr][dc], dr, dc))

m, n = map(int, sys.stdin.readline().split())
maze = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n)]
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
print(bfs(0, 0, n - 1, m - 1))