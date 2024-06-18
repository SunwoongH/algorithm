'''
Created by sunwoong on 2024/06/18

풀이 시간 - 20분
'''
from collections import deque

def bfs(begin, target, words):
    visited = [False for _ in range(len(words))]
    queue = deque([(begin, 0)])
    while queue:
        curr, convert = queue.popleft()
        if curr == target:
            return convert
        for i in range(len(words)):
            count = 0
            if visited[i]:
                continue
            for j in range(len(words[i])):
                if curr[j] != words[i][j]:
                    count += 1
            if count == 1:
                visited[i] = True
                queue.append((words[i], convert + 1))
    return 0

def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin, target, words)