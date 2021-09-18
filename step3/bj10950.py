T = int(input())

list = []
for i in range(0, T):
    A, B = map(int, input().split())
    list.append([A, B])

for i in list:
    print(i[0] + i[1])