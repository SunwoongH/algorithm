'''
Created by sunwoong on 2022/05/27
'''
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
present_box = list(map(int, sys.stdin.readline().split()))
children = list(map(int, sys.stdin.readline().split()))
heap = []
for present in present_box:
    heapq.heappush(heap, -present)
check = True
for order in children:
    present = heapq.heappop(heap)
    if present + order < 0:
        heapq.heappush(heap, present + order)
    elif present + order > 0:
        check = False
        break
print(1) if check else print(0)