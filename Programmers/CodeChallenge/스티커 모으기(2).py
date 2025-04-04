'''
Created by sunwoong on 2025/04/04
'''

def solution(sticker):
    if len(sticker) == 1:
        return sticker[0]
    
    case_1 = [sticker[i] for i in range(len(sticker))]
    case_2 = [sticker[i] for i in range(len(sticker))]
    
    case_1[-1] = 0
    case_1[1] = max(case_1[1], case_1[0])
    case_2[0] = 0
    
    for i in range(2, len(sticker)):
        case_1[i] = max(case_1[i - 2] + case_1[i], case_1[i - 1])
        case_2[i] = max(case_2[i - 2] + case_2[i], case_2[i - 1])

    return max(case_1[-1], case_2[-1])