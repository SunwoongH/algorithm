'''
문제 - 코스 스케줄

0을 완료하기 위해서는 1을 끝내야 한다는 것을 [0, 1] 쌍으로 표현하는 n개의 코스가 있다.
코스 개수 n과 이 쌍들을 입력으로 받았을 때 모든 코스가 완료 가능한지 판별하라.
'''
from typing import List
import collections

# DFS(재귀) 풀이 - 그래프의 순환 구조를 판별하는 방식
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = collections.defaultdict(list)
        for v, w in prerequisites:
            graph[v].append(w)
        visited = [0 for _ in range(numCourses)]
        def dfs(v):
            if visited[v] == -1: # v에 연결된 다른 노드들을 방문 중인 경우, 즉, v의 완전탐색이 끝나지 않은 경우
                return False
            elif visited[v] == 1: # v에 연결된 다른 노드들이 모두 방문 되었을때 즉, v의 완전탐색이 이루어진 경우
                return True
            visited[v] = -1
            for w in graph[v]:
                if not dfs(w):
                    return False
            visited[v] = 1
            return True
        for v in range(numCourses):
            if not dfs(v):
                return False
        return True