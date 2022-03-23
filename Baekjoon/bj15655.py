'''
Created by sunwoong on 2022/03/23
'''
import sys

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
number.sort()

sequence = []
def dfs(start: int) -> None:
    if len(sequence) == m:
        print(*sequence)
        return
    for i in range(start, len(number)):
        sequence.append(number[i])
        dfs(i + 1)
        sequence.pop()
dfs(0)