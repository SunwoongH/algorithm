'''
Created by sunwoong on 2022/11/28
'''

import heapq

def solution(n, works):
    works = list(map(lambda x: -x, works))
    heapq.heapify(works)
    while n > 0:
        task = heapq.heappop(works)
        if task < 0:
            heapq.heappush(works, task + 1)
        else:
            break
        n -= 1
    return sum(map(lambda x: pow(x, 2), works))