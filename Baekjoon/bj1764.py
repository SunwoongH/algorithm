'''
Created by sunwoong on 2022/04/18
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
table, result = collections.defaultdict(int), []
for _ in range(n + m):
    table[sys.stdin.readline().rstrip()] += 1
result = sorted([name for name in table if table[name] == 2])
print(len(result))
print(*result, sep='\n')