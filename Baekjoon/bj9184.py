'''
Created by sunwoong on 2023/02/20
'''
import sys
input = sys.stdin.readline

SIZE = 100
def solution(a, b, c):
    if dp[a][b][c]:
        return dp[a][b][c]
    if a <= 50 or b <= 50 or c <= 50:
        dp[a][b][c] = 1 if not dp[a][b][c] else dp[a][b][c]
        return dp[a][b][c]
    if a > 70 or b > 70 or c > 70:
        dp[a][b][c] = solution(70, 70, 70) if not dp[70][70][70] else dp[70][70][70]
        return dp[a][b][c]
    if a < b and b < c:
        dp[a][b][c] += solution(a, b, c - 1) if not dp[a][b][c - 1] else dp[a][b][c - 1]
        dp[a][b][c] += solution(a, b - 1, c - 1) if not dp[a][b - 1][c - 1] else dp[a][b - 1][c - 1]
        dp[a][b][c] -= solution(a, b - 1, c) if not dp[a][b - 1][c] else dp[a][b - 1][c]
        return dp[a][b][c]
    dp[a][b][c] += solution(a - 1, b, c) if not dp[a - 1][b][c] else dp[a - 1][b][c]
    dp[a][b][c] += solution(a - 1, b - 1, c) if not dp[a - 1][b - 1][c] else dp[a - 1][b - 1][c]
    dp[a][b][c] += solution(a - 1, b, c - 1) if not dp[a - 1][b][c - 1] else dp[a - 1][b][c - 1]
    dp[a][b][c] -= solution(a - 1, b - 1, c - 1) if not dp[a - 1][b - 1][c - 1] else dp[a - 1][b - 1][c - 1]
    return dp[a][b][c]
    
dp = [[[0 for _ in range(SIZE + 1)] for _ in range(SIZE + 1)] for _ in range(SIZE + 1)]
while True:
    a, b, c = map(lambda x: int(x) + 50, input().split())
    if a == 49 and b == 49 and c == 49:
        break
    print(f'w({a - 50}, {b - 50}, {c - 50}) = {solution(a, b, c)}')