'''
Created by sunwoong on 2022/09/01
'''
import sys

n = int(sys.stdin.readline())
music = [0] + list(map(int, sys.stdin.readline().split()))
question = int(sys.stdin.readline())
dp = [0 for _ in range(n + 1)]
for i in range(2, n + 1):
    if music[i] < music[i - 1]:
        dp[i] = dp[i - 1] + 1
    else:
        dp[i] = dp[i - 1]
for _ in range(question):
    start, end = map(int, sys.stdin.readline().split())
    print(dp[end] - dp[start])