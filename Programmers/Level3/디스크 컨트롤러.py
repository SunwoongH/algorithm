'''
Created by sunwoong on 2022/10/10
'''
import heapq

def solution(jobs):
    time = 0
    scheduler = []
    count = len(jobs)
    for point, task in jobs:
        heapq.heappush(scheduler, (task, point))
    wait = 0
    while scheduler:
        is_dispatch = False
        temp = []
        while not is_dispatch and scheduler:
            task, point = heapq.heappop(scheduler)
            if point <= time:
                time += task
                wait += time - point
                is_dispatch = True
            else:
                temp.append((task, point))
        if not is_dispatch:
            temp.sort(key=lambda x: (-x[1], -x[0]))
            task, point = temp.pop()
            time += point - time + task
            wait += time - point
        for job in temp:
            heapq.heappush(scheduler, job)
    return wait // count