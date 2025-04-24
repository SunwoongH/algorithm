'''
Created by sunwoong on 2025/04/24
'''
import sys
sys.setrecursionlimit(10 ** 6)

weight = [
        [1, 7, 6, 7, 5, 4, 5, 3, 2, 3],
        [7, 1, 2, 4, 2, 3, 5, 4, 5, 6],
        [6, 2, 1, 2, 3, 2, 3, 5, 4, 5],
        [7, 4, 2, 1, 5, 3, 2, 6, 5, 4],
        [5, 2, 3, 5, 1, 2, 4, 2, 3, 5],
        [4, 3, 2, 3, 2, 1, 2, 3, 2, 3],
        [5, 5, 3, 2, 4, 2, 1, 5, 3, 2],
        [3, 4, 5, 6, 2, 3, 5, 1, 2, 4],
        [2, 5, 4, 5, 3, 2, 3, 2, 1, 2],
        [3, 6, 5, 4, 5, 3, 2, 4, 2, 1],
    ]

def calculate(dp, numbers, i, left, right):
    if i == len(numbers):
        return 0
    if dp[i][left][right] < float(1e9):
        return dp[i][left][right]
    
    number = int(numbers[i])
    if number != right:
        dp[i][left][right] = min(dp[i][left][right], calculate(dp, numbers, i + 1, number, right) + weight[left][number])
    if number != left:
        dp[i][left][right] = min(dp[i][left][right], calculate(dp, numbers, i + 1, left, number) + weight[right][number])
    
    return dp[i][left][right]
    
def solution(numbers):
    dp = [[[float(1e9) for _ in range(10)] for _ in range(10)] for _ in range(len(numbers))]
    
    calculate(dp, numbers, 0, 4, 6)
    
    return calculate(dp, numbers, 0, 4, 6)