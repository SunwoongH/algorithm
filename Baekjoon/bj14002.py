'''
Created by sunwoong on 2022/12/22
'''
import sys
input = sys.stdin.readline

n = int(input())
sequence = list(map(int, input().split()))
dp = [[1, [sequence[i]]] for i in range(n)]
for i in range(1, n):
    for j in range(i):
        if sequence[j] < sequence[i]:
            if dp[i][0] < dp[j][0] + 1:
                if dp[i][1]:
                    dp[i][1] = []
                dp[i][0] = dp[j][0] + 1
                dp[i][1].extend(dp[j][1])
                dp[i][1].append(sequence[i])
answer = max(dp, key=lambda x: x[0])
print(answer[0])
print(*answer[1])