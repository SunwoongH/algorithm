'''
Created by sunwoong on 2023/02/12
'''
import sys
input = sys.stdin.readline

parent = None

def find(a):
    while parent[a] != -1:
        a = parent[a]
    return a

def union(a_parent, b_parent):
    if a_parent < b_parent:
        parent[b_parent] = a_parent
    else:
        parent[a_parent] = b_parent

def kruskal(n, edges):
    edge_count = 0
    costs = 0
    while edge_count < n - 1:
        u, v, cost = edges.pop()
        a_parent = find(u)
        b_parent = find(v)
        if a_parent != b_parent:
            union(a_parent, b_parent)
            edge_count += 1
            costs += cost
    return costs

def find_optimaize_value(data, target, pos, planet):
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid][1][pos] < target:
            left = mid + 1
        else:
            right = mid - 1
    if left == len(data):
        if data[right][0] == planet:
            return False, right - 1
        return False, right
    elif right == -1:
        if data[left][0] == planet:
            return False, left + 1
        return False, left
    else:
        if data[left][0] == planet:
            if left + 1 < len(data):
                return True, right, left + 1
            else:
                return False, right
        return True, left, right

n = int(input())
parent = [-1 for _ in range(n)]
planets = []
heap = []
for i in range(n):
    x, y, z = map(int, input().split())
    planets.append((i, (x, y, z)))
if n == 1:
    print(0)
    sys.exit(0)
sorted_by_x = sorted(planets, key=lambda x: x[1][0])
sorted_by_y = sorted(planets, key=lambda x: x[1][1])
sorted_by_z = sorted(planets, key=lambda x: x[1][2])
edges = []
for planet, position in planets:
    x, y, z = position
    result = find_optimaize_value(sorted_by_x, x, 0, planet)
    if result[0]:
        edges.append((planet, sorted_by_x[result[2]][0], abs(x - sorted_by_x[result[2]][1][0])))
    edges.append((planet, sorted_by_x[result[1]][0], abs(x - sorted_by_x[result[1]][1][0])))
    result = find_optimaize_value(sorted_by_y, y, 1, planet)
    if result[0]:
        edges.append((planet, sorted_by_y[result[2]][0], abs(y - sorted_by_y[result[2]][1][1])))
    edges.append((planet, sorted_by_y[result[1]][0], abs(y - sorted_by_y[result[1]][1][1])))
    result = find_optimaize_value(sorted_by_z, z, 2, planet)
    if result[0]:
        edges.append((planet, sorted_by_z[result[2]][0], abs(z - sorted_by_z[result[2]][1][2])))
    edges.append((planet, sorted_by_z[result[1]][0], abs(z - sorted_by_z[result[1]][1][2])))
edges.sort(key=lambda x: x[2], reverse=True)
print(kruskal(n, edges))