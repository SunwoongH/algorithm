'''
Created by sunwoong on 2023/06/20
'''
from itertools import combinations

def calculate_an_intersaction(first, second):
    a, b, e = first
    c, d, f = second
    pivot = a * d - b * c
    if pivot == 0:
        return None, None
    x = (b * f - e * d) / pivot
    y = (e * c - a * f) / pivot
    return x, y

def solution(line):
    coordinates = []
    for case in combinations(line, 2):
        first, second = case
        x, y = calculate_an_intersaction(first, second)
        if x is None and y is None:
            continue
        if x.is_integer() and y.is_integer():
            coordinates.append((int(x), int(y)))
    max_x, min_x = max(coordinates, key=lambda x: x[0])[0], min(coordinates, key=lambda x: x[0])[0]
    max_y, min_y = max(coordinates, key=lambda x: x[1])[1], min(coordinates, key=lambda x: x[1])[1]
    temp = [['.' for _ in range(max_x - min_x + 1)] for _ in range(max_y - min_y + 1)]
    for x, y in coordinates:
        temp[-y + max_y][x - min_x] = '*'
    return [''.join(line) for line in temp]