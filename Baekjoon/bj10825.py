'''
Created by sunwoong on 2022/06/22
'''
import sys

n = int(sys.stdin.readline())
score = []
for _ in range(n):
    score.append(list(sys.stdin.readline().split()))
score.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for line in score:
    print(line[0])