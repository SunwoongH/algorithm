import sys

n = int(sys.stdin.readline())
countingArray = [0] * 10001
for i in range(n):
    countingArray[int(sys.stdin.readline())] += 1
for i in range(10001):
    while countingArray[i] != 0:
        print(i)
        countingArray[i] -= 1