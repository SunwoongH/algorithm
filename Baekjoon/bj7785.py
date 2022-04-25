'''
Created by sunwoong on 2022/04/25
'''
import sys

n = int(sys.stdin.readline())
log = dict()
for _ in range(n):
    name, state = sys.stdin.readline().split()
    log[name] = state
print(*sorted([name for name, state in log.items() if state == 'enter'], reverse=True), sep='\n')