'''
문제 - 최소 높이 트리

노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록을 반환하라.

>>> 무방향 그래프에서 '최소' 높이 트리가 되는 정점은 그래프에서 가장 중앙에 위치한 정점일 것이다. 주어진 그래프에서 리프 노드를
하나씩 제거해 나가면 마지막에는 중앙에 위치한 노드만 남게 될 것이고 해당 노드는 최소 높이 트리를 구성할 수 있는 루트 노드가 될 것이다. 
다만, 중앙 노드는 항상 한 개가 아니며 두 개인 경우도 발생하기 때문에 이에 대한 조건을 추가로 설정 해야한다. 아래는 앞서서 설명한
방식으로 풀이하였다. 이 문제의 핵심은 '최소' 높이를 구성할 수 있는 트리의 조건은 무엇일까? 에 대해 먼저 고민하여 접근 방법을 
고안해내는 것인 것 같다. 항상 문제를 풀기 전에 충분한 생각을 통해 문제의 핵심을 먼저 파악하고 풀이를 진행해야할 필요성을 많이 느끼게
된 문제이다.
'''
from typing import List
import collections

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = collections.defaultdict(list)
        for v, w in edges:
            graph[v].append(w)
            graph[w].append(v)
        leaves = []
        for i in range(n + 1):
            if len(graph[i]) == 1:
                leaves.append(i)
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            leaves = new_leaves
        return leaves