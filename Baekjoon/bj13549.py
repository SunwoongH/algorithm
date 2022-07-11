'''
Created by sunwoong on 2022/07/11
'''
import sys
import collections

n, k = map(int, sys.stdin.readline().split())

def bfs(start: int, end: int) -> int:
    visited = [False for _ in range(100001)]
    queue = collections.deque([(start, 0)])
    while queue:
        curr_pos, time = queue.popleft()
        if curr_pos == end:
            return time
        for next_pos, weight in [(curr_pos * 2, 0), (curr_pos - 1, 1), (curr_pos + 1, 1)]:
            if next_pos >= 0 and next_pos <= 100000 and not visited[next_pos]:
                visited[next_pos] = True
                if weight == 0:
                    queue.appendleft((next_pos, time))
                else:
                    queue.append((next_pos, time + weight))
print(bfs(n, k))