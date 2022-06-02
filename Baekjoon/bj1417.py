'''
Created by sunwoong on 2022/06/02
'''
import sys
import heapq

n = int(sys.stdin.readline())
heap = []
for i in range(n):
    people = int(sys.stdin.readline())
    if i == 0:
        target = people
    else:
        heapq.heappush(heap, -people)
        
result = 0
if n != 1:
    win = False
    while not win:
        ticket = abs(heapq.heappop(heap))
        if target > ticket:
            break
        target, result = target + 1, result + 1
        heapq.heappush(heap, -(ticket - 1))
print(result)