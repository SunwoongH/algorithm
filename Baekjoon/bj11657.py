'''
문제 - 타임머신

풀이 방법 - 음수 가중치가 존재하는 조건이 있기 때문에 벨만 포드 최단 경로 알고리즘으로 풀이.

>>> 음수 가중치가 존재하는 모든 그래프에서 최단 경로를 구할 수 있는 것은 아니다. 만약 음수 가중치를 가진 그래프에서
음수 값이 더 큰 음수 순환 경로가 존재할 경우에 무한히 최소 경로의 값이 낮아지기 때문에 최단 경로를 구할 수 없다.
따라서 음수 순환 경로가 존재하는지 확인하는 조건이 필요하다. 해당 조건은 음수 순환 경로가 존재할 경우 매 반복마다 
값이 갱신되는 특징을 활용하여 확인할 수 있다. 즉, 정점이 n개 일 때 최단 경로를 구할 수 있는 최악의 횟수인 n - 1번 
반복 이후 한 번 더 반복을 해서 이때 최소 경로 값이 갱신되는 경우 음수 순환 경로가 존재하는 것이다. 또한 모든 그래프가
연결 그래프는 아니므로 비연결 그래프가 주어질 경우에 대한 조건도 필요하다. float('inf')를 사용하여 값의 변경을 막거나
아래의 풀이와 같이 기준 노드의 경로 값이 sys.maxsize(INF)가 아닌 경우에만 가능하도록 조건을 추가하는 것이 필요하다.
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = collections.defaultdict(list)
for _ in range(m):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

def bellman_ford(n: int, start: int):
    distance = [sys.maxsize] * (n + 1)
    distance[start] = 0
    for i in range(n):
        for v in graph:
            for adj_v, adj_dist in graph[v]:
                if distance[v] != sys.maxsize and distance[adj_v] > distance[v] + adj_dist:
                    distance[adj_v] = distance[v] + adj_dist
                    if i == n - 1:
                        return -1
    return distance

distance = bellman_ford(n, 1)
if distance == -1: print(-1)
else:
    for dist in distance[2:]:
        if dist == sys.maxsize: print(-1)
        else: print(dist)