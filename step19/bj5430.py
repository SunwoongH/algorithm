import sys
from collections import deque

test = int(sys.stdin.readline())

for t in range(test):
    check = True
    order = list(sys.stdin.readline().strip('\n'))
    n = int(sys.stdin.readline())
    charaters = "[]\n,"
    inputNum = sys.stdin.readline().replace(',', ' ')
    strNum = inputNum.lstrip('[').rstrip(']\n')
    num = list(map(int, strNum.split()))
    queue = deque(num)
    
    isReverse = 1
    for i in range(len(order)):
        if order[i] == 'R':
            isReverse += 1
            continue
        elif isReverse % 2 == 0: 
            if len(queue) == 0:
                check = False
                break
            else: queue.pop()
        else: 
            if len(queue) == 0:
                check = False
                break
            else: queue.popleft()

    if check:
        print('[', end='')
        if isReverse % 2 == 0:
            for i in range(len(queue) - 1, -1, -1):
                if i == 0: print(queue[i], end='')
                else: print(str(queue[i]) + ',', end='')
        else:
            for i in range(len(queue)):
                if i == len(queue) - 1: print(queue[i], end='')
                else: print(str(queue[i]) + ',', end='')
        print(']')
    else: print('error')