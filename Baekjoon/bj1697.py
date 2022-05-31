'''
Created by sunwoong on 2022/05/31
'''
import sys
import collections

n, k = map(int, sys.stdin.readline().split())

def bfs(start: int) -> int:
    visited = [False for _ in range(100001)]
    visited[start] = True
    queue = collections.deque([(start, 0)])
    while queue:
        curr_pos, time = queue.popleft()
        if curr_pos == k:
            break
        for next_pos in [curr_pos - 1, curr_pos + 1, curr_pos * 2]:
            if next_pos >= 0 and next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                queue.append((next_pos, time + 1))
    return time
print(bfs(n))