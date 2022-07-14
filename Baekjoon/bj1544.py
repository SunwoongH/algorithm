'''
Created by sunwoong on 2022/07/14
'''
import sys
import collections

n = int(sys.stdin.readline())
table = collections.defaultdict(int)
for _ in range(n):
    word = collections.deque(list(sys.stdin.readline().rstrip()))
    is_seen = False
    for _ in range(len(word)):
        word.rotate(-1)
        if ''.join(word) in table:
            is_seen = True
            table[''.join(word)] += 1
            break
    if not is_seen:
        table[''.join(word)] += 1
print(len(table.keys()))