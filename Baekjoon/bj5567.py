'''
Created by sunwoong on 2022/05/26
'''
import collections
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
friend = collections.defaultdict(list)
for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    friend[u].append(v)
    friend[v].append(u)
    
def bfs(start: int) -> int:
    result = -1
    visited = [False for _ in range(n + 1)]
    visited[start] = True
    queue = collections.deque([(start, 0)])
    while queue:
        u, level = queue.popleft()
        if level > 2:
            break
        result += 1
        for v in friend[u]:
            if not visited[v]:
                visited[v] = True
                queue.append((v, level + 1))
    return result
print(bfs(1))