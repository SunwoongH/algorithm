'''
문제 - 원점에 k번째로 가까운 점

평면상에 points 목록이 있을 때 원점 (0, 0)에서 k번 가까운 점 목록을 순서대로 출력하라.
평면상 두 점의 거리는 유클리드 거리로 한다.
'''
from typing import List
import heapq
import math

# 딕셔너리 풀이
class Solution1:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        index_table = {}
        for i in range(len(points)):
            index_table[i] = math.sqrt(points[i][0] ** 2 + points[i][1] ** 2)
        index_table = sorted(index_table, key=index_table.get)
        return [points[i] for i in index_table][:k]

# heapq 모듈 활용 풀이
class Solution2:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = math.sqrt(point[0] ** 2 + point[1] ** 2)
            heapq.heappush(heap, (distance, point))
        return [heapq.heappop(heap)[1] for _ in range(k)]