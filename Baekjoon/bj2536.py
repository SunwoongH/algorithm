'''
Created by sunwoong on 2025/04/25
'''
from collections import deque
import sys

def is_cross(a, b):
    _, x1, y1, x2, y2 = a
    _, x3, y3, x4, y4 = b
    return max(x1, x2) >= min(x3, x4) and max(x3, x4) >= min(x1, x2) \
        and max(y1, y2) >= min(y3, y4) and max(y3, y4) >= min(y1, y2)

m, n = map(int, sys.stdin.readline().split())
k = int(sys.stdin.readline())
lines = []
for _ in range(k):
    bus = list(map(int, sys.stdin.readline().split()))
    lines.append(bus)
sx, sy, dx, dy = map(int, sys.stdin.readline().split())

lines.sort(key=lambda x: x[0])

destination = set()

queue = deque()
visited = [False for _ in range(k + 1)]

start = [0, sx, sy, sx, sy]
end = [0, dx, dy, dx, dy]

for i in range(k):
    if is_cross(start, lines[i]):
        visited[i] = True
        queue.append((i, 1))
    if is_cross(end, lines[i]):
        destination.add(i)

while queue:
    bus, count = queue.popleft()
    if bus in destination:
        print(count)
        break
    for next_bus in range(k):
        if not visited[next_bus] and is_cross(lines[bus], lines[next_bus]):
            visited[next_bus] = True
            queue.append((next_bus, count + 1))