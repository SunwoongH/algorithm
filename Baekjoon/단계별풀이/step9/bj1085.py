data = list(map(int, input().split()))
data[2] -= data[0]
data[3] -= data[1]
print(min(data))