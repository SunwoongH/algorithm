'''
Created by sunwoong on 2022/10/02
'''
import sys

n = int(sys.stdin.readline())
distance = list(map(int, sys.stdin.readline().split()))
gas_station = list(map(int, sys.stdin.readline().split()))

result = 0
prev = None
for i in range(len(distance)):
    if prev and prev < gas_station[i]:
        result += distance[i] * prev
        continue
    prev = gas_station[i]
    result += distance[i] * gas_station[i]
print(result)