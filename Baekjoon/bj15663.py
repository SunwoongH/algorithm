'''
Created by sunwoong on 2022/03/25
'''
import sys

n, m = map(int, sys.stdin.readline().split())
number = list(map(int, sys.stdin.readline().split()))
number.sort()

seen = set()
index = []
def dfs() -> None:
    if len(index) == m:
        sequence = tuple(map(lambda x: number[x], index))
        if sequence not in seen:
            seen.add(sequence)
            print(*sequence)
        return
    for i in range(len(number)):
        if i not in index:
            index.append(i)
            dfs()
            index.pop()
dfs()