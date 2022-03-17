'''
Created by sunwoong on 2022/03/17
'''
import sys

n = int(sys.stdin.readline())
number = list(map(int, sys.stdin.readline().split()))

result = -sys.maxsize
check = [False] * n
def dfs(prev: int, count: int, sum_of_num: int) -> None:
    if count == n - 1:
        global result
        result = max(result, sum_of_num)
        return
    for i in range(n):
        if not check[i]:
            check[i] = True
            dfs(number[i], count + 1, sum_of_num + abs(prev - number[i]))
            check[i] = False
for i in range(n):
    check[i] = True
    dfs(number[i], 0, 0)
    check[i] = False
print(result)