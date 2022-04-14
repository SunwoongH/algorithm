'''
Created by sunwoong on 2022/04/14
'''
import sys
import collections

n, k = map(int, sys.stdin.readline().split())
queue, result = collections.deque(range(1, n + 1)), []
while queue:
    queue.rotate(-(k - 1))
    result.append(queue.popleft())
print('<' + ', '.join(map(str, result)) + '>')