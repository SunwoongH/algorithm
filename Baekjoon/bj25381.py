'''
Created by sunwoong on 2025/09/11
'''
import sys
from collections import deque

s = sys.stdin.readline().rstrip()
a = deque()
b = deque()
ban = set()

for i in range(len(s)):
    if s[i] == 'A':
        a.append(i)
    if s[i] == 'B':
        b.append(i)

for i in range(len(s)):
    if s[i] == 'C' and len(b) > 0 and b[0] < i:
        pos = b.popleft()
        ban.add(pos)

for i in b:
    if len(a) > 0 and a[0] < i:
        a.popleft()
        ban.add(i)

print(len(ban))