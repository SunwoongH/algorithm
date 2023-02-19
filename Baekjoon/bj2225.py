'''
Created by sunwoong on 2023/02/19
'''
import sys
input = sys.stdin.readline

MOD = 1_000_000_000
n, k = map(int, input().split())
dp = [[0 for _ in range(n + 1)] for _ in range(k + 1)]
for num in range(n + 1):
    dp[1][num] = 1
for count in range(2, k + 1):
    for num in range(n + 1):
        for i in range(num + 1):
            dp[count][num] = (dp[count][num] + dp[count - 1][i]) % MOD
print(dp[k][n])