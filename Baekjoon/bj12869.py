'''
Created by sunwoong on 2022/11/21 (답은 잘 나오는데 시간 초과.......)
'''
import sys
from itertools import permutations
sys.setrecursionlimit(10 ** 8)

def dfs(depth, total):
    if total == 0:
        global attack_count
        attack_count = min(attack_count, depth)
        return
    elif total < 0:
        return
    for order in permutations(range(n), n):
        valid = dict()
        i = 0
        for pos in order:
            if lifes[i] - attacks[pos] >= 0:
                lifes[i] -= attacks[pos]
            else:
                valid[pos] = lifes[i]
                lifes[i] = 0
            i += 1
        dfs(depth + 1, sum(lifes))
        i = 0
        for pos in order:
            if pos in valid:
                lifes[i] += valid[pos]
            else:
                lifes[i] += attacks[pos]
            i += 1

attacks = (9, 3, 1)
n = int(sys.stdin.readline())
lifes = list(map(int, sys.stdin.readline().split()))
attack_count = sys.maxsize
dfs(0, sum(lifes))
print(attack_count)