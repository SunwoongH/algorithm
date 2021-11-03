import sys

wCount = 0
bCount = 0

def confetti(data, size, i, j):
    global wCount, bCount
    if size == 1:
        if data[i][j] == 1: bCount += 1
        else: wCount += 1
        return
    else:
        checkSum = 0
        for r in range(i, i + size):
            for c in range(j, j + size):
                checkSum += data[r][c]
        if checkSum == 0: 
            wCount += 1
            return
        elif checkSum == size ** 2:
            bCount += 1
            return
        else:
            confetti(data, size // 2, i, j)
            confetti(data, size // 2, i + size // 2, j)
            confetti(data, size // 2, i, j + size // 2)
            confetti(data, size // 2, i + size // 2, j + size // 2)

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

confetti(data, n, 0, 0)
print(wCount)
print(bCount)