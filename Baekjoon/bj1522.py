'''
Created by sunwoong on 2024/02/05
'''
import sys
input = sys.stdin.readline

data = input().rstrip()
count = 0
answer = sys.maxsize
for i in range(len(data)):
    if data[i] == 'a':
        count += 1
for i in range(len(data)):
    if i + count < len(data):
        temp = data[i:i + count]
    else:
        temp = data[i:] + data[:i + count - len(data)]
    temp_count = 0
    for c in temp:
        if c == 'b':
            temp_count += 1
    if answer > temp_count:
        answer = temp_count
print(answer)