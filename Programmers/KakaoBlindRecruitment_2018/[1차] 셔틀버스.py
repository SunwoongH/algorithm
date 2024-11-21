'''
Created by sunwoong on 2024/11/21

'''

def time_to_miniutes(time):
    hour, miniute = time.split(":")
    return int(hour) * 60 + int(miniute)

def miniutes_to_time(miniutes):
    hour, miniute = divmod(miniutes, 60)
    return f'{hour:02}:{miniute:02}'

def solution(n, t, m, timetable):
    timetable.sort(reverse=True)
    
    answer = ""
    
    start = '09:00'
    
    for i in range(n):
        stack = []
        if i != n - 1:
            for _ in range(m):
                if timetable and time_to_miniutes(timetable[-1]) <= time_to_miniutes(start):
                    timetable.pop()
            start = miniutes_to_time(time_to_miniutes(start) + t)
        else:
            for _ in range(m):
                if timetable and time_to_miniutes(timetable[-1]) <= time_to_miniutes(start):
                    stack.append(timetable.pop())
            if stack and len(stack) == m:
                answer = miniutes_to_time(time_to_miniutes(stack[-1]) - 1)
            else:
                answer = start
                    
    return answer