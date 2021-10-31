import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
order = list(map(int, sys.stdin.readline().split()))
queue = deque([i for i in range(1, n + 1)])

count = 0
mid = len(queue) // 2
for o in order:
    check = False
    while not check:
        if queue.index(o) == 0:
            queue.popleft()
            mid = len(queue) // 2
            check = True
        if not check:
            if queue.index(o) <= mid:
                queue.append(queue.popleft())
            else: queue.appendleft(queue.pop())
            count += 1
print(count)