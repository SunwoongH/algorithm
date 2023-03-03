'''
Created by sunwoong on 2023/03/03
'''
import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

def dijkstra(start, end):
    distance = [sys.maxsize for _ in range(n * n)]
    distance[start] = 0
    heap = [(0, start)]
    while heap:
        cost, curr = heapq.heappop(heap)
        if distance[curr] < cost:
            continue
        for next, next_cost in graph[curr]:
            if distance[next] > distance[curr] + next_cost:
                distance[next] = distance[curr] + next_cost
                heapq.heappush(heap, (distance[next], next))
    return distance[end] + board[start // n][start % n]


t = int(input())
move = [(1, 0), (-1, 0), (0, -1), (0, 1)]
for _ in range(t):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    graph = defaultdict(list)
    for r in range(n):
        for c in range(n):
            for oper in move:
                dr = r + oper[0]
                dc = c + oper[1]
                if 0 <= dr < n and 0 <= dc < n:
                    graph[r * n + c].append((dr * n + dc, board[dr][dc]))
    print(dijkstra(0, n * n - 1))