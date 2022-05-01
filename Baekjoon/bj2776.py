'''
Created by sunwoong on 2022/05/01
'''
import sys
import collections

test = int(sys.stdin.readline())
for _ in range(test):
    n = int(sys.stdin.readline())
    table = collections.defaultdict(bool)
    number1 = list(map(int, sys.stdin.readline().split()))
    for num in number1:
        table[num] = True
    m = int(sys.stdin.readline())
    number2 = list(map(int, sys.stdin.readline().split()))
    for num in number2:
        if table[num]:
            print(1)
        else:
            print(0)