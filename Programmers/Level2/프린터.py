'''
Created by sunwoong on 2022/10/15
'''
from collections import deque

def solution(priorities, location):
    priorities = deque(priorities)
    count = 0
    while priorities:
        target = priorities.popleft()
        is_possible = True
        for priority in priorities:
            if target < priority:
                is_possible = False
                break
        if not is_possible:
            priorities.append(target)
        else:
            count += 1
            if location == 0:
                return count
        location = (location - 1 + len(priorities)) % len(priorities)