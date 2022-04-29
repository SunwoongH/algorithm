'''
Created by sunwoong on 2022/04/29
'''
import sys

bracket = list(sys.stdin.readline().rstrip())
stack = []
result = 0
for char in bracket:
    if char == '(':
        stack.append(char)
    elif char == ')':
        if not stack:
            result += 1
        else:
            stack.pop()
print(result + len(stack))