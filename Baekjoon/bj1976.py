'''
Created by sunwoong on 2022/12/11
'''
import sys
from collections import deque
input = sys.stdin.readline

def bfs(start, end):
    queue = deque([start])
    visited = [False for _ in range(n)]
    visited[start] = True
    while queue:
        curr = queue.popleft()
        if curr == end:
            return True
        for next in range(n):
            if graph[curr][next] and not visited[next]:
                visited[next] = True
                queue.append(next)
    return False

n = int(input())
m = int(input())
graph = []
for _ in range(n):
    line = list(map(int, input().split()))
    graph.append(line)
sequence = list(map(int, input().split()))
is_promising = True
for i in range(len(sequence) - 1):
    is_promising = bfs(sequence[i] - 1, sequence[i + 1] - 1)
    if not is_promising:
        break
print("YES") if is_promising else print("NO")