'''
Created by sunwoong on 2024/07/09
'''
import heapq

def solution(program):
    answer = [0 for _ in range(11)]
    waiting = []
    init = []
    for data in program:
        heapq.heappush(init, ((data[1], data[0]), data))
    start = None
    while waiting or init:
        if not waiting:
            _, data = heapq.heappop(init)
            if not start or start < data[1]:
                start = data[1] + data[2]
            else:
                answer[data[0]] += start - data[1]
                start += data[2]
        else:
            _, data = heapq.heappop(waiting)
            if not start or start < data[1]:
                start = data[1] + data[2]
            else:
                answer[data[0]] += start - data[1]
                start += data[2]
        while init:
            _, data = heapq.heappop(init)
            if data[1] <= start:
                heapq.heappush(waiting, ((data[0], data[1]), data))
            else:
                heapq.heappush(init, ((data[1], data[0]), data))
                break
    answer[0] = start
    return answer