'''
Created by sunwoong on 2022/08/04
'''
import sys

result = set()
m = int(sys.stdin.readline())
for _ in range(m):
    order = sys.stdin.readline().split()
    if order[0] == 'add' and int(order[1]) not in result:
        result.add(int(order[1]))
    elif order[0] == 'remove' and int(order[1]) in result:
        result.remove(int(order[1]))
    elif order[0] == 'check':
        print(1) if int(order[1]) in result else print(0)
    elif order[0] == 'toggle':
        result.remove(int(order[1])) if int(order[1]) in result else result.add(int(order[1]))
    elif order[0] == 'all':
        result = set(range(1, 21))
    else:
        result.clear()