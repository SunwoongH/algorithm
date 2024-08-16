'''
Created by sunwoong on 2024/08/16
'''

def solution(N, number):
    if N == number:
        return 1
    
    cases = [set() for _ in range(8)]
    for i, case in enumerate(cases):
        case.add(int(str(N) * (i + 1)))
    
    for i in range(1, len(cases)):
        for j in range(i):
            for op1 in cases[j]:
                for op2 in cases[i - j - 1]:
                    cases[i].add(op1 + op2)
                    cases[i].add(op1 - op2)
                    cases[i].add(op1 * op2)
                    if op2 > 0:
                        cases[i].add(op1 // op2)
        if number in cases[i]:
            return i + 1
    
    return -1