'''
Created by sunwoong 2022/05/07
'''
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))
heapq.heapify(cards)
for _ in range(m):
    card1, card2 = heapq.heappop(cards), heapq.heappop(cards)
    heapq.heappush(cards, card1 + card2)
    heapq.heappush(cards, card1 + card2)
print(sum(cards))