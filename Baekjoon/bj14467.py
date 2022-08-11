'''
Created by sunwoong on 2022/08/11
'''
import sys

caw = dict()
n = int(sys.stdin.readline())
count = 0
for _ in range(n):
    num, flag = map(int, sys.stdin.readline().split())
    if num not in caw:
        caw[num] = flag
    elif caw[num] != flag:
        count += 1
        caw[num] = flag
print(count)