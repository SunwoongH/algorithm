'''
Created by sunwoong on 2023/03/10
'''
import sys
from collections import deque
input = sys.stdin.readline

def labeling(r, c, label):
    queue = deque([(r, c)])
    positions.append((r, c, label))
    board[r][c] = label
    count = 1
    while queue:
        r, c = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < m and board[dr][dc] == 1:
                count += 1
                board[dr][dc] = label
                queue.append((dr, dc))
                positions.append((dr, dc, label))
    return count

def extend(positions):
    queue = deque(positions)
    while queue:
        r, c, label = queue.popleft()
        for oper in move:
            dr = r + oper[0]
            dc = c + oper[1]
            if 0 <= dr < n and 0 <= dc < m and not board[dr][dc]:
                visited[dr][dc].add(label)

def find_maximum_size():
    maximum_size = 0
    for r in range(n):
        for c in range(m):
            if not visited[r][c]:
                continue
            size = 0
            for label in visited[r][c]:
                size += labels[label]
            maximum_size = max(maximum_size, size)
    return maximum_size

n, m = map(int, input().split())
move = [(1, 0), (0, 1), (-1, 0), (0, -1)]
board = [list(map(int, input().split())) for _ in range(n)]
visited = [[set() for _ in range(m)] for _ in range(n)]
label = 2
labels = dict()
positions = []
for r in range(n):
    for c in range(m):
        if board[r][c] == 1:
            count = labeling(r, c, label)
            labels[label] = count
            label += 1
extend(positions)
print(find_maximum_size() + 1)