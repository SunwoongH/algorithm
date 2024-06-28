'''
Created by sunwoong on 2024/06/28

풀이 시간 - 25분
'''
from collections import defaultdict
from math import ceil

def calculate(in_time, out_time):
    in_hour, in_minute = list(map(lambda x: int(x), in_time.split(":")))
    out_hour, out_minute = list(map(lambda x: int(x), out_time.split(":")))
    return (out_hour * 60 + out_minute) - (in_hour * 60 + in_minute)
    
def solution(fees, records):
    answer = []
    info = defaultdict(str)
    time = defaultdict(int)
    for record in records:
        t, num, code = record.split()
        if code == 'IN':
            info[num] = t
            continue
        time[num] += calculate(info[num], t)
        info[num] = ""
    for num in info.keys():
        if info[num]:
            time[num] += calculate(info[num], '23:59')
            info[num] = ""
    for num in sorted(info.keys()):
        if time[num] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + ceil(((time[num] - fees[0]) / fees[2])) * fees[3])
    return answer