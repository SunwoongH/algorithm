'''
Created by sunwoong on 2023/02/09

풀이 시간 - 39분
'''

def solution(survey, choices):
    mbti_table = {"R": [0, 1], "T": [0, 1], "C": [0, 2], "F": [0, 2], "J": [0, 3], "M": [0, 3], "A": [0, 4], "N": [0, 4]}
    score_table = {0: (3, 0), 1: (2, 0), 2: (1, 0), 3: (0, None), 4: (1, 1), 5: (2, 1), 6: (3, 1)}
    for i in range(len(survey)):
        score, pos = score_table[choices[i] - 1]
        if pos is not None:
            mbti_table[survey[i][pos]][0] += score
    temp = sorted(mbti_table.items(), key=lambda x: (x[1][1], -x[1][0], x[0]))
    mbti = ""
    for i in range(len(mbti_table)):
        if i % 2 == 0:
            mbti += temp[i][0]
    return mbti