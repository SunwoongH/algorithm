'''
Created by sunwoong on 2022/10/01
'''
import collections

def bfs(n, computers, start):
    queue = collections.deque([start])
    computers[start][start] = 0
    while queue:
        curr = queue.popleft()
        for next in range(n):
            if computers[curr][next]:
                computers[curr][next] = computers[next][curr] = computers[next][next] = 0
                queue.append(next)
    return computers
                
def solution(n, computers):
    answer = 0
    for start in range(n):
        if computers[start][start] == 1:
            computers = bfs(n, computers, start)
            answer += 1
    return answer