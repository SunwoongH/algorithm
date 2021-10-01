import sys

n = int(sys.stdin.readline())
coordinate = []
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    temp = (x, y)
    coordinate.append(temp)
coordinate = sorted(coordinate)
for v in coordinate:
    print(v[0], v[1])