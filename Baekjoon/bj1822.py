'''
Created by sunwoong on 2022/07/08
'''
import sys

n, m = map(int, sys.stdin.readline().split())
a = set(list(sys.stdin.readline().split()))
b = set(list(sys.stdin.readline().split()))
if len(a - b) == 0:
    print(len(a - b))
else:
    print(len(a - b))
    print(*sorted(list(map(int, a - b))))