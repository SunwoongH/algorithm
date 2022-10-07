'''
Created by sunwoong on 2022/10/07
'''
import sys
from itertools import combinations

HOUSE = 1
CHICKEN = 2
n, m = map(int, sys.stdin.readline().split())
houses = []
origin_chickens = []
city = []
for r in range(n):
    line = list(map(int, sys.stdin.readline().split()))
    for c in range(n):
        if line[c] == HOUSE:
            houses.append((r, c))
        elif line[c] == CHICKEN:
            origin_chickens.append((r, c))
    city.append(line)
min_distance = sys.maxsize
for chickens in combinations(origin_chickens, m):
    distance = 0
    for house in houses:
        house_distance = sys.maxsize
        for chicken in chickens:
            house_distance = min(house_distance, abs(house[0] - chicken[0]) + abs(house[1] - chicken[1]))
        distance += house_distance
    min_distance = min(min_distance, distance)
print(min_distance)