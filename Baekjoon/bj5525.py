'''
Created by sunwoong on 2022/07/29
'''
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
data = sys.stdin.readline().rstrip()
i = 0
result = 0
count = 0
while i < m - 2:
    if data[i:i + 3] == 'IOI':
        count += 1
        if count == n:
            result += 1
            count -= 1
        i += 2
    else:
        count = 0
        i += 1
print(result)