'''
Created by sunwoong on 2022/07/29
'''
import sys
import collections

n = int(sys.stdin.readline())
flower = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
sum_flower = [[0 for _ in range(n)] for _ in range(n)]

for r in range(1, n - 1):
    for c in range(1, n - 1):
        sum_flower[r][c] = flower[r - 1][c] + flower[r + 1][c] \
            + flower[r][c - 1] + flower[r][c + 1] + flower[r][c]

result = sys.maxsize
move = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
def dfs(depth: int, target: int) -> None:
    if depth == 3:
        global result
        result = min(result, target)
        return
    temp = collections.deque()
    for r in range(1, n - 1):
        for c in range(1, n - 1):
            is_possible = True
            for oper in move:
                if sum_flower[r + oper[0]][c + oper[1]] == -1:
                    is_possible = False
                    break
            if is_possible:
                for oper in move:
                    temp.append(sum_flower[r + oper[0]][c + oper[1]])
                    sum_flower[r + oper[0]][c + oper[1]] = -1
                dfs(depth + 1, target + temp[-1])
                for oper in move:
                    sum_flower[r + oper[0]][c + oper[1]] = temp.popleft()
dfs(0, 0)
print(result)