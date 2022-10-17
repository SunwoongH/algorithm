'''
Created by sunwoong on 2022/10/17
'''
import sys

left = [['q', 'w', 'e', 'r', 't'],
        ['a', 's', 'd', 'f', 'g'],
        ['z', 'x', 'c', 'v', 'X']]
right = [['X', 'y', 'u', 'i', 'o', 'p'],
         ['X', 'h', 'j', 'k', 'l', 'X'],
         ['b', 'n', 'm', 'X', 'X', 'X']]

def find_position(target, is_left):
    for r in range(len(left) if is_left else len(right)):
        for c in range(len(left[0]) if is_left else len(right[0])):
            if target == (left[r][c] if is_left else right[r][c]):
                return r, c

left_table = set()
for data in left:
    left_table = left_table.union(set(data))
n, m = sys.stdin.readline().rstrip().split()
sequence = sys.stdin.readline().rstrip()
left_prev, right_prev = n, m
distance = 0
for char in sequence:
    if char in left_table:
        prev_r, prev_c = find_position(left_prev, True)
        curr_r, curr_c = find_position(char, True)
        distance += abs(prev_r - curr_r) + abs(prev_c - curr_c)
        left_prev = char
    else:
        prev_r, prev_c = find_position(right_prev, False)
        curr_r, curr_c = find_position(char, False)
        distance += abs(prev_r - curr_r) + abs(prev_c - curr_c)
        right_prev = char
print(distance + len(sequence))