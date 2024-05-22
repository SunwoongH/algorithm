'''
Created by sunwoong on 2024/05/22

풀이 시간 - 20분
'''
def find(parent, n):
    if parent[n] != n:
        parent[n] = find(parent, parent[n])
    return parent[n]

def union(parent, u, v):
    parent_u = find(parent, u)
    parent_v = find(parent, v)
    if parent_u < parent_v:
        parent[parent_v] = parent_u
    else:
        parent[parent_u] = parent_v

def solution(n, costs):
    costs.sort(key=lambda x: -x[2])
    parent = [i for i in range(n)]
    edge_count = 0
    answer = 0
    while edge_count < n - 1:
        u, v, cost = costs.pop()
        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            edge_count += 1
            answer += cost
    return answer