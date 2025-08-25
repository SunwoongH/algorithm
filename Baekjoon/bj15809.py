import sys

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

def union(option, a, b):
    a = find(a)
    b = find(b)

    if option == 1:
        if a < b:
            parent[b] = a
            costs[a] += costs[b]
            costs[b] = 0
        else:
            parent[a] = b
            costs[b] += costs[a]
            costs[a] = 0
    else:
        if costs[a] < costs[b]:
            parent[a] = b
            costs[b] -= costs[a]
            costs[a] = 0
        elif costs[a] > costs[b]:
            parent[b] = a
            costs[a] -= costs[b]
            costs[b] = 0
        else:
            costs[a] = 0
            costs[b] = 0

n, m = map(int, sys.stdin.readline().split())
costs = [0] + [int(sys.stdin.readline()) for _ in range(n)]
parent = [0] + [i for i in range(1, n + 1)]
order = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
for option, a, b in order:
    union(option, a, b)
count = 0
answer = []
for cost in costs:
    if cost > 0:
        count += 1
        answer.append(cost)
answer.sort()
print(count)
print(*answer)