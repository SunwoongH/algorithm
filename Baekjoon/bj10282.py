'''
Created by sunwoong on 2022/11/04
'''
import sys
from collections import defaultdict
import heapq

def spread_of_virus(start):
    heap = [(0, start)]
    time = [sys.maxsize for _ in range(n + 1)]
    time[start] = 0
    while heap:
        curr_time, curr = heapq.heappop(heap)
        if time[curr] < curr_time:
            continue
        for next, next_time in computer[curr]:
            if time[next] > time[curr] + next_time:
                time[next] = time[curr] + next_time
                heapq.heappush(heap, (time[next], next))        
    virus = []
    for cost in time:
        if cost >= sys.maxsize:
            continue
        virus.append(cost)
    return len(virus), max(virus)

test = int(sys.stdin.readline())
for _ in range(test):
    n, d, c = map(int, sys.stdin.readline().split())
    computer = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        computer[b].append((a, s))
    print(*spread_of_virus(c))