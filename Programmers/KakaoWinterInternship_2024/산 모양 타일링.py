'''
Created by sunwoong on 2024/09/30
'''

def solution(n, tops):
    counts = [0 for _ in range(n * 2 + 1)]
    counts[0] = 1
    counts[1] = 2
    
    for i in range(1, n * 2 + 1):
        if i % 2 != 0 and tops[i // 2] == 1:
            if i == 1:
                counts[i] += 1
                continue
            counts[i] = (counts[i - 1] * 2 + counts[i - 2]) % 10007
        else:
            if i == 1:
                continue
            counts[i] = (counts[i - 1] + counts[i - 2]) % 10007
    
    return counts[n * 2]