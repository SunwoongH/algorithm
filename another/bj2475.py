num = list(map(int, input().split()))
for i in range(len(num)): num[i] **= 2
print(sum(num) % 10)