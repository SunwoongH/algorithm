'''
Created by sunwoong on 2022/08/05
'''
import sys

n, m = map(int, sys.stdin.readline().split())
interval = list(map(int, sys.stdin.readline().split()))
if sum(interval) >= m:
    for i in range(1, n):
        interval[i] += interval[i - 1]
    is_finish = False
    for i in range(n):
        if interval[i] > m:
            print(i + 1)
            is_finish = True
            break
    if not is_finish:
        print(n)
else:
    interval.reverse()
    for i in range(1, n):
        interval[i] += interval[i - 1]
    is_finish = False
    for i in range(n):
        if interval[i] > m - interval[-1]:
            print(n - i)
            is_finish = True
            break
    if not is_finish:
        print(1)