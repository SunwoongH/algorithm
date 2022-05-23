'''
Created by sunwoong on 2022/05/23
'''
from typing import List
import sys
import collections
from copy import deepcopy

n, m = map(int, sys.stdin.readline().split())
graph = []
empty = []
viruses = []
move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
result = -sys.maxsize

for r in range(n):
    data = list(map(int, sys.stdin.readline().split()))
    graph.append(data[:])
    for c in range(m):
        if data[c] == 0:
            empty.append([r, c])
        elif data[c] == 2:
            viruses.append([r, c])

def bfs(board: List[int]) -> None:
    global result
    count = 0
    queue = collections.deque()
    for virus in viruses:
        queue.append(virus)
    while queue:
        r, c = queue.popleft()
        for operation in move:
            dr = r + operation[0]
            dc = c + operation[1]
            if dr >= 0 and dr < n and dc >= 0 and dc < m and board[dr][dc] == 0:
                board[dr][dc] = 2
                queue.append([dr, dc])
    for r in range(n):
        for c in range(m):
            if board[r][c] == 0:
                count += 1
    result = max(result, count)
    
for i in range(len(empty)):
    for j in range(i + 1, len(empty)):
        for k in range(j + 1, len(empty)):
            graph[empty[i][0]][empty[i][1]] = 1
            graph[empty[j][0]][empty[j][1]] = 1
            graph[empty[k][0]][empty[k][1]] = 1
            board = deepcopy(graph)
            bfs(board)
            graph[empty[i][0]][empty[i][1]] = 0
            graph[empty[j][0]][empty[j][1]] = 0
            graph[empty[k][0]][empty[k][1]] = 0
print(result)