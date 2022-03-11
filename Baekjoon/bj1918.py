'''
Created by sunwoong on 2022/03/11
'''
import sys

expression = list(sys.stdin.readline().rstrip('\n'))
stack = []
result = []
for char in expression:
    if char.isalpha():
        result.append(char)
    elif char == '(':
        stack.append(char)
    elif char in '+-*/':
        if not result:
            stack.append(char)
        else:
            if char in '+-':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.append(char)
            else:
                while stack and stack[-1] in '*/':
                    result.append(stack.pop())
                stack.append(char)
    else:
        while stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
while stack:
    result.append(stack.pop())
print(''.join(result))