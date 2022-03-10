'''
Created by sunwoong on 2022/03/10
'''
import sys
data = list(sys.stdin.readline().rstrip('\n'))
result = 0
stack = []
for i in range(len(data)):
    if data[i] == '(':
        stack.append(i)
    else:
        j = stack.pop()
        if i - j == 1:
            result += len(stack)
        else:
            result += 1
print(result)