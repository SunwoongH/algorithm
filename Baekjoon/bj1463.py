'''
Created by sunwoong on 2022/07/20
'''
import sys
import collections

n = int(sys.stdin.readline())

def bfs(start: int) -> int:
    visited = [False] * (n + 1)
    visited[start] = True
    queue = collections.deque([(start, 0)])
    while queue:
        num, count = queue.popleft()
        if num == 1:
            break
        if num % 3 == 0 and not visited[num // 3]:
            visited[num // 3] = True
            queue.append((num // 3, count + 1))
        if num % 2 == 0 and not visited[num // 2]:
            visited[num // 2] = True
            queue.append((num // 2, count + 1))
        if not visited[num - 1]:
            visited[num - 1] = True
            queue.append((num - 1, count + 1))
    return count
print(bfs(n))