'''
문제 - 주식을 사고팔기 가장 좋은 시점

한 번의 거래로 낼 수 있는 최대 이익을 산출하라.
'''
from typing import List
import sys

# 브루트 포스 풀이 - 시간 초과
class Solution1:
    def maxprofit(self, prices: List[int]) -> int:
        profit = 0
        for i, price in enumerate(prices):
            for j in range(i + 1, len(prices)):
                profit = max(profit, prices[j] - price)
        return profit
    
# 카데인 알고리즘 풀이
class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = sys.maxsize
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price - min_price)
        return profit