year = int(input())
check = 0
if year % 4 == 0:
    if year % 400 == 0:
        check = 1
    elif year % 100 != 0:
        check = 1
print(check)