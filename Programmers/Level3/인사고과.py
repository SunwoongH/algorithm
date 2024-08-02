'''
Created by sunwoong on 2024/08/02

풀이 시간 - 120분 (풀이 참조)
'''

def solution(scores):
    target_a, target_b = scores[0]
    answer = 1
    max_b = 0
    
    scores.sort(key=lambda x: (-x[0], x[1]))
    
    for a, b in scores:
        if target_a < a and target_b < b:
            return -1
        if b < max_b:
            continue
        max_b = b
        if a + b > target_a + target_b:
            answer += 1
    
    return answer