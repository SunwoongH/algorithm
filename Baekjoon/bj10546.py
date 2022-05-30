'''
Created by sunwoong on 2022/05/30
'''
import sys
import collections

n = int(sys.stdin.readline().rstrip())
participant = collections.defaultdict(int)

for _ in range(n):
    player = sys.stdin.readline().rstrip()
    participant[player] += 1

for _ in range(n - 1):
    player = sys.stdin.readline().rstrip()
    participant[player] -= 1
        
for player in participant.keys():
    if participant[player] > 0:
        print(player)