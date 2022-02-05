n = int(input())

for i in range(1, n * 2):
    if i == n - 1: temp = i
    if i <= n:
        print('*' * i, end='')
        print(' ' * (n * 2 - i * 2), end='')
        print('*' * i)
    else:
        print('*' * temp, end='')
        print(' ' * (n * 2 - temp * 2), end='')
        print('*' * temp)
        temp -= 1