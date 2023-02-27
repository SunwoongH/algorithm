'''
Created by sunwoong on 2023/02/27
'''
import sys
from itertools import combinations
input = sys.stdin.readline

minimum = sys.maxsize
n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
group = set(range(n))
for start in range(1, n // 2 + 1):
    for start_combi in combinations(range(n), start):
        start_combi = set(start_combi)
        link_combi = group.difference(start_combi)
        start_ability = 0
        link_ability = 0
        for a, b in combinations(start_combi, 2):
            start_ability += board[a][b] + board[b][a]
        for a, b in combinations(link_combi, 2):
            link_ability += board[a][b] + board[b][a]
        minimum = min(minimum, abs(start_ability - link_ability))
print(minimum)