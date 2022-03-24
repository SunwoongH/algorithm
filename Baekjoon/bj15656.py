'''
Created by sunwoong on 2022/03/24
'''
import sys

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
number.sort()

sequence = []
def dfs() -> None:
    if len(sequence) == m:
        print(*sequence)
        return
    for num in number:
        sequence.append(num)
        dfs()
        sequence.pop()
dfs()