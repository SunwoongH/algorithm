'''
Created by sunwoong on 2022/11/15
'''
import sys

origin = list(sys.stdin.readline().rstrip())
after = list(sys.stdin.readline().rstrip())
while len(after) > len(origin):
    last = after.pop()
    if last == 'B':
        after = after[::-1]
print(1) if ''.join(origin) == ''.join(after) else print(0)