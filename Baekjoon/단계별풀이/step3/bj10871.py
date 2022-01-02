n, x = map(int, input().split())
list = list(map(int, input().split()))

for num in list:
    if num < x:
        print(num, end = ' ')

