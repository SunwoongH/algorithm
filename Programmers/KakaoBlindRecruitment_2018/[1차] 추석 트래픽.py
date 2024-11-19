'''
Created by sunwoong on 2024/11/19

'''

def convert_to_milliseconds(time):
    hour, miniutes, seconds = time.split(":")
    seconds, milliseconds = seconds.split(".")
    return int(hour) * 60 * 60 * 1000 + int(miniutes) * 60 * 1000 + int(seconds) * 1000 + int(milliseconds)

def solution(lines):
    answer = 1
    times = []
    
    for line in lines:
        _, time, interval = line.split()
        
        milliseconds = convert_to_milliseconds(time)
        
        interval = interval[:len(interval) - 1]
        interval = interval.split('.')
        
        target = 0
        
        if len(interval) == 1:
            target = int(interval[0]) * 1000
        else:
            target = int(interval[0]) * 1000 + int(interval[1])
        
        start = milliseconds - target + 1
        times.append([start, milliseconds])
        
    for i in range(len(times) - 1):
        count = 1
        for j in range(i + 1, len(times)):
            if times[i][1] + 1000 - 1 >= times[j][0]:
                count += 1
        answer = max(answer, count)
    
    return answer