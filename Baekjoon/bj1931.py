import sys

n = int(sys.stdin.readline())
conference = []
for i in range(n):
    start, end = map(int, sys.stdin.readline().split())
    conference.append([start, end, end - start])
conference = sorted(conference, key = lambda x: (x[1], x[0], x[2]))
result = 0
endTime = -1
for data in conference:
    if endTime <= data[0]:
        result += 1
        endTime = data[1]
print(result)