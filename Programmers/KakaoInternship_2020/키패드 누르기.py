'''
Created by sunwoong on 2024/05/23

풀이 시간 - 15분
'''

def solution(numbers, hand):
    answer = []
    keys = [1, 2, 3, 4, 5, 6, 7, 8, 9, '*', 0, '#']
    key_table = dict()
    for i in range(3):
        for j in range(4):
            key_table[keys[j * 3 + i]] = (i, j)
    left, right = '*', '#'
    for num in numbers:
        if num in [1, 4, 7]:
            answer.append("L")
            left = num
        elif num in [3, 6, 9]:
            answer.append("R")
            right = num
        else:
            left_distance = abs(key_table[num][0] - key_table[left][0]) + abs(key_table[num][1] - key_table[left][1])
            right_distance = abs(key_table[num][0] - key_table[right][0]) + abs(key_table[num][1] - key_table[right][1])
            if left_distance > right_distance:
                answer.append("R")
                right = num
            elif left_distance < right_distance:
                answer.append("L")
                left = num
            else:
                if hand == "left":
                    answer.append("L")
                    left = num
                else:
                    answer.append("R")
                    right = num
    return ''.join(answer)