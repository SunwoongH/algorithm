'''
Created by sunwoong 2022/05/06
'''
import sys

data = list(sys.stdin.readline().rstrip())
seen = set()
for window in range(1, len(data) + 1):
    for i in range(0, len(data) - window + 1):
        seen.add(''.join(data[i:window + i]))
print(len(seen))