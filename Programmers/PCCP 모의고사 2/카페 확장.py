'''
Created by sunwoong on 2025/05/08
'''
from collections import deque

def solution(menu, order, k):
    order.reverse()
    item = order.pop()
    
    queue = deque([item])
    new_order = k
    end = 0
    answer = 0
    
    while order:
        task = queue.popleft()
        end = end + menu[task]
        while order and new_order < end:
            item = order.pop()
            queue.append(item)
            new_order += k
        answer = max(answer, len(queue) + 1)
        
        if not queue:
            item = order.pop()
            queue.append(item)
            end = new_order
            new_order += k

    return answer