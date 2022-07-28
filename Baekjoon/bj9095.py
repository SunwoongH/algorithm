'''
Created by sunwoong on 2022/07/28
'''
import sys

def dfs(target: int) -> None:
    if target == n:
        global count
        count += 1
    elif target < n:
        for num in [1, 2, 3]:
            dfs(target + num)

test = int(sys.stdin.readline())
for _ in range(test):
    n = int(sys.stdin.readline())
    count = 0
    dfs(0)
    print(count)