'''
Created by sunwoong on 2025/09/17
'''
import sys

n = int(sys.stdin.readline())
rooms = list(map(int, sys.stdin.readline().split()))

if not any(rooms):
    print(n // 2)
    exit()

temp = 0
count = 0
room = 0
is_first = True
for i in range(len(rooms)):
    if rooms[i] > 0:
        if is_first:
            is_first = False
        if room > 0:
            count += (room + 1) // 2
            room = 0
        count += rooms[i]
        continue
    if is_first:
        temp += 1
    else:
        room += 1

if rooms[len(rooms) - 1] == 0 and rooms[0] == 0:
    temp += room
    count += (temp + 1) // 2
elif rooms[len(rooms) - 1] == 0:
    count += (room + 1) // 2
elif rooms[0] == 0:
    count += (temp + 1) // 2

print(count)