'''
Created by sunwoong on 2024/10/03

풀이 시간 - 110분
'''
from collections import deque

def time_to_second(time):
    h, m, s = time.split(":")
    return int(h) * 60 * 60 + int(m) * 60 + int(s)

def second_to_time(second):
    h = second // (60 * 60)
    m = (second - h * 60 * 60) // 60
    s = (second - h * 60 * 60 - m * 60)
    return f"{h:02}:{m:02}:{s:02}"

def solution(play_time, adv_time, logs):
    play_time = time_to_second(play_time)
    adv_time = time_to_second(adv_time)
    
    times = [0 for _ in range(play_time + 1)]
    for log in logs:
        start, end = log.split('-')
        start_time = time_to_second(start)
        end_time = time_to_second(end)
        times[start_time] += 1
        times[end_time] += -1
    for i in range(play_time):
        times[i + 1] += times[i]
    
    answer = None
    max_time = 0
    seen = deque()
    accumulate_time = 0
    left = 0
    for right in range(play_time + 1):
        if right < adv_time:
            seen.append(times[right])
            accumulate_time += times[right]
            continue
        if answer is None:
            answer = left
            max_time = accumulate_time
            if right == play_time:
                break
        
        left += 1
        second = seen.popleft()
        accumulate_time -= second
        seen.append(times[right])
        accumulate_time += times[right]
        
        if max_time < accumulate_time:
            answer = left
            max_time = accumulate_time
            
    return second_to_time(answer)
    