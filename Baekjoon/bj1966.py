import sys
from collections import deque

n = int(sys.stdin.readline())

for i in range(n):
    num, index = map(int, sys.stdin.readline().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    maxV = max(queue)
    printV = 0
    while True:
        value = queue.popleft()
        if maxV != value:
            queue.append(value)
            index = (index - 1) % num
        elif index == 0:
            printV += 1
            break
        else:
            printV += 1
            num -= 1
            index = (index - 1) % num
            maxV = max(queue)
    print(printV)