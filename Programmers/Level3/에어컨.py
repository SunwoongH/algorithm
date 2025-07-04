'''
Created by sunwoong on 2025/07/04
'''

def is_valid(onboard, i, temperature, t1, t2):
    return not (onboard[i] and not (t1 <= temperature <= t2))

def solution(temperature, t1, t2, a, b, onboard):
    temperature += 10
    t1 += 10
    t2 += 10
    dp = [[int(1e9) for _ in range(51)] for _ in range(len(onboard))]
    dp[0][temperature] = 0
    
    for i in range(len(onboard) - 1):
        for j in range(51):
            if dp[i][j] == int(1e9):
                continue
            pos = None
            if j < temperature:
                pos = j + 1
            elif j > temperature:
                pos = j - 1
            else:
                pos = j
            if is_valid(onboard, i + 1, pos, t1, t2):
                dp[i + 1][pos] = min(dp[i + 1][pos], dp[i][j])
            
            for pos, cost in [(j + 1, a), (j - 1, a), (j, b)]:
                if 0 <= pos <= 50 and is_valid(onboard, i + 1, pos, t1, t2):
                    dp[i + 1][pos] = min(dp[i + 1][pos], dp[i][j] + cost)
            
    return min(dp[len(onboard) - 1])