'''
Created by sunwoong on 2022/07/18
'''
import sys
import collections

n = int(sys.stdin.readline())
friends = [list(sys.stdin.readline().rstrip()) for _ in range(n)]

def bfs(start: int) -> int:
    visited = [False] * n
    queue = collections.deque([(start, 0)])
    visited[start] = True
    count = -1
    while queue:
        curr, relationship = queue.popleft()
        count += 1
        for i in range(n):
            if friends[curr][i] == 'Y' and not visited[i]:
                visited[i] = True
                if relationship < 2:
                    queue.append((i, relationship + 1))
    return count
result = 0
for start in range(n):
    result = max(result, bfs(start))
print(result)