'''
Created by sunwoong on 2022/08/08
'''
import sys
from typing import List

def implement_calender(schedule: List[int], length: int) -> List[int]:
    calender = [[0 for _ in range(length + 1)]]
    for start, end in schedule:
        i = 0
        while calender[i][start] != 0:
            if len(calender) - 1 == i:
                calender.append([0 for _ in range(length + 1)])
            i += 1
        for j in range(start, end + 1):
            calender[i][j] = 1
    return calender
            
def calculation_interval(schedule: List[int]) -> List[int]:
    interval = []
    for start, end in schedule:
        if not interval or interval[-1][1] + 1 < start:
            interval.append([start, end])
            continue
        interval[-1][1] = max(interval[-1][1], end)
    return interval

def calculation_area(calender: List[int], interval: List[int]) -> int:
    area = 0
    for start, end in interval:
        i = len(calender) - 1
        while not any(calender[i][start:end + 1]):
            i -= 1
        area += (end - start + 1) * (i + 1)
    return area

n = int(sys.stdin.readline())
length = 0
schedule = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    length = max(length, end)
    schedule.append((start, end))

schedule.sort(key=lambda x: (x[0], -(x[1] - x[0]))) 
calender = implement_calender(schedule, length)
interval = calculation_interval(schedule)
print(calculation_area(calender, interval))