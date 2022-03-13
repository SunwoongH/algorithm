'''
Created by sunwoong on 2022/03/13
'''
import sys

n = int(sys.stdin.readline())
sequence = list(map(int, sys.stdin.readline().split()))
count = list(map(int, sys.stdin.readline().split()))
operation = ('+', '-', '*', '/')
counter = {}
for i in range(len(operation)):
    counter[operation[i]] = count[i]

max_result = -sys.maxsize
min_result = sys.maxsize
def dfs(start, result):
    if sum(counter.values()) == 0:
        global max_result, min_result
        max_result = max(max_result, result)
        min_result = min(min_result, result)
        return
    for o in operation:
        if counter[o] > 0:
            counter[o] -= 1
            if o == '+':
                dfs(start + 1, result + sequence[start])
            elif o == '-':
                dfs(start + 1, result - sequence[start])
            elif o == '*':
                dfs(start + 1, result * sequence[start])
            else:
                if result < 0:
                    dfs(start + 1, -(abs(result) // sequence[start]))
                else:
                    dfs(start + 1, result // sequence[start])
            counter[o] += 1
dfs(1, sequence[0])
print(max_result)
print(min_result)