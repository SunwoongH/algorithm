'''
Created by sunwoong on 2022/03/26
'''
import sys

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
number.sort()

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
        dfs(i + 1)
        sequence.pop()
dfs(0)