'''
Created by sunwoong on 2025/09/15
'''
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
items = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
money = [[0 for _ in range(k + 1)] for _ in range(n)]

def bfs(start):
    queue = deque([(start, 0)])
    
    while queue:
        city, time = queue.popleft()

        if city > n - 2:
            break

        walk_time, walk_money = items[city + 1][0], items[city + 1][1]
        if k >= time + walk_time and money[city + 1][time + walk_time] < money[city][time] + walk_money:
            money[city + 1][time + walk_time] = money[city][time] + walk_money
            queue.append((city + 1, time + walk_time))
        
        cycle_time, cycle_money = items[city + 1][2], items[city + 1][3]
        if k >= time + cycle_time and money[city + 1][time + cycle_time] < money[city][time] + cycle_money:
            money[city + 1][time + cycle_time] = money[city][time] + cycle_money
            queue.append((city + 1, time + cycle_time))

bfs(-1)
print(max(money[n - 1]))