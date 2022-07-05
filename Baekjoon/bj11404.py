'''
Created by sunwoong on 2022/07/05
'''
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
city = [[sys.maxsize for _ in range(n)] for _ in range(n)]
for _ in range(m):
    u, v, cost = map(int, sys.stdin.readline().split())
    city[u - 1][v - 1] = min(cost, city[u - 1][v - 1])
for r in range(n):
    for c in range(n):
        if r == c:
            city[r][c] = 0

def floyd():
    for k in range(n):
        for r in range(n):
            for c in range(n):
                if city[r][c] > city[r][k] + city[k][c]:
                    city[r][c] = city[r][k] + city[k][c]
                    
floyd()
for line in city:
    for node in line:
        if node == sys.maxsize:
            print(0, end=' ')
        else:
            print(node, end=' ')
    print()