'''
Created by sunwoong on 2025/04/07
'''

def solution(cookie):
    if len(cookie) == 1:
        return 0
    
    answer = 0
    for i in range(len(cookie) - 1):
        left_weight = right_weight = 0
        left = i
        right = i + 1
        left_weight += cookie[left]
        right_weight += cookie[right]
        while 0 <= left and right < len(cookie):
            if left_weight == right_weight:
                answer = max(answer, left_weight)
                if 0 < left and right < len(cookie) - 1:
                    left -= 1
                    left_weight += cookie[left]
                    right += 1
                    right_weight += cookie[right]
                else:
                    break
            elif left_weight < right_weight and 0 < left:
                left -= 1
                left_weight += cookie[left]
            elif left_weight > right_weight and right < len(cookie) - 1:
                right += 1
                right_weight += cookie[right]
            else:
                break
    return answer