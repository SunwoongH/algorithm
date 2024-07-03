'''
Created by sunwoong on 2024/07/03

풀이 시간 - 해설 참조 (완전탐색 시간 초과 TC 있음, 추가 해설 참고하기)
'''
from collections import defaultdict

def dfs(curr, sheep, wolf, promising, info, graph, answer):
    sheep += info[curr] ^ 1
    wolf += info[curr]
    if wolf >= sheep:
        return
    answer.append(sheep)
    for next in promising:
        promising |= set(graph[next])
        promising.remove(next)
        dfs(next, sheep, wolf, promising, info, graph, answer)
        promising.add(next)
        promising -= set(graph[next])

def solution(info, edges):
    answer = []
    graph = defaultdict(list)
    for parent, child in edges:
        graph[parent].append(child)
    dfs(0, 0, 0, set(graph[0]), info, graph, answer)
    return max(answer)