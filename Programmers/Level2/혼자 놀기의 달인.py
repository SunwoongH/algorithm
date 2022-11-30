'''
Created by sunwoong on 2022/11/30
'''
from collections import defaultdict

def dfs(curr, visited, boxes):
    if visited[curr]:
        return 0
    visited[curr] = True
    depth = 1
    for next in boxes[curr]:
        if not visited[next]:
            depth += dfs(next, visited, boxes)
    return depth
    

def solution(cards):
    boxes = defaultdict(list)
    answer = []
    for i in range(len(cards)):
        boxes[i + 1].append(cards[i])
    visited = [False for _ in range(len(cards) + 1)]
    for i in range(1, len(cards) + 1):
        depth = dfs(i, visited, boxes)
        if depth > 0:
            answer.append(depth)
        if all(visited[1:]):
            if i == 1:
                return 0
            break
    answer.sort(reverse=True)
    return answer[0] * answer[1]