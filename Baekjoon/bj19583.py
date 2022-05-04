'''
Created by sunwoong 2022/05/04
'''
import sys
import collections

start, end, s_end = sys.stdin.readline().split()
meeting_start = int(''.join(start.split(':')))
meeting_end = int(''.join(end.split(':')))
streaming_end = int(''.join(s_end.split(':')))

attendance_book, count = collections.defaultdict(bool), 0
while True:
    log = sys.stdin.readline()
    if len(log) < 5:
        break
    time, name = log.split()
    time = int(''.join(time.split(':')))
    if time <= meeting_start:
        attendance_book[name] = True
    elif attendance_book[name] and time >= meeting_end and time <= streaming_end:
        count += 1
        attendance_book[name] = False
print(count)