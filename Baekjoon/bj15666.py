'''
Created by sunwoong on 2022/03/29
'''
import sys

n, m = map(int, sys.stdin.readline().split())
number = sorted(list(map(int, sys.stdin.readline().split())))

seen = set()
sequence = []
def dfs(start: int) -> None:
    if len(sequence) == m:
        temp = tuple(sequence)
        if temp not in seen:
            seen.add(temp)
            print(*temp)
        return
    for i in range(start, len(number)):
        sequence.append(number[i])
        dfs(i)
        sequence.pop()
dfs(0)