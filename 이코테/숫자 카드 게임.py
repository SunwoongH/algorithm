'''
Created by sunwoong on 2023/02/14
'''
import sys
input = sys.stdin.readline

n, m  = map(int, input().split())
cards = []
for _ in range(n):
    line = list(map(int, input().split()))
    line.sort()
    cards.append(line)
cards = list(zip(*cards))
print(max(cards[0]))