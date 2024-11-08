'''
Created by sunwoong on 2024/11/08
'''

def solution(N, stages):
    stages.sort()
    answer = []
    
    prev = -1
    curr = -1
    
    for s in range(1, N + 1):
        while curr + 1 < len(stages):
            if stages[curr + 1] == s:
                curr += 1
            else:
                break
        if len(stages) - prev - 1 == 0:
            answer.append((s, 0))
            continue
        
        answer.append((s, (curr - prev) / (len(stages) - prev - 1)))
        prev = curr
    
    answer = list(map(lambda x: x[0], sorted(answer, key=lambda x: -x[1])))
    
    return answer