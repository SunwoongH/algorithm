'''
Created by sunwoong on 2022/05/25
'''
import sys
import collections

n = int(sys.stdin.readline())
table = collections.defaultdict(int)
for _ in range(n):
    _, extension = map(str, sys.stdin.readline().rstrip().split('.'))
    table[extension] += 1
result = sorted(table.items(), key=lambda x: x[0])
for item in result:
    print(*item)