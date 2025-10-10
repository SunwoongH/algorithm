'''
Created by sunwoong on 2025/10/10
'''
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

def bfs(start):
    visited = [False for _ in range(200000)]
    visited[start] = True

    queue = deque([(0, start)])
    while queue:
        time, node = queue.popleft()
        if node == k:
            print(time)
            return
        
        for cost, next_node in [(0, 2 * node), (1, node - 1), (1, node + 1)]:
            if 0 <= next_node < 200000 and not visited[next_node]:
                visited[next_node] = True
                if cost == 0:
                    queue.appendleft((time, next_node))
                else:
                    queue.append((time + cost, next_node))

bfs(n)