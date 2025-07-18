'''
Created by sunwoong on 2025/07/18
'''

def solution(strs, t):
    dp = [int(1e9) for _ in range(len(t) + 1)]
    dp[0] = 0
    for i in range(1, len(t) + 1):
        for k in range(1, 6):
            s = 0
            if i - k > 0:
                s = i - k
            if t[s:i] in strs:
                dp[i] = min(dp[i], dp[s] + 1)

    return dp[len(t)] if dp[len(t)] < int(1e9) else -1