'''
Created by sunwoong on 2022/09/11
'''
import sys

def floyd() -> None:
    for k in range(n):
        for r in range(n):
            for c in range(n):
                if distance[r][c] > distance[r][k] + distance[k][c]:
                    distance[r][c] = distance[r][k] + distance[k][c]
    
n, m = map(int, sys.stdin.readline().split())
distance = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
floyd()
for _ in range(m):
    start, end, time = map(int, sys.stdin.readline().split())
    print("Enjoy other party") if distance[start - 1][end - 1] <= time else print("Stay here")