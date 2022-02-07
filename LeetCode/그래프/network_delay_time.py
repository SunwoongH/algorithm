'''
문제 - 네트워크 딜레이 타임

k부터 출발해 모든 노드가 신호를 받을 수 있는 시간을 계산하라. 불가능할 경우 -1을 반환한다.
입력값 (v, w, time)은 각각 출발지, 도착지, 소요 시간으로 구성되며, 전체 노드의 개수는 n이다.
'''
from typing import List
import sys
import heapq
import collections

# dijkstra(최소 힙) 풀이
class Solution1:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for v, w, time in times:
            graph[v].append((w, time))
        delay_time = [sys.maxsize] * (n + 1)
        delay_time[k] = 0
        heap = [(0, k)]
        while heap:
            time, v = heapq.heappop(heap)
            if delay_time[v] < time:
                continue
            for adj_v, adj_time in graph[v]:
                if delay_time[adj_v] > time + adj_time:
                    delay_time[adj_v] = time + adj_time
                    heapq.heappush(heap, (delay_time[adj_v], adj_v))
        result = max(delay_time[1:])
        if result == sys.maxsize:
            return -1
        return result

# dijkstra(최소 힙) 풀이 - 최적화
class Solution2:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for v, w, time in times:
            graph[v].append((w, time))
        delay_time = collections.defaultdict(int)
        heap = [(0, k)]
        while heap:
            time, v = heapq.heappop(heap)
            if v not in delay_time:
                delay_time[v] = time
                for adj_v, adj_time in graph[v]:
                    heapq.heappush(heap, (time + adj_time, adj_v))
        if len(delay_time) == n:
            return max(delay_time.values())
        return -1
    
# dijkstra(순차 탐색) 풀이
class Solution3:
    def getMinDelayTimeNode(self, delay_time: List[int], visited: List[bool]) -> int:
        smallest = 0
        for i in range(1, len(delay_time)):
            if delay_time[smallest] > delay_time[i] and not visited[i]:
                smallest = i
        return smallest
    
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for v, w, time in times:
            graph[v].append((w, time))
        delay_time = [sys.maxsize] * (n + 1)
        visited = [False] * (n + 1)
        delay_time[k] = 0
        for _ in range(n - 1):
            smallest = self.getMinDelayTimeNode(delay_time, visited)
            visited[smallest] = True
            for adj_v, adj_time in graph[smallest]:
                if delay_time[adj_v] > delay_time[smallest] + adj_time:
                    delay_time[adj_v] = delay_time[smallest] + adj_time
        result = max(delay_time[1:])
        if result == sys.maxsize:
            return -1
        return result