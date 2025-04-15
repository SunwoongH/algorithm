'''
Created by sunwoong on 2025/04/15
'''
from collections import deque

def solution(s):
    answer = []
    target = '110'
    
    for line in s:
        stack = []
        line = deque(line)
        count = 0
        while line:
            item = line.popleft()
            stack.append(item)
            if len(stack) > 2:
                if ''.join(stack[len(stack) - 3:]) == target:
                    for _ in range(len(target)):
                        stack.pop()
                    count += 1
        pos = -1
        for i in range(len(stack) - 1, -1, -1):
            if stack[i] == '0':
                pos = i
                break
        line = ''.join(stack[:pos + 1]) + '110' * count + ''.join(stack[pos + 1:])
        answer.append(line)
        
    return answer