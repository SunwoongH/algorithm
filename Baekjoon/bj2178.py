'''
문제 - 미로 탐색

풀이 방법 - graph를 인접 행렬로 만들고 BFS로 이동할 수 있는 칸인 1을 방문할 때 이전에 방문했던 장소의 값 + 1을 저장하는
           방식으로 최종 목적지까지 진행하며 풀이.
'''
import sys
import collections

n, m = map(int, sys.stdin.readline().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().rstrip('\n'))))
    
loc_x = [-1, 0, 1, 0]
loc_y = [0, 1, 0, -1]
def bfs(x, y):
    queue = collections.deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + loc_x[i]
            ny = y + loc_y[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
bfs(0, 0)
print(graph[n - 1][m - 1])