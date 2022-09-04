'''
Created by sunwoong on 2022/09/04
'''
import sys

n = int(sys.stdin.readline())
if n == 1 or n == 3:
    print(-1)
elif n % 5 == 0:
    print(n // 5)
elif n % 5 % 2 == 0:
    count = n // 5
    n %= 5
    print(count + n // 2)
else:
    count = n // 5 - 1
    n -= (n // 5 - 1) * 5
    print(count + n // 2)