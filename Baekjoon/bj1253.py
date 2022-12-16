'''
Created by sunwoong on 2022/12/16
'''
import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
table = defaultdict(int)
for i in range(n):
    table[sequence[i]] += 1
count = 0
for i in range(n):
    table[sequence[i]] -= 1
    is_check = False
    for j in range(n):
        if i == j:
            continue
        table[sequence[j]] -= 1
        if table[sequence[i] - sequence[j]]:
            count += 1
            is_check = True
        table[sequence[j]] += 1
        if is_check:
            break
    table[sequence[i]] += 1
print(count)