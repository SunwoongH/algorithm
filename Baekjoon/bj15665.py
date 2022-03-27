'''
Created by sunwoong on 2022/03/27
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
number = sorted(list(map(int, sys.stdin.readline().split())))

seen = collections.defaultdict(bool)
sequence = []
def dfs() -> None:
    if len(sequence) == m:
        temp = tuple(sequence)
        if not seen[temp]:
            seen[temp] = True
            print(*temp)
        return
    for num in number:
        sequence.append(num)
        dfs()
        sequence.pop()
dfs()