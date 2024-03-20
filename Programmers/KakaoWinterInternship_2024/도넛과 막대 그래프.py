'''
Created by sunwoong on 2024/03/20

풀이 시간 - 60분
'''
from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)

def search(curr, start, visited, graph, count, in_table, out_table):
    if visited[curr]:
        if start == curr:
            count += 1
        return count, False
    flag = False
    visited[curr] = True
    if in_table[curr] == 2 and out_table[curr] == 2:
        flag = True
    for next in graph[curr]:
        count, new_flag = search(next, start, visited, graph, count, in_table, out_table)
        if new_flag:
            flag = new_flag
    return count, flag

def solution(edges):
    node = 1
    in_table = defaultdict(int)
    out_table = defaultdict(int)
    graph = defaultdict(list)
    for start, end in edges:
        if start > node:
            node = start
        if end > node:
            node = end
        graph[start].append(end)
        in_table[end] += 1
        out_table[start] += 1
    start_node = None
    for n in range(1, node + 1):
        if out_table[n] >= 2 and in_table[n] == 0:
            start_node = n
            break
    answer = [start_node, 0, 0, 0]
    visited = [False for _ in range(node + 1)]
    for curr in graph[start_node]:
        in_table[curr] -= 1
        count, flag = search(curr, curr, visited, graph, 0, in_table, out_table)
        if count == 1:
            if flag:
                answer[3] += 1
            else:
                answer[1] += 1
        elif count == 2:
            answer[3] += 1
        else:
            answer[2] += 1
    return answer