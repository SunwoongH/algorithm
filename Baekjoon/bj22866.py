'''
Created by sunwoong on 2025/08/31
'''
import sys

n = int(sys.stdin.readline())
heights = list(map(int, sys.stdin.readline().split()))
answer = [0 for _ in range(n)]
count = [0 for _ in range(n)]

stack = []
for i in range(n):
    if not stack:
        stack.append((i + 1, heights[i]))
        continue
    while stack and stack[-1][1] <= heights[i]:
        stack.pop()
    if stack:
        answer[i] = stack[-1][0]
        count[i] += len(stack)
    stack.append((i + 1, heights[i]))

stack = []
for i in range(n - 1, -1, -1):
    if not stack:
        stack.append((i + 1, heights[i]))
        continue
    while stack and stack[-1][1] <= heights[i]:
        stack.pop()
    if stack:
        if not answer[i]:
            answer[i] = stack[-1][0]
        else:
            if (i + 1) - answer[i] > stack[-1][0] - (i + 1):
                answer[i] = stack[-1][0]
        count[i] += len(stack)
    stack.append((i + 1, heights[i]))

for i in range(n):
    if count[i]:
        print(str(count[i]) + ' ' + str(answer[i]))
    else:
        print(count[i])
