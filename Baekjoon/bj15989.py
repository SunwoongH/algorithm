'''
Created by sunwoong on 2023/02/05
'''
import sys
input = sys.stdin.readline

SIZE = 10000
nums = [1, 2, 3]
t = int(input())
dp = [0 for _ in range(SIZE + 1)]
dp[0] = 1
for num in nums:
    for i in range(num, SIZE + 1):
        dp[i] += dp[i - num]
for _ in range(t):
    case = int(input())
    print(dp[case])