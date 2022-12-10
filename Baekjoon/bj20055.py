'''
Created by sunwoong on 2022/12/10
'''
import sys
from collections import deque
    
def check_the_last_element():
    if contents[n - 1]:
        contents[n - 1] = False

def level_1():
    conveyor.rotate(1)
    contents.rotate(1)

def level_2():
    for i in range(n - 1, 0, -1):
        if not contents[i] and conveyor[i] > 0 and contents[i - 1]:
            conveyor[i] -= 1
            contents[i - 1] = False
            contents[i] = True

def level_3():
    if conveyor[0] > 0:
        conveyor[0] -= 1
        contents[0] = True

def level_4():
    count = 0
    for pos in conveyor:
        if pos == 0:
            count += 1
    return True if count >= k else False

n, k = map(int, sys.stdin.readline().split())
conveyor = deque(list(map(int, sys.stdin.readline().split())))
contents = deque([False for _ in range(n * 2)])
process = 0
while True:
    process += 1
    check_the_last_element()
    level_1()
    check_the_last_element()
    level_2()
    check_the_last_element()
    level_3()
    result = level_4()
    if result:
        break
print(process)