'''
Created by sunwoong on 2025/09/24
'''
import sys

s = sys.stdin.readline().rstrip()
stack = []

for i in range(len(s)):
    if s[i].isdigit() or s[i] == '(':
        stack.append((s[i], True))
    else:
        num = 0
        while stack and stack[-1][0] != '(':
            temp, is_origin = stack.pop()
            if is_origin:
                num += 1
            else:
                num += temp
        stack.pop()
        count = int(stack.pop()[0])
        stack.append((count * num, False))

answer = 0
for temp, is_origin in stack:
    if is_origin:
        answer += 1
    else:
        answer += temp
print(answer)