'''
Created by sunwoong on 2022/08/19
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
trains = [collections.deque(['0' for _ in range(20)]) for _ in range(n + 1)]
for _ in range(m):
    choice, *order = map(int, sys.stdin.readline().split())
    if choice == 1:
        trains[order[0]][order[1] - 1] = '1'
    elif choice == 2:
        trains[order[0]][order[1] - 1] = '0'
    elif choice == 3:
        trains[order[0]].rotate(1)
        trains[order[0]][0] = '0'
    else:
        trains[order[0]].rotate(-1)
        trains[order[0]][-1] = '0'
pass_trains = set()
for i in range(1, n + 1):
    pass_trains.add(''.join(trains[i]))
print(len(pass_trains))