'''
문제 - N과 M (5)

풀이 방법 - 재귀 구조 DFS로 풀이
'''
import sys

n, m = map(int, sys.stdin.readline().split())
nums = sorted(list(map(int, sys.stdin.readline().split())))
results = []
path = []
def dfs() -> None:
    if len(path) == m:
        results.append(path[:])
        return
    for num in nums:
        if num not in path:
            path.append(num)
            dfs()
            path.pop()
dfs()
for result in results:
    print(*result)