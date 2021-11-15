import sys

n = int(sys.stdin.readline())
time = sorted(list(map(int, sys.stdin.readline().split())))
result_time = 0
temp_time = 0
for i in range(n):
    temp_time += time[i]
    result_time += temp_time
print(result_time)