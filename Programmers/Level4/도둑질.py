'''
Created by sunwoong on 2025/03/04
'''

def solution(money):
    dp = [0 for _ in range(len(money))]
    answer = 0
    dp[1] = money[1]
    for i in range(2, len(money)):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer = max(answer, dp[len(money) - 1])
    dp[0] = money[0]
    dp[1] = max(dp[0], money[1])
    for i in range(2, len(money) - 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + money[i])
    answer = max(answer, dp[len(money) - 2])
    return answer