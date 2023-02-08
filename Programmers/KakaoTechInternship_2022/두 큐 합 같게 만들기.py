'''
Created by sunwoong on 2023/02/08

풀이 시간 - 72분
'''
from collections import deque

def solution(queue1, queue2):
    sum_of_queue1, sum_of_queue2 = sum(queue1), sum(queue2)
    left, right = 0, len(queue1) - 1
    queue = queue1 + queue2
    queue = list(zip(queue, [True if i == 0 or i == len(queue1) - 1 else False for i in range(len(queue1) * 2)]))
    count = 0
    while sum_of_queue1 != sum_of_queue2:
        if sum_of_queue1 > sum_of_queue2:
            sum_of_queue1 -= queue[left][0]
            sum_of_queue2 += queue[left][0]
            left = (left + 1) % (len(queue1) * 2)
        elif sum_of_queue1 < sum_of_queue2:
            right = (right + 1) % (len(queue1) * 2)
            sum_of_queue2 -= queue[right][0]
            sum_of_queue1 += queue[right][0]
        count += 1
        if queue[left][1] and queue[right][1]:
            count = -1
            break
    return count