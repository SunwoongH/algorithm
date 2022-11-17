'''
Created by sunwoong on 2022/11/17
'''
import sys
from collections import defaultdict, deque

def bfs(curr):
    visited = [False for _ in range(n + 1)]
    queue = deque([(curr, 0)])
    visited[curr] = True
    while queue:
        curr, depth = queue.popleft()
        for next in friends[curr]:
            if not visited[next]:
                visited[next] = True
                queue.append((next, depth + 1))
    return depth
    
n = int(sys.stdin.readline())
user = []
optimize_score = sys.maxsize
friends = defaultdict(list)
while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break
    friends[a].append(b)
    friends[b].append(a)
for i in range(1, n + 1):
    depth = bfs(i)
    if optimize_score > depth:
        optimize_score = depth
        user.clear()
        user.append(i)
    elif optimize_score == depth:
        user.append(i)
print(optimize_score, len(user))
print(*user)