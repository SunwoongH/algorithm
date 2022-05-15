'''
Created by sunwoong on 2022/05/15
'''
import sys
import heapq

n = int(sys.stdin.readline())
present = []
for _ in range(n):
    select = sys.stdin.readline().rstrip()
    if select == '0':
        if not present:
            print(-1)
        else:
            print(abs(heapq.heappop(present)))
    else:
        select = list(map(int, select.split()))
        select.pop(0)
        for new_present in select:
            heapq.heappush(present, -new_present)