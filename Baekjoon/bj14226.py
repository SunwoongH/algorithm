'''
Created by sunwoong on 2023/02/07
'''
import sys
from collections import deque
input = sys.stdin.readline

SIZE = 1000
visited = [[0 for _ in range(SIZE + 1)] for _ in range(SIZE + 1)]
s = int(input())

def bfs(target):
    queue = deque([(1, 0)])
    while queue:
        screen, clipboard = queue.popleft()
        if target == screen:
            print(visited[screen][clipboard])
            return
        if not visited[screen][screen]:
            visited[screen][screen] = 1 + visited[screen][clipboard]
            queue.append((screen, screen))
        if clipboard != 0 and screen + clipboard <= SIZE and not visited[screen + clipboard][clipboard]:
            visited[screen + clipboard][clipboard] = 1 + visited[screen][clipboard]
            queue.append((screen + clipboard, clipboard))
        if screen - 1 >= 0 and not visited[screen - 1][clipboard]:
            visited[screen - 1][clipboard] = 1 + visited[screen][clipboard]
            queue.append((screen - 1, clipboard))
bfs(s)