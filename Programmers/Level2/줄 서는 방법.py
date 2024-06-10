'''
Created by sunwoong on 2024/06/10

풀이 시간 - 60분
'''
from math import factorial

def solution(n, k):
    promising = [[i, True] for i in range(1, n + 1)] 
    lotation = n - 1
    answer = []
    while lotation > 0:
        if k == 0:
            for i in range(n - 1, -1, -1):
                if promising[i][1]:
                    promising[i][1] = False
                    answer.append(promising[i][0])
                    break
            
            lotation -= 1
            continue
        pos, k = divmod(k, factorial(lotation))
        if not k:
            count = 0
            for i in range(n):
                if promising[i][1]:
                    count += 1
                if count == pos:
                    promising[i][1] = False
                    answer.append(promising[i][0])
                    break
        else:
            count = 0
            for i in range(n):
                if promising[i][1]:
                    count += 1
                if count == pos + 1:
                    promising[i][1] = False
                    answer.append(promising[i][0])
                    break
        lotation -= 1
    for i in range(n):
        if promising[i][1]:
            promising[i][1] = False
            answer.append(promising[i][0])
            break
    return answer

def solution(n, k):
    promising = [num for num in range(1, n + 1)]
    k -= 1
    answer = []
    while promising:
        i, k = divmod(k, factorial(len(promising) - 1))
        answer.append(promising.pop(i))
    return answer