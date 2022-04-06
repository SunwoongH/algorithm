'''
Created by sunwoong on 2022/04/06
'''
import sys

n = int(sys.stdin.readline())
eggs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result, broken = -sys.maxsize, [False] * n
def dfs(position: int, count: int) -> None:
    global result
    if position == n:
        result = max(result, count)
        return
    if broken[position]:
        dfs(position + 1, count)
    else:
        for i in range(n):
            if i != position and not broken[i]:
                broken_count = 0
                eggs[position][0] -= eggs[i][1]
                eggs[i][0] -= eggs[position][1]
                if eggs[position][0] <= 0:
                    broken[position], broken_count = True, broken_count + 1
                if eggs[i][0] <= 0:
                    broken[i], broken_count = True, broken_count + 1
                dfs(position + 1, count + broken_count)
                eggs[position][0] += eggs[i][1]
                eggs[i][0] += eggs[position][1]
                broken[position], broken[i] = False, False
        result = max(result, count)
dfs(0, 0)
print(result)