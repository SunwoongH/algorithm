'''
Created by sunwoong on 2022/07/22
'''
import sys
import collections

n, x = map(int, sys.stdin.readline().split())
visited = list(map(int, sys.stdin.readline().split()))
result = 0
count = 1
target = 0
queue = collections.deque()
for i in range(len(visited)):
    if len(queue) < x - 1:
        target += visited[i]
        queue.append(visited[i])
    else:
        if len(queue) >= x:
            target -= queue.popleft()
        target += visited[i]
        queue.append(visited[i])
        if target > result:
            count = 1
            result = target
        elif target == result:
            count += 1
print("SAD") if not result else print(result, count, sep='\n')