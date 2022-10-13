'''
Created by sunwoong on 2022/10/13
'''
from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []
    while progresses:
        count = 1
        job = progresses.popleft()
        temp = (100 - job) / speeds.popleft()
        day = int(temp) if temp.is_integer() else int(temp) + 1
        while progresses and progresses[0] + day * speeds[0] >= 100:
            count += 1
            progresses.popleft()
            speeds.popleft()
        answer.append(count)
    return answer