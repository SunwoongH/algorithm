import sys

n = int(sys.stdin.readline())
coordinate = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    temp = (y, x)
    coordinate.append(temp)
coordinate = sorted(coordinate)
for v in coordinate:
    print(v[1], v[0])