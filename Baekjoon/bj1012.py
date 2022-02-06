'''
문제 - 유기농 배추

풀이 방법 - 재귀 구조 DFS로 상,하,좌,우 탐색하여 풀이

>>> 처음 제출 시 런타임 에러(RecursionError)가 발생했었다. 이는 파이썬에서 재귀 깊이를
최대 1000으로 제한했기 때문에 발생한 에러였고 sys 모듈을 통해 최대 재귀 깊이를 늘려서 해결하였다.
파이썬의 재귀 깊이에 대해서 처음 알게 되었고 앞으로 문제를 풀면서 재귀 함수를 활용할 때 고려해야겠다.
'''
import sys
sys.setrecursionlimit(10000)

def dfs(i, j):
    if i < 0 or i >= n or j < 0 or j >= m or graph[i][j] == 0:
        return
    graph[i][j] = 0
    dfs(i, j + 1)
    dfs(i, j - 1)
    dfs(i - 1, j)
    dfs(i + 1, j)

test = int(sys.stdin.readline())
for _ in range(test):
    m, n, k = map(int, sys.stdin.readline().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        v, w = map(int, sys.stdin.readline().split())
        graph[w][v] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                dfs(i, j)
                result += 1
    print(result)