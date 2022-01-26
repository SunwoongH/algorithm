'''
문제 - 섬의 개수

1을 육지로 0을 물로 가정한 2D 그리드 맵이 주어졌을 때 섬의 개수를 계산하라.
'''
from typing import List

# DFS(재귀) 주어진 행렬 데이터를 그래프화 시킨 후 DFS 탐색하여 풀이
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]) or grid[i][j] != '1':
                return
            grid[i][j] = '0'
            dfs(i, j + 1)
            dfs(i, j - 1)
            dfs(i + 1, j)
            dfs(i - 1, j)
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i, j)
                    result += 1
        return result