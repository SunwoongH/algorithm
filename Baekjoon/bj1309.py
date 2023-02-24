'''
Created by sunwoong on 2023/02/24
'''
import sys
input = sys.stdin.readline

MOD = 9_901
n = int(input())
if n == 1:
    print(3)
    sys.exit(0)
dp = [[0, 0, 0], [0, 0, 0]]
dp[0][0] = dp[0][1] = dp[0][2] = 1
for _ in range(n - 1):
    cases = sum(dp[0])
    dp[1][0] = cases
    dp[1][1] = cases - dp[0][1]
    dp[1][2] = cases - dp[0][2]
    for i in range(3):
        dp[0][i] = dp[1][i]
print(sum(dp[1]) % MOD)