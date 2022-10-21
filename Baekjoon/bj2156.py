'''
Created by sunwoong on 2022/10/21
'''
import sys

n = int(sys.stdin.readline())
wine = [0]
for _ in range(n):
    amount = int(sys.stdin.readline())
    wine.append(amount)
dp = [0 for _ in range(n + 1)]
dp[1] = wine[1]
if n > 1:
    dp[2] = dp[1] + wine[2]
    if n > 2:
        for i in range(3, n + 1):
            if i == 3:
                dp[i] = wine[i] + max(dp[i - 2], dp[i - 3] + wine[i - 1])
            else:
                dp[i] = wine[i] + max(dp[i - 2], dp[i - 3] + wine[i - 1], dp[i - 4] + wine[i - 1])
print(max(dp))