'''
Created by sunwoong on 2022/04/16
'''
import sys

n = int(sys.stdin.readline())
formula = list(sys.stdin.readline().rstrip())
values, stack = [int(sys.stdin.readline()) for _ in range(n)], []
for i in range(len(formula)):
    if formula[i].isalpha():
        stack.append(values[ord(formula[i]) - ord('A')])
    else:
        curr, prev = stack.pop(), stack.pop()
        if formula[i] == '+':
            stack.append(prev + curr)
        elif formula[i] == '-':
            stack.append(prev - curr)
        elif formula[i] == '*':
            stack.append(prev * curr)
        else:
            stack.append(prev / curr)
print("%.2f" %float(stack[-1]))