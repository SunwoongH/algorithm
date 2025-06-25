'''
Created by sunwoong on 2025/06/25
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

def find(room, a):
    if room[a] == a:
        return a
    room[a] = find(room, room[a])
    return room[a]

def union(room, a, b):
    parent_a = find(room, a)
    parent_b = find(room, b)
    
    if parent_a < parent_b:
        room[parent_a] = parent_b
    else:
        room[parent_b] = parent_a

def solution(k, room_number):
    answer = []
    room = defaultdict(int)
    
    for i in range(len(room_number)):
        num = room_number[i]
        room[num] = num
    
    for i in range(len(room_number)):
        num = room_number[i]
        
        if room[num] == 0:
            room[num] = num
            answer.append(num)
            if num < k:
                if room[num + 1] == 0:
                    room[num + 1] = num + 1
                union(room, num, num + 1)
        else:
            num = find(room, num)
            answer.append(num)
            if num < k:
                if room[num + 1] == 0:
                    room[num + 1] = num + 1
                union(room, num, num + 1)
    
    return answer