'''
Created by sunwoong on 2023/01/29
'''
import sys
input = sys.stdin.readline

n = int(input())
cards = [0] + list(map(int, input().split()))
dp = [0 for _ in range(n + 1)]
dp[1] = cards[1]
for i in range(2, n + 1):
    pivot = i / 2
    dp[i] = cards[i]
    for j in range(i - 1, int(pivot) - 1 if pivot.is_integer() else int(pivot), -1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])
print(dp[n])