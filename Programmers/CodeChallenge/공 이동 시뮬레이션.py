'''
Created by sunwoong on 2025/04/16
'''

def solution(n, m, x, y, queries):
    r_min, c_min, r_max, c_max = x, y, x, y
    for i in range(len(queries) - 1, -1, -1):
        select, distance = queries[i]
        if select == 0:
            c_max += distance
            if c_max > m - 1:
                c_max = m - 1
            if c_min > 0:
                c_min += distance
        elif select == 1:
            c_min -= distance
            if c_min < 0:
                c_min = 0
            if c_max < m - 1:
                c_max -= distance
        elif select == 2:
            r_max += distance
            if r_max > n - 1:
                r_max = n - 1
            if r_min > 0:
                r_min += distance
        elif select == 3:
            r_min -= distance
            if r_min < 0:
                r_min = 0
            if r_max < n - 1:
                r_max -= distance
        if r_min > n - 1 or r_max < 0 or c_min > m - 1 or c_max < 0:
            return 0
    return (r_max - r_min + 1) * (c_max - c_min + 1)