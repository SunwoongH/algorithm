'''
Created by sunwoong on 2022/04/17
'''
import sys
import collections

n = int(sys.stdin.readline())
balloon, order = collections.deque(zip(list(map(int, sys.stdin.readline().split())), range(1, n + 1))), []
while balloon:
    jump = balloon.popleft()
    balloon.rotate(-(jump[0] - 1 if jump[0] > 0 else jump[0]))
    order.append(jump[1])
print(*order)