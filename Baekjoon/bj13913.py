'''
Created by sunwoong on 2023/02/01
'''
import sys
from collections import deque
input = sys.stdin.readline

SIZE = 100001

def bfs(start, end):
    queue = deque([start])
    visited[start][0] = 1
    visited[start][1] = -1
    while queue:
        pos = queue.popleft()
        if pos == end:
            return
        if pos * 2 < SIZE and not visited[pos * 2][0]:
            visited[pos * 2][0] = visited[pos][0] + 1
            visited[pos * 2][1] = pos
            queue.append(pos * 2)
        if pos + 1 < SIZE and not visited[pos + 1][0]:
            visited[pos + 1][0] = visited[pos][0] + 1
            visited[pos + 1][1] = pos
            queue.append(pos + 1)
        if pos - 1 >= 0 and not visited[pos - 1][0]:
            visited[pos - 1][0] = visited[pos][0] + 1
            visited[pos - 1][1] = pos
            queue.append(pos - 1)

def find_path():
    i = k
    path = [i]
    while visited[i][1] != -1:
        path.append(visited[i][1])
        i = visited[i][1]
    path.reverse()
    return path

n, k = map(int, input().split())
visited = [[0, 0] for _ in range(SIZE)]
bfs(n, k)
print(visited[k][0] - 1)
print(*find_path())