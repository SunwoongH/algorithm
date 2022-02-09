'''
문제 - k 경유지 내 가장 저렴한 항공권

시작점에서 도착점까지의 가장 저렴한 가격을 계산하되, k개의 경유지 이내에 도착하는 가격을 반환하라.
경로가 존재하지 않을 경우 -1을 반환한다.

>>> 첫 번째 풀이는 거의 완전 탐색에 가까워서 중복 검사가 발생하기 때문에 시간 초과가 발생한 것으로 생각된다.
이를 해결하기 위해 검사하지 않아도 되는 간선을 탐지할 추가 조건이 필요하다고 판단했다. 임의의 정점이 방문된 이후
다른 간선으로 동일 정점을 방문하려고 할 때 해당 간선의 stopover 값이 현재 정점의 stopover 값보다 작거나 같을 경우는
이미 이전에 방문했을 때가 최적이기 때문에 해당 간선을 검사할 필요가 없다. 따라서 두 번째 풀이에서 해당 조건에 대한 
추가 조건을 설정하여 해결하였다.
'''
from typing import List
import collections
import heapq

# dijkstra 풀이 - 시간 초과
class Solution1:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        heap = [(0, src, k)]
        while heap:
            price, v, stopover = heapq.heappop(heap)
            if v == dst:
                return price
            if stopover >= 0:
                for adj_v, adj_price in graph[v]:
                    heapq.heappush(heap, (price + adj_price, adj_v, stopover - 1))
        return -1

# dijkstra 풀이 - 인접한 정점을 방문할 때마다 주어진 k값을 감소 시키면서 최종적으로 k개의 경유지 이내에 목적지에 도착하도록 조건 설정
class Solution2:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        heap = [(0, src, k)]
        visited = collections.defaultdict(int)
        while heap:
            price, v, stopover = heapq.heappop(heap)
            if v == dst:
                return price
            if stopover >= 0:
                if v not in visited or visited[v] < stopover:
                    visited[v] = stopover
                    for adj_v, adj_price in graph[v]:
                        heapq.heappush(heap, (price + adj_price, adj_v, stopover - 1))
        return -1