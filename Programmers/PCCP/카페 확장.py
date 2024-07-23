'''
Created by sunwoong on 2024/07/23
'''
from collections import deque

def solution(menu, order, k):
    time = -1
    i = answer = 0
    queue = deque()
    
    for t in range(k * (len(order) - 1) + 1):
        if time == t:
            queue.popleft()
            time = -1
        if i * k == t:
            queue.append(order[i])
            i += 1
        if time == -1 and queue:
            time = t + menu[queue[0]]
        answer = max(answer, len(queue))
    return answer        