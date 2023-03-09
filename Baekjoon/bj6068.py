'''
Created by sunwoong on 2023/03/09
'''
import sys
input = sys.stdin.readline

n = int(input())
tasks = []
for _ in range(n):
    time, end = map(int, input().split())
    tasks.append((time, end))
tasks.sort(key=lambda x: x[1], reverse=True)
start = tasks[0][1] - tasks[0][0]
for i in range(1, n):
    time, end = tasks[i]
    if end < start:
        start = end - time
    else:
        start -= time
print(-1) if start < 0 else print(start)