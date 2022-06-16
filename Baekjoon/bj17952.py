'''
Created by sunwoong on 2022/06/16
'''
import sys

n = int(sys.stdin.readline())
result = 0
time = 0
is_task = False
task = None
queue = []
while time < n:
    time += 1
    data = sys.stdin.readline()
    if data[0] == '0':
        if not is_task:
            continue
    else:
        _, score, need_time = map(int, data.split())
        if task:
            queue.append([task[0], task[1]])
        else:
            is_task = True
        task = [score, need_time]
    task[1] -= 1
    if task[1] == 0:
        result += task[0]
        if not queue:
            is_task = False
            task = None
        else:
            task = queue.pop()
print(result)