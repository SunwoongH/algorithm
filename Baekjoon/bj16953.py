'''
Created by sunwoong 2022/05/13
'''
import sys

a, b = map(int, sys.stdin.readline().split())
order = ['add', 'mul']

result = -1
def dfs(num: int, count: int) -> None:
    if num == b:
        global result
        if result != -1:
            result = min(result, count)
        else:
            result = count
        return
    elif num > b:
        return
    for operation in order:
        if operation == 'add':
            dfs(int(str(num) + '1'), count + 1)
        else:
            dfs(num * 2, count + 1)
dfs(a, 1)
print(result)