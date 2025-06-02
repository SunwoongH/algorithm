'''
Created by sunwoong on 2025/06/01
'''
import sys

n = int(sys.stdin.readline())
cost = list(map(int, sys.stdin.readline().split()))
order = list(zip(range(len(cost)), cost))
m = int(sys.stdin.readline())

if n == 1:
    print(0)
    exit()

cost = sorted(order, key=lambda x: x[1])

minimum = cost[0]
sequence = ""
total = 0
if minimum[0] == 0:
    if cost[1][1] > m:
        print(0)
        exit()
    sequence += str(cost[1][0])
    sequence += str(minimum[0]) * ((m - cost[1][1]) // minimum[1])
    total = cost[1][1] + ((m - cost[1][1]) // minimum[1]) * minimum[1]
else:
    sequence = str(minimum[0]) * (m // minimum[1])
    total = (m // minimum[1]) * minimum[1]

sequence = list(sequence)

for i in range(len(sequence)):
    for j in range(len(order) - 1, -1, -1):
        if order[j][0] <= int(sequence[i]):
            continue
        if i == 0 and minimum[0] == 0:
            total -= cost[1][1]
        else:
            total -= minimum[1]
        if total + order[j][1] <= m:
            sequence[i] = order[j][0]
            total += order[j][1]
            continue
        if i == 0 and minimum[0] == 0:
            total += cost[1][1]
        else:
            total += minimum[1]

sequence = ''.join(map(str, sequence))
print(sequence)