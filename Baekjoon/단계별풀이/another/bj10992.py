n = int(input())
mul = 1
temp = n - 1
for i in range(1, n + 1):
    print(' ' * temp, end='')
    if i == 1: print('*')
    elif i == n: print('*' * (i * 2 - 1))
    else:
        print('*' + ' ' * mul + '*')
        mul += 2
    temp -= 1