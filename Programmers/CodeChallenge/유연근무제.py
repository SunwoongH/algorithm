'''
Created by sunwoong on 2025/02/15
'''

promising = ['o', 'o', 'o', 'o', 'o', 'x', 'x']

def convert(time):
    hour, miniute = divmod(time, 100)
    time = hour * 60 + miniute
    promising_time = time + 10
    hour, miniute = divmod(promising_time, 60)
    return hour * 100 + miniute

def solution(schedules, timelogs, startday):
    startday -= 1
    answer = len(schedules)
    for i in range(len(schedules)):
        pos = startday
        promising_time = convert(schedules[i])
        for k in range(len(promising)):
            if promising[pos] == 'o':
                if promising_time < timelogs[i][k]:
                    answer -= 1
                    break
            pos = (pos + 1) % len(promising)

    return answer