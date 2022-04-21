'''
Created by sunwoong on 2022/04/21
'''
import sys

bracket = list(sys.stdin.readline().rstrip())

stack, flag = [], False
for i in range(len(bracket)):
    if bracket[i] in '([':
        stack.append(bracket[i])
    elif bracket[i] == ')':
        if '(' not in stack:
            flag = True
            break
        temp = 0
        while stack[-1] != '(':
            if stack[-1] == '[':
                flag = True
                break
            temp += stack.pop()
        if flag:
            break
        stack.pop()
        stack.append(2 if temp == 0 else temp * 2)
    else:
        if '[' not in stack:
            flag = True
            break
        temp = 0
        while stack[-1] != '[':
            if stack[-1] == '(':
                flag = True
                break
            temp += stack.pop()
        if flag:
            break
        stack.pop()
        stack.append(3 if temp == 0 else temp * 3)
print(sum(stack) if not flag and '(' not in stack and '[' not in stack else 0)