'''
Created by sunwoong on 2023/06/21
'''
EMPTY = None

def write_a_number(n, count, map, sequence):
    is_finish = True
    for i in range(count * 2, n - count):
        if map[i][count] != EMPTY:
            return sequence, False, is_finish
        if is_finish:
            is_finish = False
        map[i][count] = sequence
        sequence += 1
    for i in range(count + 1, n - count * 2):
        if map[n - count - 1][i] != EMPTY:
            return sequence, False, is_finish
        map[n - count - 1][i] = sequence
        sequence += 1
    for i in range(n - count - 2, count * 2, -1):
        if map[i][i - count] != EMPTY:
            return sequence, False, is_finish
        map[i][i - count] = sequence
        sequence += 1
    return sequence, True, is_finish

def solution(n):
    map = [[EMPTY for _ in range(n)] for _ in range(n)]
    count = 0
    result = True
    sequence = 1
    while result:
        sequence, result, is_finish = write_a_number(n, count, map, sequence)
        if result and is_finish:
            break
        count += 1
    return [map[i][j] for i in range(n) for j in range(i + 1)]