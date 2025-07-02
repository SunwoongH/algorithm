'''
Created by sunwoong on 2025/07/02
'''
from itertools import product
import heapq

def solution(k, n, reqs):
    answer = int(1e9)
    reqs.sort(key=lambda x: (x[2], x[0], x[0] + x[1]))

    for case in product(range(n + 1), repeat=k):
        if sum(case) != n:
            continue
        if not all(case):
            continue
        waiting = 0
        queue = [[] for _ in range(k)]
        for i in range(len(reqs)):
            task = reqs[i]
            pos = task[2] - 1
            if len(queue[pos]) < case[pos]:
                heapq.heappush(queue[pos], task[0] + task[1])
            else:
                finished_task = heapq.heappop(queue[pos])
                time = finished_task - task[0]
                if time > 0:
                    waiting += time
                    heapq.heappush(queue[pos], task[0] + task[1] + time)
                else:
                    heapq.heappush(queue[pos], task[0] + task[1])
        answer = min(answer, waiting)
    
    return answer