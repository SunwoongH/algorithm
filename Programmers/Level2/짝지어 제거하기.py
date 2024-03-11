'''
Created by sunwoong on 2024/03/11

풀이 시간 - 30분
'''
def solution(s):
    stack = []
    for char in s:
        if stack:
            if stack[-1] == char:
                stack.pop()
                continue
        stack.append(char)
    return 1 if not stack else 0