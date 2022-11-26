'''
Created by sunwoong on 2022/11/26
'''

def solution(s):
    stack = []
    for char in s:
        if char == '(':
            stack.append(char)
        else:
            if stack:
                stack.pop()
            else:
                return False
    if stack:
        return False
    return True