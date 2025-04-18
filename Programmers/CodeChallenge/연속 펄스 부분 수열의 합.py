'''
Created by sunwoong on 2025/04/18
'''

def solution(sequence):
    case_1 = [sequence[i] if i % 2 == 0 else sequence[i] * -1 for i in range(len(sequence))]
    case_2 = [sequence[i] * -1 if i % 2 == 0 else sequence[i] for i in range(len(sequence))]

    for i in range(1, len(sequence)):
        case_1[i] = max(case_1[i - 1] + case_1[i], case_1[i])
        case_2[i] = max(case_2[i - 1] + case_2[i], case_2[i])
    
    return max(max(case_1), max(case_2))