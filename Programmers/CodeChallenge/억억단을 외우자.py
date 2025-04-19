'''
Created by sunwoong on 2025/04/19
'''

def solution(e, starts):
    answer = []
    
    counting = [1 for _ in range(e + 1)]
    for i in range(2, len(counting)):
        for j in range(i, len(counting), i):
            counting[j] += 1
        
    maximum = (counting[e], e)
    promising = [0 for _ in range(e + 1)]
    for i in range(e, -1, -1):
        if i == e:
            promising[i] = e
            continue
        if maximum[0] <= counting[i]:
            promising[i] = i
            maximum = (counting[i], i)
        else:
            promising[i] = maximum[1]
            
    for start in starts:
        answer.append(promising[start])
        
    return answer