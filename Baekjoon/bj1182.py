'''
Created by sunwoong on 2022/03/16
'''
import sys

n, target = map(int, sys.stdin.readline().split())
sequence = list(map(int, sys.stdin.readline().split()))

result = 0
def dfs(start: int, sum_of_num: int, check: bool=False) -> None:
    if check and sum_of_num == target:
        global result
        result += 1
    for i in range(start, len(sequence)):
        dfs(i + 1, sum_of_num + sequence[i], True)
dfs(0, 0)
print(result)