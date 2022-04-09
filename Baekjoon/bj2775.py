'''
Created by sunwoong on 2022/04/09
'''
test = int(input())
for _ in range(test):
    k, n = int(input()), int(input())
    data = list(range(n + 1))
    for i in range(1, k + 1):
        for j in range(2, n + 1):
            data[j] += data[j - 1]
    print(data[n])