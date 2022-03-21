'''
Created by sunwoong on 2022/03/21
'''
import sys

n = int(sys.stdin.readline())

sequence = []
def dfs() -> None:
    if len(sequence) == n:
        print(*sequence)
        return
    for num in range(1, n + 1):
        if num not in sequence:
            sequence.append(num)
            dfs()
            sequence.pop()
dfs()