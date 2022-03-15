'''
Created by sunwoong on 2022/03/15
'''
import sys

lotto = []
def dfs(start: int) -> None:
    if len(lotto) == 6:
        print(*lotto)
        return
    for i in range(start, k):
        lotto.append(number[i])
        dfs(i + 1)
        lotto.pop()

while True:
    number = list(map(int, sys.stdin.readline().split()))
    k = number.pop(0)
    if not k:
        break
    dfs(0)
    print()