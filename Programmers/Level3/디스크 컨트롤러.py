'''
Created by sunwoong on 2024/05/14

풀이 시간 - 60분
'''
import heapq

def solution(jobs):
    jobs.sort(key=lambda x: -x[0])
    size = len(jobs)
    waiting_time = 0
    waiting = []
    start = 0
    while True:
        while jobs and jobs[-1][0] <= start:
            job = jobs.pop()
            heapq.heappush(waiting, (job[1], job[0]))
        if not waiting:
            if not jobs:
                break
            job = jobs.pop()
            heapq.heappush(waiting, (job[1], job[0]))
        time, origin = heapq.heappop(waiting)
        if origin > start:
            start = origin
            waiting_time += time
        else:
            waiting_time += time + start - origin
        start += time
    return int(waiting_time / size)