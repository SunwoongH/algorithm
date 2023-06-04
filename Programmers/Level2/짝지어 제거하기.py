'''
Created by sunwoong on 2023/06/04
'''
from collections import deque

def solution(s):
    left = deque()
    right = deque(s)
    while right:
        while left and right and left[-1] == right[0]:
            left.pop()
            right.popleft()
        if right:
            left.append(right.popleft())
    return 1 if not left and not right else 0