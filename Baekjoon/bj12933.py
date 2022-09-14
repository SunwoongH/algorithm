'''
Created by sunwoong on 2022/09/14
'''
import sys

sound = "quack"
index_table = []
sequence = sys.stdin.readline().rstrip()
is_possible = True
for char in sequence:
    is_new_sound = True
    for i, item in enumerate(index_table):
        index, _ = item
        if char == sound[(index + 1) % len(sound)]:
            if is_new_sound:
                is_new_sound = False
            index_table[i][0] = (index + 1) % len(sound)
            if not index_table[i][1]:
                if index_table[i][0] == len(sound) - 1:
                    index_table[i][1] = True
            else:
                if index_table[i][0] == 0:
                    index_table[i][1] = False
            break
    if is_new_sound:
        if char == 'q':
            index_table.append([0, False])
        else:
            is_possible = False
            break
print(len(index_table)) if is_possible and all(list(map(lambda x: x[1], index_table))) else print(-1)