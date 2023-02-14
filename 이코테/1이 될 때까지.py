'''
Created by sunwoong on 2023/02/14
'''
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
count = 0
while True:
    target = (n // k) * k
    count += n - target
    n = target
    if n < k:
        count += n - 1
        break
    count += 1
    n //= k
print(count)