'''
Created by sunwoong on 2022/11/12
'''
import sys
from collections import deque

SIZE = 100001

def bfs(start: int, end: int) -> int:
    queue = deque([(start, 0)])
    visited = [False for _ in range(SIZE)]
    time_table = [False for _ in range(SIZE)]
    visited[start] = True
    time_table[start] = 0
    is_find = False
    optimize_time = None
    count = 0
    while queue:
        pos, time = queue.popleft()
        if pos == end:
            if not is_find:
                is_find = True
                optimize_time = time
                count += 1
            else:
                if time == optimize_time:
                    count += 1
                else:
                    break
        for next_pos in [pos -1, pos + 1, pos * 2]:
            if 0 <= next_pos < SIZE and (not visited[next_pos] or time_table[next_pos] == time):
                if not visited[next_pos]:
                    visited[next_pos] = True
                if not time_table[next_pos]:
                    time_table[next_pos] = time
                queue.append((next_pos, time + 1))
    return optimize_time, count

n, k = map(int, sys.stdin.readline().split())
print(*bfs(n, k), sep='\n')