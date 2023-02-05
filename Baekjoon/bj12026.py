'''
Created by sunwoong on 2023/02/05
'''
import sys
input = sys.stdin.readline

n = int(input())
words = list(input().rstrip())
dp = [sys.maxsize for _ in range(n)]
dp[0] = 0
table = {'B': 'J', 'O': 'B', 'J': 'O'}
for i in range(1, n):
    for j in range(i - 1, -1, -1):
        if words[j] == table[words[i]]:
            dp[i] = min(dp[i], dp[j] + pow((j - i), 2))
print(dp[n - 1]) if dp[n - 1] != sys.maxsize else print(-1)