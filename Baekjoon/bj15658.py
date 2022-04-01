'''
Created by sunwoong on 2022/04/01
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
operation = ('+', '-', '*', '/')
count = list(map(int, sys.stdin.readline().split()))
operation_count = dict()
for i in range(4):
    operation_count[operation[i]] = count[i]

min_result, max_result = sys.maxsize, -sys.maxsize
def dfs(start: int, prev: int) -> None:
    if start == n:
        global min_result, max_result
        min_result = min(min_result, prev)
        max_result = max(max_result, prev)
        return
    for oper in operation:
        if operation_count[oper]:
            operation_count[oper] -= 1
            if oper == '+':
                dfs(start + 1, prev + sequence[start])
            elif oper == '-':
                dfs(start + 1, prev - sequence[start])
            elif oper == '*':
                dfs(start + 1, prev * sequence[start])
            else:
                dfs(start + 1, prev // sequence[start] if prev > 0 else -(abs(prev) // sequence[start]))
            operation_count[oper] += 1
dfs(1, sequence[0])
print(max_result, min_result, sep='\n')