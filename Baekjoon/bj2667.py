'''
문제 - 단지 번호 붙이기

풀이 방법 - graph를 인접 행렬로 만든 후 DFS(재귀) 동,서,남,북 탐색 풀이

>>> LeetCode에서 풀었던 "섬의 개수" 문제와 유사한 문제라 바로 접근하여 풀 수 있었다.
'''
import sys

n = int(sys.stdin.readline())
graph = []
for _ in range(n):
    graph.append(list(sys.stdin.readline().rstrip('\n')))

house = {}
def dfs(house_num, i, j):
    if i < 0 or i >= n or j < 0 or j >= n or graph[i][j] == '0':
        return
    graph[i][j] = '0'
    house[house_num] += 1
    dfs(house_num, i, j + 1)
    dfs(house_num, i, j - 1)
    dfs(house_num, i - 1, j)
    dfs(house_num, i + 1, j)

house_num = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == '1':
            house_num += 1
            house[house_num] = 0
            dfs(house_num, i, j)
print(house_num)
house = sorted(house.values())
print(*house, sep='\n')