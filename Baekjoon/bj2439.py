n = int(input())

for i in range(0, n):
    print("{1:>{0}}".format(n, '*' * (i + 1)))